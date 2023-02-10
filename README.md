# Web Crawling - Python

O projeto tem como principal objetivo fazer consultas em notícias sobre tecnologia.</br>
As notícias são obtidas através da raspagem de dados no [Blog da Trybe](https://blog.betrybe.com/).

Essas notícias são salvas no banco de dados chamado `tech_news`, utilizando o MongoDB.


## 📟 Executando o Projeto


Para executar o projeto, você precisará ter rodando o banco de dados MongoDB.


</br>

<details>
    <summary><strong>MongoDB via Docker 🐳</strong></summary><br />

No terminal, rode o comando:
```
docker-compose up -d mongodb
```
Para mais detalhes acerca do mongo com o docker, olhe o arquivo `docker-compose.yml`.</br>

</details>

</br>

Caso queira instalar e rodar o servidor MongoDB nativo na máquina, siga as instruções no tutorial oficial:
- Ubuntu: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
- MacOS: https://docs.mongodb.com/guides/server/install/


Lembre-se de que o mongoDB utilizará por padrão a porta 27017. Se já houver outro serviço utilizando esta porta, considere desativá-lo.


</br>

<details>
    <summary><strong>💻 Ambiente Virtual</strong></summary><br />

O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.</br>

Criar o ambiente virtual
```
$ python3 -m venv .venv
```

Ativar o ambiente virtual
```
$ source .venv/bin/activate
```

Instalar as dependências no ambiente virtual
```
$ python3 -m pip install -r dev-requirements.txt
```
Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
Quando precisar desativar o ambiente virtual, execute o comando "deactivate".

O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto.

</details>


</br>

## Habilidades desenvolvidas:

Utilizar o terminal interativo do Python;</br>
Escrever meus próprios módulos e importá-los em outros códigos;</br>
Aplicar técnicas de raspagem de dados;</br>
Extrair dados de conteúdo HTML;</br>
Armazenar os dados obtidos em um banco de dados;</br>


---


</br>

Projeto desenvolvido por [Thais R Kotovicz](https://www.linkedin.com/in/thaiskotovicz/).
</br>
