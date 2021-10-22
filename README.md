# HARBOR MANAGEMENT

<<<<<<< HEAD


## Getting started
=======
![diagram_er](./HM.png)
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6

## Descrição

</br>

Back-end de um sistema que facilita a gestão da logística portuária, integrando o comprador ao gestor do porto.

O HM Plus é um sistema que permitirá
analisar todas as viagens realizadas, os
containers transportados, os navios
utilizados, bem como as datas de chegada
e de saída do porto.

</br>

***

<<<<<<< HEAD
# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!).  Thank you to [makeareadme.com](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.
=======
## Tecnologias:

- Linguagem:
  - Python 3
- Framework:
  - Flask
- Banco de dados e migração:
  - PostgreSQL
  - Flask-Migrate
- ORM:
  - Flask-SQLAlchemy
- Design pattens:
  - Blueprints
  - e design pattern Flask Factory.
- Autenticação:
  - JWT
- Deploy no Heroku
- entre outras.

<br>

### BASE URL - HARBOR MANAGEMENT

- https://harbor-management.herokuapp.com/

</br>

## Diagrama ER

</br>

![diagram_er](./diagram_ER.png)

</br>
</br></br>

## Instalação

</br>

1. Crie e ative o venv (ambiente virtual);

   ```
   $ python -m venv venv
   ```

2. Instale as dependências do projeto;

   ```
   $ pip install -r requirements.txt
   ```

3. Crie um banco de dados postgreSQL

</br>

4.  Crie e configure o .env com base no arquivo .env.example, em seguida substitua com as informações do seu banco de dados

    ```
    SQLALCHEMY_DATABASE_URI=postgresql://seuUsuário:suaSenha@localhost:5432/seuBanco
    ```

    </br>
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6

5.  Atualize o banco de dados

    ```
    $ flask db migrate
    $ flask db upgrade
    ```

<<<<<<< HEAD
## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

## Endpoints User (tabela usuário)
POST /harbor_manager/users - cria um usuário.
=======
</br>

- **Rode, e teste as rotas**

  ```
  $ gunicorn "app:create_app()"
  ```

<br><br>

---

<br>

## Endpoints User (Tabela "users")

### POST `/harbor_manager/users`
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6

> Rota responsável pelo cadastros de usuários.

GET /harbor_manager/users - lista o próprio dado do usuário. - **precisa de autorização** 

PATCH /harbor_manager/users - atualiza os próprios dados. - **precisa de autorização** 

DELETE /harbor_manager/users - se deleta do banco de dados. - **precisa de autorização**
                      
## Endpoints Marine Company (tabela empresa marítima)
POST /harbor_manager/marine_company - cria empresas marítimas. - **precisa de autorização**

## Endpoints Container (Tabela 'containers')

POST /harbor_manager/container - cria containers. - **precisa de autorização**

<<<<<<< HEAD
GET /harbor_manager/container/<int:codigo_rastreio> - lista um container específico. - **precisa de autorização**
=======
## Endpoints Shipping Company (Tabela "shipping_company")
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6

-------
GET /harbor_manager/marine_company/<string:fantasy_name of the marine_company>/containers - lista todos os containers da companhia. - **precisa de autorização** 

GET /harbor_manager/marine_company/<string:fantasy_name of the marine_company>/ships - lista todos os navios da companhia. - **precisa de autorização** 

## Endpoints Ship (tabela navio)
POST /harbor_manager/ship - cria navios. - **precisa de autorização**     

- **Rota protegida**
- is_harbor: false
- Corpo requisição:

<<<<<<< HEAD
PATCH /harbor_manager/ship/<string:name of the ship> - altera dados do navio. - **precisa de autorização**     
=======
```json
{
  "trading_name": "H2H"
}
```

- Corpo da resposta:

```json
{
  "msg": "Shipping Company created!"
}
```
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6

DELETE /harbor_manager/ship/<string:name of the ship> - deleta o navio. - **precisa de autorização**  

-----
GET /harbor_manager/ship/<string:name of the ship>/travels - lista todos as viagens que o navio fez. - **precisa de autorização**

## Endpoints Container (tabela container)
POST /harbor_manager/container - cria containers. - **precisa de autorização**

- Status: 400 BAD REQUEST

<br>

### GET `/harbor_manager/container/<string:tracking_code>`

<<<<<<< HEAD
> Retorna informarções do Ship
=======
> Retorna dados de uma Shipping Company
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6

- **Rota protegida**

- Corpo requisição:

