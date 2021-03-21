# Gisela Ortt
Projeto de um site para a venda de desenhos e publicações de um blog da Gisela Ortt   
<a href="https://www.instagram.com/waternlights/">
  <img alt="Instagram" src="https://img.shields.io/badge/Watern Lights-%23E4405F.svg?&logo=Instagram&logoColor=white"/>
</a>   

<a href="https://drive.google.com/drive/u/0/folders/1D8wFGOGt5BMG6-57hG2jsTmZavpsbuxN">
  <img alt="GoogleDrive" src="https://img.shields.io/badge/-Portifólio-%2331A8FF.svg?&logo=GoogleDrive&logoColor=white"/>
</a>     
<br>

Índice
=================
  * [Pré-requisitos](#pré-requisitos)
  * [Como rodar o projeto](#como-rodar-esse-projeto)
    * [Virtualenv e dependências](#virtualenv-e-dependências)
      * [venv](#venv)
      * [poetry](#poetry)
      * [Rodar o projeto](#rodar-o-projeto)
  * [Todo](#todo)
  * [Contribuindo](#contribuindo)
  * [Licença](#licença)

## Pré-requisitos
Para você rodar o projeto é necessário tem instalado em sua máquina o [`Python3.6.+`](https://www.python.org/) e [`Poetry`](https://python-poetry.org/) se ele for a sua escolha para gerenciar as dependências, o módulo `venv` já vem instalado com o python. Em ambos os sites, do python e do poetry, há istruções para você instala-los em sua máquina.

## Como rodar esse projeto
- ### Clone esse repositório.
```bash
git clone https://github.com/igor-taconi/giselaortt.git <nome_da_pasta>
```
- ### Virtualenv e dependências
  ### Venv

  - ##### Crie um virtualenv com Python3 usando o venv.   
```bash
cd <nome_da_pasta>
python -m venv .venv
```

  - #### Ative o virtualenv.
```bash
source .venv/bin/activate
```

  - #### Instale as dependências.
```bash
pip install -U pip
pip install --require-hashes -r requirements.txt
pip install --require-hashes -r requirements_dev.txt
pip install --require-hashes -r requirements_test.txt
```

  ### Poetry
  - ##### Crie um virtualenv com Python 3.8 usando o poetry.   
```bash
cd <nome_da_pasta>
poetry env use 3.8
```

  - #### Ative o virtualenv.
```bash
poetry shell
```

  - #### Instale as dependências.
```bash
poetry install
```

- ### Rodar o projeto
```bash
flask run
```
ou
```bash
gunicorn giselaortt.wsgi:app --bind 0.0.0.0:5000 --timeout 1000 --worker-class gevent
```
ou
```bash
make run
```
- Entre no seu navegador acessando a porta padrão
```bash
http://127.0.0.1:5000/
```

## Todo
:white_check_mark: Pronto
:soon: Em progresso

| Status | Tarefa |
|--------|--------|
|:soon:| Testes de unidade |
| | Criar admim |
| | Banco de dados para os usuários |
| | Banco de dados para os post's |
| | Banco de dados para os produtos |
| | Testes funcionais |
| | Interface do usuário (UI) |
| | Calcular frete |
| | Validar dados de pagamento |
| | Experiência do usuário (UX) |
| | Adicionar guias para outros gerenciadores de dependências |

## Contribuindo
Sinta-se à vontade para enviar pull request ou criar uma issue para sujestões ou discuções sobre escolhas no projeto, estrutura ou feramentas.
#### Como contribuir
  - Crie um fork do projeto
  - Realize alguma tarefa do [Todo](#todo) ou crie novas
  - Siga esse [guia](https://gist.github.com/nailton/512e3daa717f1d6dbef1) sobre boas práticas de commit's
  - Formate o projeto com o comando `make format`
  - Rode os testes com o comando `make test`
  - Check o código com o comando `make check`
  - Envie um pull request.



## Licença

O código fonte desse projeto esta sob a
licença [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0).
