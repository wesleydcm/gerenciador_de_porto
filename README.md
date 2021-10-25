# HARBOR MANAGEMENT
​
![diagram_er](./HM.png)
​
## Descrição
​
</br>
​
Back-end de um sistema que facilita a gestão da logística portuária, integrando o comprador ao gestor do porto.
​
O HM Plus é um sistema que permitirá
analisar todas as viagens realizadas, os
containers transportados, os navios
utilizados, bem como as datas de chegada
e de saída do porto.
​
</br>
​
---
​
## Tecnologias:
​
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
​
<br>
​
### BASE URL - HARBOR MANAGEMENT
​
- https://harbor-management.herokuapp.com/
​
</br>
​
## Diagrama ER
​
</br>
​
![diagram_er](./diagram_ER.png)
​
</br>
</br></br>
​
## Instalação
​
</br>
​
1. Crie e ative o venv (ambiente virtual);
​
   ```
   $ python -m venv venv
   ```
​
2. Instale as dependências do projeto;
​
   ```
   $ pip install -r requirements.txt
   ```
​
3. Crie um banco de dados postgreSQL
​
</br>
​
4.  Crie e configure o .env com base no arquivo .env.example, em seguida substitua com as informações do seu banco de dados
​
    ```
    SQLALCHEMY_DATABASE_URI=postgresql://seuUsuário:suaSenha@localhost:5432/seuBanco
    ```
​
    </br>
​
5.  Atualize o banco de dados
​
    ```
    $ flask db migrate
    $ flask db upgrade
    ```
​
</br>
​
- **Rode, e teste as rotas**
​
  ```
  $ gunicorn "app:create_app()"
  ```