- Exemplo de requisição

      GET /harbor_manager/ship/Navio N

  - Corpo da requisição:

    ```json
    {
      "company": "MSC"
    }
    ```

  - Corpo da resposta:

<<<<<<< HEAD
    ```json
    {
      "name": "Navio N",
      "draught": 20,
      "size": 30,
      "nationality": "Brasil"
    }
    ```

    - Status: 200 OK

  - Caso Ship não exista:
    ```json
    {
      "msg": "Ship not found."
    }
    ```
    - Status: 404 NOT FOUND
=======
- Caso transportadora não exista:
  ```json
  {
    "Error": "Company not found!"
  }
  ```
  - Status: 404 NOT FOUND
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6

<br>

### PATCH `/harbor_manager/ship/<string:name_ship>`

> Atualiza informações de um ship.

- Rota protegida
- Exemplo de requisição

      /harbor_manager/ship/Navio N

  - Corpo da requisição:

  ```json
  {
    "nationality": "Alemanha-3",
    "company": "MSC"
  }
  ```

  - Corpo da resposta:

  ```json
  {
    "name": "Navio N",
    "draught": 20,
    "size": 30,
    "nationality": "Alemanha-3"
  }
  ```

  - Status: 200 OK

  - Caso ship não exista:

  ```json
  {
    "msg": "Ship not found."
  }
  ```

  - Status: 404 NOT FOUND

<br>

### DELETE `/harbor_manager/ship/<string:name_ship>`

> Deleta shipping company.

- Rota protegida
- Exemplo de requisição

        /harbor_manager/ship/Navio N

  - Precisa informar Shipping Company:

  ```json
<<<<<<< HEAD
  {
    "company": "MSC"
  }
=======
  [
    {
      "tracking_code": "n7O07",
      "teu": 1,
      "type": "dry box"
    },
    {
      "tracking_code": "75xT5",
      "teu": 1,
      "type": "dry box"
    },
      ...
  ]
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6
  ```

  - Não retorna corpo

  - Status: 200 OK

<br>

<<<<<<< HEAD
--------
GET /harbor_manager/container/<int:codigo_rastreio>/travel - lista as viagens de um container
=======
### GET `/harbor_manager/shipping_company/<string:trading_name>/ships`

> Retorna lista com todos os ships da Shipping Company.

- **Rota protegida**

- Corpo requisição:

- Exemplo de requisição

      GET /harbor_manager/shipping_company/MSC/ships

- Corpo da resposta:

  ```json
  [
    {
      "name": "Navio_N",
      "draught": 20,
      "size": 30,
      "nationality": "Brasil"
    }
  ]
  ```

- Status: 200 OK

- Caso transportadora não exista:
  ```json
  {
    "Error": "Company not found!"
  }
  ```
  - Status: 404 NOT FOUND
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6

GET /harbor_manager/container/<int:codigo_rastreio>/marine_terminal - lista os pátios nos quais o container esteve

## Endpoints Travel (tabela viagem)
POST /harbor_manager/travel - cria uma viagem. - **precisa de autorização**

GET /harbor_manager/travel/<int:codigo> - lista uma viagem específico. - **precisa de autorização**

PATCH /harbor_manager/travel/<int:codigo> - atualiza uma viagem específico. - **precisa de autorização**

<<<<<<< HEAD
DELETE /harbor_manager/travel/<int:codigo> - deleta uma viagem específico. - **precisa de autorização**
=======
## Endpoints Ship (Tabela "ships")
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6

------
GET /harbor_manager/travel/<int:codigo>/containers - lista todos os containers da viagem. . - **precisa de autorização**

## Endpoints harbor (tabela porto)
POST /harbor_manager/harbor - cria um porto. - **precisa de autorização**

- Status: 201 CREATED

GET /harbor_manager/harbor/<int:nome> - lista alguns dados de um específico.
- nome,
- pais,
- cidade

## GET `/harbor_manager/harbor/<str:nome>`

<<<<<<< HEAD
> Lista um porto específico.
=======
```json
{
  "name": "Navio_N",
  "draught": 20,
  "size": 30,
  "nationality": "Brasil",
  "company": "MSC"
}
```
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6

------
GET /harbor_manager/harbor/<int:nome>/containers - lista todos os containers que estão no porto. - **precisa de autorização**

```json
{
<<<<<<< HEAD
  "container": "452KGR",
  "entry_code": "01/10/2021",
  "exit_code": "10/10/2021"
=======
  "name": "Navio_N",
  "draught": 20,
  "size": 30,
  "nationality": "Brasil"
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6
}
```

