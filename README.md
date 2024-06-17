# PY-INVESTIMENTOS [EM DESENVOLVIMENTO]
Projeto em Django para fazer gestão de investimentos.

## COMO USAR

### Dependencias
- Python ~3.12

### Instalação
1. Criar o virtualenv:
```shell
python -m venv .venv
```

2. Acessar o virtualenv:
```shell
.venv\Scripts\Activate.ps1
```
> No Windows

```shell
source .venv/bin/activate
```
> No Linux

3. Instalar o `poetry`:
```shell
pip install poetry
```

4. Instalar as dependencias:
```shell
poetry install
```

5. Criar banco de dados
```shell
python manage.py migrate
```

### Iniciar servidor
```shell
python manage.py runserver
```
> Com o `virtualenv` ativo.

### Criar usuario admin
```shell
python manage.py createsuperuser
```
> Com o `virtualenv` ativo.
