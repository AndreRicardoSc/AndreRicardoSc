# Contribuições — @AndreRicardoSc

Gráfico de contribuições dos últimos 12 meses, gerado automaticamente por
[`scripts/generate_contributions.py`](../scripts/generate_contributions.py) e
publicado pelo workflow
[`update-contributions.yml`](../.github/workflows/update-contributions.yml).

O arquivo `contributions.svg` é versionado neste repositório para que o README
funcione mesmo se um serviço externo de imagens estiver indisponível.

Para gerar localmente:

```bash
GITHUB_USERNAME=AndreRicardoSc GITHUB_TOKEN=<seu-token> python scripts/generate_contributions.py
```

O token precisa apenas do escopo de leitura de dados públicos do usuário.
O script não usa dependências externas além da biblioteca padrão do Python 3.10+.
