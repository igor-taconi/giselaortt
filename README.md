# WaternLights
Projeto de um site pessoal de venda de ilustrações e publicações de um blog da ilustradora `Gisela Ortt`   
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
  * [Todo](#todo)
  * [Contribuindo](#contribuindo)
  * [Licença](#licença)

## Pré-requisitos
Para você rodar o projeto é necessário tem instalado em sua máquina o [`Python3.6.+`](https://www.python.org/)

## Como rodar esse projeto
- #### Instale as dependências.
```sh
pip install -U pip
pip install poetry
poetry install
```

- ### Rodar o projeto
```sh
flask run
```
ou
```sh
gunicorn waternlights.wsgi:app --bind 0.0.0.0:5000 --timeout 1000 --worker-class gevent
```
ou
```sh
make run
```
- Entre no seu navegador acessando a porta padrão
```sh
http://127.0.0.1:5000/
```

## Todo
- [x] Criar admim  
- [x] Banco de dados para os usuários  
- [x] Banco de dados para os post's  
- [ ] Banco de dados para os produtos  
- [ ] Testes funcionais  
- [ ] Interface do usuário (UI)  
- [ ] Calcular frete  
- [ ] Validar dados de pagamento  
- [ ] Experiência do usuário (UX)  
- [ ] Adicionar guias para outros gerenciadores de dependências  

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
