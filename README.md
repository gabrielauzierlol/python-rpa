## Configurando ambiente virtual

No Linux:

- `apt install python3.10-venv`
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`

## Linting

- Extensão autopep8
- Adicione o seguinte trecho ao seu arquivo settings.json

```
  "[python]": {
    "editor.defaultFormatter": "ms-python.autopep8",
    "editor.formatOnSave": true
  },
```