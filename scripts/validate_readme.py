#!/usr/bin/env python3
"""Valida o README do perfil.

Dois modos, executados separadamente pelo workflow:

    python scripts/validate_readme.py --structure   # offline, determinístico
    python scripts/validate_readme.py --links       # rede, informativo

--structure verifica:
  * presença das seções obrigatórias;
  * existência dos arquivos locais referenciados (ex.: assets/contributions.svg);
  * balanceamento mínimo do Markdown (blocos de código e tags <picture>/<p>).

--links verifica com requisições HEAD/GET:
  * URLs de imagens e links externos encontrados no README.
  Nunca reprova por falha de rede: apenas reporta avisos.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import urllib.error
import urllib.request

README_PATH = "README.md"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_SECTIONS = [
    "## Sobre mim",
    "## Tecnologias e ferramentas",
    "## Projetos em destaque",
    "## Estatísticas do GitHub",
    "## Contribuições",
    "## Contato",
]

REQUIRED_FILES = [
    "assets/contributions.svg",
    ".github/workflows/update-contributions.yml",
    ".github/workflows/validate-readme.yml",
    "scripts/generate_contributions.py",
    "scripts/validate_readme.py",
]

URL_PATTERN = re.compile(r"https?://[^\s\"')<>]+")
LOCAL_IMG_PATTERN = re.compile(r'(?:src|srcset)="(?!https?://|#)([^"]+)"')

# Serviços que podem recusar HEAD ou limitar taxa; tratados como aviso, não erro.
TOLERANT_HOSTS = (
    "img.shields.io",
    "komarev.com",
    "readme-typing-svg",
)


def read_readme() -> str:
    with open(os.path.join(REPO_ROOT, README_PATH), encoding="utf-8") as handle:
        return handle.read()


def check_structure(content: str) -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"Seção ausente: {section}")

    for relative in REQUIRED_FILES:
        if not os.path.exists(os.path.join(REPO_ROOT, relative)):
            errors.append(f"Arquivo referenciado não existe: {relative}")

    # Caminhos de imagem locais usados no README precisam existir de fato.
    for match in LOCAL_IMG_PATTERN.finditer(content):
        candidate = match.group(1).strip()
        if not candidate or candidate.startswith("data:"):
            continue
        if not os.path.exists(os.path.join(REPO_ROOT, candidate)):
            warnings.append(f"Imagem local não encontrada: {candidate}")

    if content.count("```") % 2 != 0:
        errors.append("Blocos de código ``` desbalanceados.")

    for tag in ("picture", "p", "h1", "h3"):
        openings = len(re.findall(rf"<{tag}[ >]", content))
        closings = len(re.findall(rf"</{tag}>", content))
        if openings != closings:
            errors.append(f"Tags <{tag}> desbalanceadas: {openings} aberturas / {closings} fechamentos.")

    if not re.search(r"^#\s", content, flags=re.MULTILINE) and "<h1" not in content:
        errors.append("README sem título principal (h1).")

    for item in warnings:
        print(f"::warning::{item}")
    for item in errors:
        print(f"::error::{item}")

    if errors:
        print(f"::error::Validação estrutural falhou com {len(errors)} erro(s).")
        return 1

    print(f"::notice::Estrutura do README validada ({len(REQUIRED_SECTIONS)} seções, {len(REQUIRED_FILES)} arquivos).")
    return 0


def check_links(content: str) -> int:
    urls = sorted(set(URL_PATTERN.findall(content)))
    if not urls:
        print("::warning::Nenhuma URL externa encontrada no README.")
        return 0

    unavailable: list[str] = []
    for url in urls:
        status = probe(url)
        if status is None:
            unavailable.append(url)

    if unavailable:
        for url in unavailable:
            print(f"::warning::Sem resposta: {url}")
        print(f"::warning::{len(unavailable)} de {len(urls)} URLs não responderam (informativo, não bloqueia).")
    else:
        print(f"::notice::Todas as {len(urls)} URLs externas responderam.")

    # Informativo por definição: nunca reprova o job.
    return 0


def probe(url: str) -> int | None:
    headers = {"User-Agent": "profile-readme-validator"}
    for method in ("HEAD", "GET"):
        try:
            request = urllib.request.Request(url, headers=headers, method=method)
            with urllib.request.urlopen(request, timeout=15) as response:
                return response.status
        except urllib.error.HTTPError as error:
            # Alguns serviços rejeitam HEAD mas respondem a GET, e vice-versa.
            if error.code in (403, 405, 429) and method == "HEAD":
                continue
            if error.code in (403, 429) and any(host in url for host in TOLERANT_HOSTS):
                return error.code
            if method == "GET":
                return error.code
        except (urllib.error.URLError, TimeoutError, OSError):
            if method == "GET":
                return None
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida o README do perfil.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--structure", action="store_true", help="Checagens offline de estrutura e arquivos.")
    group.add_argument("--links", action="store_true", help="Checagem de rede dos links externos.")
    args = parser.parse_args()

    content = read_readme()

    if args.structure:
        return check_structure(content)
    return check_links(content)


if __name__ == "__main__":
    raise SystemExit(main())