​
<br><br>
​
---
​
<br>
​
## Endpoints User (Tabela "users")
​
### POST `/harbor_manager/users`
​
> Rota responsável pelo cadastros de usuários.
​
- Corpo requisição:
​
```json
{
  "name": "F_Porto",
  "username": "Fporto_1",
  "password": "abc1234",
  "is_harbor": true
}
```
​
- Corpo da resposta:
​
```json
{
  "name": "F_Porto",
  "username": "Fporto_1"
}
```
​
- Status: 201 CREATED
​
- **\*_is_harbor_**: essa propriedade distingue usuário do porto (true) e da companhia (false).\*
​
<br>
​
### POST `/harbor_manager/users/login`
​
> Rota responsável pelo login de usuários.
​
- Corpo requisição:
​
```json
{
  "username": "Fporto_1",
  "password": "abc1234"
}
```
​
- Corpo da resposta:
​
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNDc2NTY1MiwianRpIjoiZDE5Mzg3NzctMjQ4OC00NWNjLWJlYTYtMmJiYTBhNDdmZDdkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJuYW1lIjoiRl9Qb3J0byIsInVzZXJuYW1lIjoiRnBvcnRvXzEifSwibmJmIjoxNjM0NzY1NjUyLCJleHAiOjE2MzQ3NjY1NTJ9.3dxK4yqivcn9TYq8z-d-Jc36QPY4qW4gkcsNUep9n8g"
}
```
​
- Status: 200 OK
​
- **\*access_token**: token tipo **Bearer Token**, deverá ser informado no cabeçalho das requisições à rotas protegidas\*
​
<br>
​
### GET `/harbor_manager/users`
​
> Retorna os dados do usuário
​
- Rota protegida
- Exemplo de requisição
​
        /harbor_manager/users
​
  - Corpo da resposta:
​
  ```json
  {
    "name": "F_Porto",
    "username": "Fporto_1"
  }
  ```
​
  - Status: 200 OK
​
<br>
​
### PATCH `/harbor_manager/users`
​
> Update dados do usuário
​
- Rota protegida
​
- Corpo requisição
​
  ```json
  {
    "name": "haha",
    "password": "1234567"
  }
  ```
​
  - Corpo da resposta:
​
  ```json
  {
    "name": "haha",
    "username": "Fporto_1"
  }
  ```
​
  - Status: 200 OK
​
<br>
​
### DELETE `/harbor_manager/users`
​
> Deleta o usuário.
​
- Rota protegida
- Exemplo de requisição
​
        /harbor_manager/users
​
  - Corpo da resposta:
​
  ```json
  {
    "name": "haha",
    "username": "Fporto_1"
  }
  ```
​
  - Status: 200 OK
​
<br>
​
---
​
<br>
​
## Endpoints Shipping Company (Tabela "shipping_company")
​
### POST `/harbor_manager/shipping_company`
​
> Rota responsável pelo cadastros de Shipping Company
​
> Somente para usuários "is_harbor: false".
​
- **Rota protegida**
- is_harbor: false
- Corpo requisição:
​
```json
{
  "trading_name": "H2H"
}
```
​
- Corpo da resposta:
​
```json
{
  "msg": "Shipping Company created!"
}
```
​
- Status: 201 CREATED
​
- Caso o usuário não seja do tipo **_is_harbor: false_**:
​
```json
{
  "Error": "This user cannot create a company"
}
```
​
- Status: 400 BAD REQUEST
​
<br>
​
### GET `/harbor_manager/shipping_company/<string:trading_name>`
​
> Retorna dados de uma Shipping Company
​
- **Rota protegida**
​
- Somente proprietario
​
- Corpo requisição:
​
- Exemplo de requisição
​
      GET /shipping_company/H2H
​
- Corpo da resposta:
​
  ```json
  {
    "created_at": "Wed, 20 Oct 2021 00:00:00 GMT",
    "trading_name": "H2H"
  }
  ```
​
- Status: 200 OK
​
- Caso transportadora não exista:
  ```json
  {
    "Error": "Company not found!"
  }
  ```
  - Status: 404 NOT FOUND
​
<br>
​
### PATCH `/harbor_manager/shipping_company/<string:trading_name>`
​
> Atualiza informações de uma shipping company.
​
- Rota protegida
- Exemplo de requisição
​
        /harbor_manager/shipping_company/H2H
​
  - Corpo da requisição:
​
  ```json
  {
    "trading_name": "MSC"
  }
  ```
​
  - Corpo da resposta:
​
  ```json
  {
    "trading_name": "MSC"
  }
  ```
​
  - Status: 200 OK
​
  - Caso shipping company não exista:
​
  ```json
  {
    "Error": "Company not found!"
  }
  ```
​
  - Status: 404 NOT FOUND
​
<br>
​
### DELETE `/harbor_manager/shipping_company/<string:trading_name>`
​
> Deleta shipping company.
​
- Rota protegida
- Exemplo de requisição
​
        /harbor_manager/travel/MSC
​
  - Corpo da resposta:
​
  ```json
  {
    "trading_name": "MSC"
  }
  ```
​
  - Status: 200 OK
​
<br>
​
**_Outras consultas relacionadas a Shipping Company:_**
​
### GET `/harbor_manager/shipping_company/<string:trading_name>/containers`
​
> Retorna lista com todos os containers da Shipping Company.
​
- **Rota protegida**
​
- Corpo requisição:
​
- Exemplo de requisição
​
      GET /harbor_manager/shipping_company/MSC/containers
​
- Corpo da resposta:
​
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
​
- Status: 200 OK
​
- Caso transportadora não exista:
  ```json
  {
    "Error": "Company not found!"
  }
  ```
  - Status: 400 OK
​
<br>
​
### GET `/harbor_manager/shipping_company/<string:trading_name>/ships`
​
> Retorna lista com todos os ships da Shipping Company.
​
- **Rota protegida**
​
- Corpo requisição:
​
- Exemplo de requisição
​
      GET /harbor_manager/shipping_company/MSC/ships
​
- Corpo da resposta:
​
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
​
- Status: 200 OK
​
- Caso transportadora não exista:
  ```json
  {
    "Error": "Company not found!"
  }
  ```
  - Status: 404 NOT FOUND
​
<br>
​
<br>
​
---
​
<br>
​
## Endpoints Ship (Tabela "ships")
​
POST /harbor_manager/ship - cria navios. - **precisa de autorização**
​
### POST `/harbor_manager/ship`
​
> Rota responsável pelo cadastros de Ship
​
> Somente para usuários "is_harbor: false".
​
- **Rota protegida**
- is_harbor: false
- Corpo requisição:
​
```json
{
  "name": "Navio_N",
  "draught": 20,
  "size": 30,
  "nationality": "Brasil",
  "company": "MSC"
}
```
​
- Corpo da resposta:
​
```json
{
  "name": "Navio_N",
  "draught": 20,
  "size": 30,
  "nationality": "Brasil"
}
```
​
- Status: 201 CREATED
​
- Caso Ship já exista:
​
```json
{
  "msg": "Ship already registered."
}
```
​
- Status: 409 CONFLICT
​
- Caso o usuário não seja do tipo **_is_harbor: false_**:
​
```json
{
  "Error": "This user cannot create a ship"
}
```
​
- Status: 400 BAD REQUEST
​
<br>
​
### GET `/harbor_manager/shipping_company/ship/<string:name_ship>`
​
> Retorna informarções do Ship
​
- **Rota protegida**
​
- Corpo requisição:
​
  - Exemplo de requisição
​
        GET /harbor_manager/ship/Navio_N
​
  - Corpo da resposta:
​
    ```json
    {
      "name": "Navio_N",
      "draught": 20,
      "size": 30,
      "nationality": "Brasil"
    }
    ```
​
    - Status: 200 OK
​
  - Caso Ship não exista:
    ```json
    {
      "msg": "Ship not found."
    }
    ```
    - Status: 404 NOT FOUND
​
<br>
​
### PATCH `/harbor_manager/ship/<string:name_ship>`
​
> Atualiza informações de um ship.
​
- Rota protegida
- Exemplo de requisição
​
      /harbor_manager/ship/Navio N
​
  - Corpo da requisição:
​
  ```json
  {
    "nationality": "Alemanha-3"
  }
  ```
​
  - Corpo da resposta:
​
  ```json
  {
    "name": "Navio_N",
    "draught": 20,
    "size": 30,
    "nationality": "Alemanha-3"
  }
  ```
​
  - Status: 200 OK
​
  - Caso ship não exista:
​
  ```json
  {
    "msg": "Ship not found."
  }
  ```
​
  - Status: 404 NOT FOUND
​
<br>
​
### DELETE `/harbor_manager/ship/<string:name_ship>`
​
> Deleta um Ship.
​
- Rota protegida
- Exemplo de requisição
​
        /harbor_manager/ship/Navio_N
​
- Não retorna corpo, basta ter autenticação.
​
- Status: 204 NO CONTENT
​
<br>
​
**_Outras consultas relacionadas a Ship:_**
​
### GET `/harbor_manager/ship/<string:name_ship>/travels`
​
> Retorna lista com todos Travel que o Ship fez.
​
- **Rota protegida**
​
- Corpo requisição:
​
- Exemplo de requisição
​
      GET /harbor_manager/ship/Navio_N/travels
​
- Corpo da resposta:
​
  ```json
  [
    {
      "travel_code": "12iY3z",
      "destination": "Santos",
      "id_ship": 3
    }
  ]
  ```
​
- Status: 200 OK
​
- Caso não tenha Travel cadastrado:
  ```json
  {
    "msg": "No trip recorded."
  }
  ```
  - Status: 404 NOT FOUND
​
<br>
​
<br>
​
---
​
<br>
​
## Endpoints Container (Tabela 'containers')
​
### POST `/harbor_manager/container`
​
> Rota responsável pelo cadastro de Container
​
> Somente para usuários "is_harbor: false".
​
- **Rota protegida**
- is_harbor: false
- Corpo requisição:
​
```json
{
  "teu": 1,
  "company": "MSC"
}
```
​
- Corpo da resposta:
​
```json
{
  "tracking_code": "7iE70",
  "teu": 1,
  "type": "dry box"
}
```
R...