- Status: 201 CREATED
- **\*_availability_** do porto é atualizada automaticamente e salva no banco dados.
- **\*_last_update_** do container é atualizada automaticamente e salva no banco dados.

GET /harbor_manager/harbor/<int:nome>/ships/history - histórico dos navios que passaram pelo porto. - **precisa de autorização**


<<<<<<< HEAD


=======
- Status: 409 CONFLICT

- Caso o usuário não seja do tipo **_is_harbor: false_**:

```json
{
  "Error": "This user cannot create a ship"
}
```

- Status: 400 BAD REQUEST

<br>

### GET `/harbor_manager/shipping_company/ship/<string:name_ship>`

> Retorna informarções do Ship

- **Rota protegida**

- Corpo requisição:

  - Exemplo de requisição

        GET /harbor_manager/ship/Navio_N

  - Corpo da resposta:

    ```json
    {
      "name": "Navio_N",
      "draught": 20,
      "size": 30,
      "nationality": "Brasil"
    }
    ```

    - Status: 200 OK

  - Caso Ship não exista:
    ```json
    {
      "msg": "Ship not found."
    }
    ```
    - Status: 404 NOT FOUND

<br>

### PATCH `/harbor_manager/ship/<string:name_ship>`

> Atualiza informações de um ship.

- Rota protegida
- Exemplo de requisição

      /harbor_manager/ship/Navio N

  - Corpo da requisição:

  ```json
  {
    "nationality": "Alemanha-3"
  }
  ```

  - Corpo da resposta:

  ```json
  {
    "name": "Navio_N",
    "draught": 20,
    "size": 30,
    "nationality": "Alemanha-3"
  }
  ```

  - Status: 200 OK

  - Caso ship não exista:

  ```json
  {
    "msg": "Ship not found."
  }
  ```

  - Status: 404 NOT FOUND

<br>

### DELETE `/harbor_manager/ship/<string:name_ship>`

> Deleta um Ship.

- Rota protegida
- Exemplo de requisição

        /harbor_manager/ship/Navio_N

- Não retorna corpo, basta ter autenticação.

- Status: 204 NO CONTENT

<br>

**_Outras consultas relacionadas a Ship:_**

### GET `/harbor_manager/ship/<string:name_ship>/travels`

> Retorna lista com todos Travel que o Ship fez.

- **Rota protegida**

- Corpo requisição:

- Exemplo de requisição

      GET /harbor_manager/ship/Navio_N/travels

- Corpo da resposta:

  ```json
  [
    {
      "travel_code": "12iY3z",
      "destination": "Santos",
      "id_ship": 3
    }
  ]
  ```

- Status: 200 OK

- Caso não tenha Travel cadastrado:
  ```json
  {
    "msg": "No trip recorded."
  }
  ```
  - Status: 404 NOT FOUND

<br>

<br>

---

<br>

## Endpoints Container (Tabela 'containers')

### POST `/harbor_manager/container`

> Rota responsável pelo cadastro de Container

> Somente para usuários "is_harbor: false".

- **Rota protegida**
- is_harbor: false
- Corpo requisição:

```json
{
  "teu": 1,
  "company": "MSC"
}
```

- Corpo da resposta:

```json
{
  "tracking_code": "7iE70",
  "teu": 1,
  "type": "dry box"
}
```

- Status: 201 CREATED

- Caso o usuário não seja do tipo **_is_harbor: false_**:

```json
{
  "Error": "This user cannot create a ship"
}
```

- Status: 400 BAD REQUEST

<br>

### GET `/harbor_manager/container/`

> Retorna lista com containers de uma compania do usuario

- **Rota protegida**

- Exemplo de requisição

      /harbor_manager/container/7iE70

- Corpo requisição:

  ```json
  {
    "company": "MSC"
  }
  ```

- Corpo da resposta:

  ```json
  [
    {
      "tracking_code": "n7O07",
      "teu": 1,
      "type": "dry box"
    },
    {
      "tracking_code": "75xT5",
      "teu": 1,
      "type": "dry box"
    },

    ...

  ]
  ```

- Status: 200 OK

- Caso company informada não exista:
  ```json
  {
    "msg": "Company not found."
  }
  ```
- Status: 404 NOT FOUND

<br>

### GET `/harbor_manager/container/<string:tracking_code>`

> Retorna informarções de um Container

- **Rota protegida**

- Corpo requisição:

- Exemplo de requisição

      /harbor_manager/container/7iE70

- Corpo da resposta:

  ```json
  {
    "name": "Navio N",
    "draught": 20,
    "size": 30,
    "nationality": "Brasil"
  }
  ```

- Status: 200 OK

