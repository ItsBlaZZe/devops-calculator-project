# Python Calculator

Pequeña calculadora (lib + CLI) con tests `pytest` y CI en GitHub Actions.

## Uso local

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python -m calculator.app
