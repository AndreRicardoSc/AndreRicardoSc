#!/usr/bin/env python3
"""Gera assets/contributions.svg a partir da API GraphQL do GitHub.

Usa apenas a biblioteca padrão do Python (sem dependências externas).
Autentica com um token do GitHub fornecido pela variável de ambiente GITHUB_TOKEN.

Uso local:
    GITHUB_USERNAME=AndreRicardoSc GITHUB_TOKEN=<token> python scripts/generate_contributions.py
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone

API_URL = "https://api.github.com/graphql"
OUTPUT_PATH = os.path.join("assets", "contributions.svg")

DAYS = 371  # 53 semanas completas (inclui a semana corrente)
CELL = 11
GAP = 3
STEP = CELL + GAP
LEFT_PAD = 34
TOP_PAD = 30
BOTTOM_PAD = 26
RADIUS = 2

BG = "#0D1117"
BORDER = "#30363D"
EMPTY = "#161B22"
TEXT = "#C9D1D9"
MUTED = "#8B949E"
ACCENT = "#3FB950"
LEVELS = ["#0E4429", "#006D32", "#26A641", "#39D353"]

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""


def fetch_calendar(login: str, token: str) -> dict:
    now = datetime.now(timezone.utc)
    variables = {
        "login": login,
        "from": (now - timedelta(days=DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    payload = json.dumps({"query": QUERY, "variables": variables}).encode("utf-8")
    request = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "profile-contributions-graph",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        body = json.loads(response.read().decode("utf-8"))

    if "errors" in body:
        raise RuntimeError(f"Erro na API GraphQL: {body['errors']}")
    return body["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def parse_days(calendar: dict) -> list[dict]:
    days: list[dict] = []
    for week in calendar["weeks"]:
        for day in week["contributionDays"]:
            days.append(
                {
                    "date": date.fromisoformat(day["date"]),
                    "count": int(day["contributionCount"]),
                }
            )
    return days


def level_for(count: int, maximum: int) -> int:
    if count <= 0:
        return 0
    if maximum <= 1:
        return 4
    ratio = count / maximum
    if ratio <= 0.25:
        return 1
    if ratio <= 0.5:
        return 2
    if ratio <= 0.75:
        return 3
    return 4


def build_svg(days: list[dict], total: int) -> str:
    # Alinha a primeira coluna no domingo, como no gráfico oficial do GitHub.
    offset = (days[0]["date"].weekday() + 1) % 7
    maximum = max((day["count"] for day in days), default=0)

    columns = (len(days) + offset + 6) // 7
    width = LEFT_PAD + columns * STEP + 8
    height = TOP_PAD + 7 * STEP + BOTTOM_PAD

    parts: list[str] = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="Gráfico de contribuições: {total} contribuições nos últimos 12 meses">'
    )
    parts.append(f"<title>Contribuições de {total} no último ano</title>")
    parts.append(
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="8" '
        f'fill="{BG}" stroke="{BORDER}"/>'
    )

    # Rótulos dos dias da semana (segunda, quarta e sexta), como no GitHub.
    for row, label in ((1, "Seg"), (3, "Qua"), (5, "Sex")):
        y = TOP_PAD + row * STEP + CELL - 2
        parts.append(
            f'<text x="8" y="{y}" font-family="ui-sans-serif,Segoe UI,Helvetica,Arial" '
            f'font-size="9" fill="{MUTED}">{label}</text>'
        )

    # Rótulos de mês na primeira semana de cada mês.
    seen: set[tuple[int, int]] = set()
    for index, day in enumerate(days):
        key = (day["date"].year, day["date"].month)
        if key in seen:
            continue
        seen.add(key)
        column = (index + offset) // 7
        x = LEFT_PAD + column * STEP
        parts.append(
            f'<text x="{x}" y="{TOP_PAD - 8}" font-family="ui-sans-serif,Segoe UI,Helvetica,Arial" '
            f'font-size="9" fill="{MUTED}">{day["date"].strftime("%b")}</text>'
        )

    # Células.
    for index, day in enumerate(days):
        position = index + offset
        column, row = divmod(position, 7)
        x = LEFT_PAD + column * STEP
        y = TOP_PAD + row * STEP
        level = level_for(day["count"], maximum)
        fill = LEVELS[level - 1] if level else EMPTY
        parts.append(
            f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="{RADIUS}" '
            f'fill="{fill}"><title>{day["date"].isoformat()}: {day["count"]} contribuições</title></rect>'
        )

    # Resumo e legenda.
    baseline = TOP_PAD + 7 * STEP + 16
    parts.append(
        f'<text x="{LEFT_PAD}" y="{baseline}" font-family="ui-sans-serif,Segoe UI,Helvetica,Arial" '
        f'font-size="10" fill="{TEXT}">{total} contribuições nos últimos 12 meses</text>'
    )

    legend_x = width - 8 - (4 * STEP) - 26
    parts.append(
        f'<text x="{legend_x - 6}" y="{baseline}" text-anchor="end" '
        f'font-family="ui-sans-serif,Segoe UI,Helvetica,Arial" font-size="9" fill="{MUTED}">Menos</text>'
    )
    for level, fill in enumerate(LEVELS):
        x = legend_x + level * STEP
        parts.append(
            f'<rect x="{x}" y="{baseline - 9}" width="{CELL}" height="{CELL}" rx="{RADIUS}" fill="{fill}"/>'
        )
    parts.append(
        f'<text x="{legend_x + 4 * STEP + 4}" y="{baseline}" '
        f'font-family="ui-sans-serif,Segoe UI,Helvetica,Arial" font-size="9" fill="{MUTED}">Mais</text>'
    )

    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> int:
    login = os.environ.get("GITHUB_USERNAME")
    token = os.environ.get("GITHUB_TOKEN")

    if not login:
        print("GITHUB_USERNAME não definido.", file=sys.stderr)
        return 1
    if not token:
        print("GITHUB_TOKEN não definido.", file=sys.stderr)
        return 1

    try:
        calendar = fetch_calendar(login, token)
    except (urllib.error.URLError, RuntimeError, KeyError) as error:
        # Falha de rede ou de API não deve quebrar o workflow: o SVG existente é preservado.
        print(f"::warning::Não foi possível obter os dados de contribuição: {error}")
        return 0

    days = parse_days(calendar)
    if not days:
        print("::warning::Nenhum dia retornado pela API. SVG preservado.")
        return 0

    svg = build_svg(days, int(calendar.get("totalContributions", 0)))

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(svg)

    print(f"::notice::{OUTPUT_PATH} gerado com {len(days)} dias.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