- Caso Ship não exista:
  ```json
  {
    "msg": "Container not found."
  }
  ```
- Status: 404 NOT FOUND

<br>

### PATCH `/harbor_manager/container/<string:tracking_code>`

> Atualiza informações de um container.

- Rota protegida
- Exemplo de requisição

      /harbor_manager/container/808Eh

  - Corpo da requisição:

  ```json
  {
    "teu": 2
  }
  ```

  - Corpo da resposta:

  ```json
  {
    "tracking_code": "808Eh",
    "teu": 2,
    "type": "dry box"
  }
  ```

  - Status: 200 OK

  - Caso Container não exista:

  ```json
  {
    "msg": "Container not found."
  }
  ```

  - Status: 404 NOT FOUND

<br>

### DELETE `/harbor_manager/container/<string:tracking_code>`

> Deleta shipping company.

- Rota protegida
- Exemplo de requisição

        /harbor_manager/container/D78x9

  - Não retorna corpo

  - Status: 204 NO CONTENT

<br>
<br>

---

<br>

## Endpoints Travel (Tabela travel)

### POST `/harbor_manager/travel`

> Rota responsável pelo cadastros de viagens.

- **Rota protegida**

- Corpo requisição:

```json
{
  "destination": "Santos",
  "name_ship": "Navio_N",
  "company": "MSC"
}
```

- Corpo da resposta:

```json
{
  "travel_code": "12iY3z",
  "destination": "Santos",
  "id_ship": 3
}
```

- Status: 201 CREATED

- **\*_travel_code_** é gerado automaticamente e salvo no banco dados, foi usado a biblioteca built-in secrets.\*

<br>

### GET `/harbor_manager/travel/<string:travel_code>`

> Retorna uma viagem específica

- Rota protegida
- Exemplo de requisição

        /harbor_manager/travel/i251LR

  - Corpo da resposta:

  ```json
  {
    "travel_code": "i251LR",
    "destination": "Santos",
    "id_ship": 1
  }
  ```

<br>

### PATCH `/harbor_manager/travel/<string:travel_code>`

> Atualiza uma viagem específico.

- Rota protegida
- Exemplo de requisição

        /harbor_manager/travel/i251LR

  - Corpo da requisição:

  ```json
  {
    "destination": "Paranaguá",
    "id_ship": 2
  }
  ```

  - Corpo da resposta:

  ```json
  {
    "travel_code": "i251LR",
    "destination": "Paranaguá",
    "id_ship": 2
  }
  ```

  - Status: 200 OK

<br>

### DELETE `/harbor_manager/travel/<string:travel_code>`

> Deleta uma viagem específico..

- Rota protegida
- Exemplo de requisição

        /harbor_manager/travel/i251LR

  - Não retornar corpo

  - Status: 204 NO CONTENT

<br>

**_Outras consultas relacionadas a Travel:_**

### GET `/harbor_manager/travel/<string:travel_code>/containers`

> Lista todos os Containers de uma Travel.

- Rota protegida

- Exemplo de requisição

        /harbor_manager/travel/12iY3z/containers

  - Corpo da resposta:

  ```json
  [
    {
      "tracking_code": "n7O07",
      "teu": 1,
      "type": "dry box"
    },
    {
      "tracking_code": "808Eh",
      "teu": 1,
      "type": "dry box"
    },
    ...
  ]
  ```

  - Status: 200 OK

<br>

### POST `/harbor_manager/travel/<string:travel_code>/add`

> Cadastra Containers em uma Travel

- Rota protegida
- Exemplo de requisição

        /harbor_manager/travel/12iY3z/add

  ```json
  {
    "tracking_code": "q50J3"
  }
  ```

  - Corpo da resposta:

  ```json
  {
    "tracking_code": "q50J3",
    "teu": 2,
    "type": "dry box"
  }
  ```

  - Status: 201 CREATED

<br>

<br>

---

<br>

## Endpoint Harbor (tavela harbor)

### POST `/harbor_manager/harbor`

> Rota responsável pela criação de portos.

- **Rota protegida**

- Corpo requisição:

```json
{
  "name": "Roterda",
  "country": "Holanda",
  "city": "Roterda",
  "teus": 100
}
```

- Corpo da resposta:

```json
{
  "name": "Roterda",
  "country": "Holanda",
  "city": "Roterda",
  "teus": 100,
  "availability": 100
}
```

- Status: 201 CREATED

- **\*_availability_** é gerada automaticamente e salva no banco dados.

<br>

## GET `/harbor_manager/harbor/<str:nome>`

