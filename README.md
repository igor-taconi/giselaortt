# Gisela Ortt
Projeto de um site para a venda de desenhos e publicações de um blog da Gisela Ortt   
<a href="https://www.instagram.com/waternlights/">
  <img alt="Instagram" src="https://img.shields.io/badge/-Watern Lights-%23B7178C.svg?&logo=Instagram&logoColor=white"/>
</a>   

<a href="https://drive.google.com/drive/u/0/folders/1D8wFGOGt5BMG6-57hG2jsTmZavpsbuxN">
  <img alt="GoogleDrive" src="https://img.shields.io/badge/-Portifólio-%2331A8FF.svg?&logo=GoogleDrive&logoColor=white"/>
</a>     
<br>

## Pré-requisitos
Para você rodar o projeto é necessário tem instalado em sua máquina o `Python3.6.+`.

## Como rodar esse projeto
- ### Clone esse repositório.
```bash
git clone https://github.com/igor-taconi/giselaortt.git <nome_da_pasta>
```

- ### Crie um virtualenv com Python 3.
```bash
cd <nome_da_pasta>
python -m venv .venv
```

- ### Ative o virtualenv.
```bash
source .venv/bin/activate
```

- ### Instale as dependências.
```bash
pip install -U pip
pip install -r requirements.txt
```

- ### Como rodar esse projeto
 - Se estiver usando Linux ou Mac
```bash
export FLASK_APP=main.py
export FLASK_ENV=Development
```
 - Se estiver usando Windows
```bash
set FLASK_APP=main.py
set FLASK_ENV=Development
```

  ```
  python main.py
  ```
- Entre no seu navegador acessando a porta padrão
```bash
http://127.0.0.1:5000/
```

## Todo
- Implementar banco de dados para o cadastro dos usuários, cadastro dos produtos e para os posts do blog.
- Implementar testes.
- Melhorar o design do site.
 - interface do usuário (UI).
 - experiência do usuário (UX).

## Contribuindo
Sinta-se à vontade para enviar pull requests ou criar uma issue para sujestões ou discuções sobre escolhas no projeto, estrutura ou feramentas.


## Licença

O código fonte desse projeto esta sob a
licença [GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0).