> Lista um porto específico.

- **Rota protegida**

- Requisição sem corpo.

- Corpo da resposta:

```json
{
  "name": "Roterda",
  "country": "Holanda",
  "city": "Roterda",
  "teus": 100,
  "availability": 100
}
```

- Status: 200 OK

<br>

## PATCH `/harbor_manager/harbor/<str:nome>`

> Atualiza um porto específico.

- **Rota protegida**

- Corpo requisição:

```json
{
  "country": "Alemanha",
  "city": "Munique",
  "teus": 120
}
```

- Corpo da resposta:

```json
{
  "name": "Roterda",
  "country": "Alemanha",
  "city": "Munique",
  "teus": 120,
  "availability": 120
}
```

- Status: 200 OK

- **\*_availability_** é atualizada automaticamente e salva no banco dados.

<br>

## GET `/harbor_manager/harbor/<str:tracking_code>/containers/history`

> Lista todos os containers que estiveram em um porto.

- **Rota protegida**

- Requisição sem corpo.

- Corpo da resposta:

```json
  [
    {
      "ship": "123HTR",
      "entry_code": "01/10/2021",
      "exit_code": None
    },
    {
      "ship": "245OPR",
      "entry_code": "01/10/2021",
      "exit_code": "10/10/2021"
    }
  ]
```

- Status: 200 OK

<br>

## GET `/harbor_manager/harbor/<str:tracking_code>/containers`

> Lista todos os containers que estão em um porto.

- **Rota protegida**

- Requisição sem corpo.

- Corpo da resposta:

```json
[
  {
    "ship": "123HTR",
    "entry_code": "01/10/2021"
  },
  {
    "ship": "245OPR",
    "entry_code": "01/10/2021"
  }
]
```

- Status: 200 OK

<br>

## GET `/harbor_manager/harbor/<str:nome>/ships/history`

> Lista todos os navios que estiveram em um porto.

- **Rota protegida**

- Requisição sem corpo.

- Corpo da resposta:

```json
  [
    {
      "ship": "Rei dos Mares",
      "entry_code": "01/10/2021",
      "exit_code": None
    },
    {
      "ship": "Príncipe dos Mares",
      "entry_code": "01/10/2021",
      "exit_code": "10/10/2021"
    }
  ]
```

- Status: 200 OK

<br>

## GET `/harbor_manager/harbor/<str:nome>/ships`

> Lista todos os navios que estão em um porto.

- **Rota protegida**

- Requisição sem corpo.

- Corpo da resposta:

```json
[
  {
    "ship": "Rei dos Mares",
    "entry_code": "01/10/2021"
  },
  {
    "ship": "Príncipe dos Mares",
    "entry_code": "01/10/2021"
  }
]
```

- Status: 200 OK

## POST `/harbor_manager/harbor/<str:nome>/ship`

> Informa entrada e saída de um navio em um porto.

- **Rota protegida**

- Corpo da requisição:

```json
{
  "ship": "Rei dos Mares"
}
```

- Corpo da resposta (varia se o navio está chegando ou saindo):

```json
  {
    "ship": "Rei dos Mares",
    "entry_code": "01/10/2021",
    "exit_code": None
  }
```

```json
{
  "ship": "Rei dos Mares",
  "entry_code": "01/10/2021",
  "exit_code": "10/10/2021"
}
```

- Status: 201 CREATED

<br>

## POST `/harbor_manager/harbor/<str:nome>/container`

> Informa entrada e saída de um container em um porto.

- **Rota protegida**

- Corpo da requisição:

```json
  {
    "tracking_code": "452KGR"
    "travel_code": "KGR789"
  }
```

- Corpo da resposta (varia se o vacio está chegando ou saindo):

```json
  {
    "container": "452KGR",
    "entry_code": "01/10/2021",
    "exit_code": None
  }
```

```json
{
  "container": "452KGR",
  "entry_code": "01/10/2021",
  "exit_code": "10/10/2021"
}
```

- Status: 201 CREATED
- **\*_availability_** do porto é atualizada automaticamente e salva no banco dados.
- **\*_last_update_** do container é atualizada automaticamente e salva no banco dados.

<br>

---

## Authors and acknowledgment

- _Felipe Dias - SM_

- _Matheus Humberto - Dev_

- _Marcelo Cabral Romão - Tech Lead_

- _Paulo Mello - Dev_

- _Wesley Matos - PO_

---

## Licença

Para projetos de código aberto, está autorizado.

<br>
>>>>>>> 65b82ccff00bfa2661198cd9fd23f6a5ec6fa7c6
