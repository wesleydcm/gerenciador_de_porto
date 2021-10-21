# capstone_q3_gerenciador_de_porto

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/MarceloRomao/capstone_q3_gerenciador_de_porto.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://docs.gitlab.com/ee/user/project/integrations/)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Automatically merge when pipeline succeeds](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://docs.gitlab.com/ee/user/clusters/agent/)

---

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://gitlab.com/-/experiment/new_project_readme_content:40bab2ae25ade5d452676e630b3ba46e?https://www.makeareadme.com/) for this template.

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

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment

Show your appreciation to those who have contributed to the project.

## License

For open source projects, say how it is licensed.

## Project status

If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

## Endpoints User (tabela usuário)

### POST `/harbor_manager/users`

> Rota responsável pelo cadastros de usuários.

- Corpo requisição:

```json
{
  "name": "F_Porto",
  "username": "Fporto_1",
  "password": "abc1234",
  "is_harbor": true
}
```

- Corpo da resposta:

```json
{
  "name": "F_Porto",
  "username": "Fporto_1"
}
```

- Status: 201 CREATED

- **\*_is_harbor_**: essa propriedade distingue usuário do porto (true) e da companhia (false).\*

<br>

### POST `/harbor_manager/users/login`

> Rota responsável pelo login de usuários.

- Corpo requisição:

```json
{
  "username": "Fporto_1",
  "password": "abc1234"
}
```

- Corpo da resposta:

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzNDc2NTY1MiwianRpIjoiZDE5Mzg3NzctMjQ4OC00NWNjLWJlYTYtMmJiYTBhNDdmZDdkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJuYW1lIjoiRl9Qb3J0byIsInVzZXJuYW1lIjoiRnBvcnRvXzEifSwibmJmIjoxNjM0NzY1NjUyLCJleHAiOjE2MzQ3NjY1NTJ9.3dxK4yqivcn9TYq8z-d-Jc36QPY4qW4gkcsNUep9n8g"
}
```

- Status: 200 OK

- **\*access_token**: token tipo **Bearer Token**, deverá ser informado no cabeçalho das requisições à rotas protegidas\*

<br>

### GET `/harbor_manager/users`

> Retorna os dados do usuário

- Rota protegida
- Exemplo de requisição

        /harbor_manager/users

  - Corpo da resposta:

  ```json
  {
    "name": "F_Porto",
    "username": "Fporto_1"
  }
  ```

  - Status: 200 OK

<br>

### PATCH `/harbor_manager/users`

> Update dados do usuário

- Rota protegida

- Corpo requisição

  ```json
  {
    "name": "haha",
    "password": "1234567"
  }
  ```

  - Corpo da resposta:

  ```json
  {
    "name": "haha",
    "username": "Fporto_1"
  }
  ```

  - Status: 200 OK

<br>

### DELETE `/harbor_manager/users`

> Deleta o usuário.

- Rota protegida
- Exemplo de requisição

        /harbor_manager/users

  - Corpo da resposta:

  ```json
  {
    "name": "haha",
    "username": "Fporto_1"
  }
  ```

  - Status: 200 OK

<br>

---

<br>

## Endpoints Shipping Company (Tabela ShippingCompany)

### POST `/harbor_manager/shipping_company`

> Rota responsável pelo cadastros de Shipping Company

> Somente para usuários "is_harbor: false".

- **Rota protegida**
- is_harbor: false
- Corpo requisição:

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

- Status: 201 CREATED

- Caso o usuário não seja do tipo **_is_harbor: false_**:

```json
{
  "Error": "This user cannot create a company"
}
```

- Status: 400 BAD REQUEST

<br>

### GET `/harbor_manager/shipping_company/<string:trading_name>`

> Retorna dados de uma Shipping Company

- **Rota protegida**

- Somente proprietario

- Corpo requisição:

- Exemplo de requisição

      GET /shipping_company/H2H

- Corpo da resposta:

  ```json
  {
    "created_at": "Wed, 20 Oct 2021 00:00:00 GMT",
    "trading_name": "H2H"
  }
  ```

- Status: 200 OK

- Caso transportadora não exista:
  ```json
  {
    "Error": "Company not found!"
  }
  ```
  - Status: 400 OK

<br>

### PATCH `/harbor_manager/shipping_company/<string:trading_name>`

> Atualiza informações de uma shipping company.

- Rota protegida
- Exemplo de requisição

        /harbor_manager/shipping_company/H2H

  - Corpo da requisição:

  ```json
  {
    "trading_name": "MSC"
  }
  ```

  - Corpo da resposta:

  ```json
  {
    "trading_name": "MSC"
  }
  ```

  - Status: 200 OK

  - Caso shipping company não exista:

  ```json
  {
    "Error": "Company not found!"
  }
  ```

  - Status: 404 NOT FOUND

<br>

### DELETE `/harbor_manager/shipping_company/<string:trading_name>`

> Deleta shipping company.

- Rota protegida
- Exemplo de requisição

        /harbor_manager/travel/MSC

  - Corpo da resposta:

  ```json
  {
    "trading_name": "MSC"
  }
  ```

  - Status: 200 OK

<br>

**_Outras consultas relacionadas a Shipping Company:_**

### GET `/harbor_manager/shipping_company/<string:trading_name>/containers`

> Retorna lista com todos os containers da Shipping Company.

- **Rota protegida**

- Corpo requisição:

- Exemplo de requisição

      GET /harbor_manager/shipping_company/MSC/containers

- Corpo da resposta:

  ```json
  {
    "Alterar": ""
  }
  ```

- Status: 200 OK

- Caso transportadora não exista:
  ```json
  {
    "Error": "Company not found!"
  }
  ```
  - Status: 400 OK

<br>

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
      "name": "Navio N",
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
  - Status: 400 OK

<br>

<br>

---

<br>

## Endpoints Ship (tabela navio)

POST /harbor_manager/ship - cria navios. - **precisa de autorização**

### POST `/harbor_manager/ship`

> Rota responsável pelo cadastros de Ship

> Somente para usuários "is_harbor: false".

- **Rota protegida**
- is_harbor: false
- Corpo requisição:

```json
{
  "name": "Navio N",
  "draught": 20,
  "size": 30,
  "nationality": "Brasil",
  "company": "MSC"
}
```

- Corpo da resposta:

```json
{
  "name": "Navio N",
  "draught": 20,
  "size": 30,
  "nationality": "Brasil"
}
```

- Status: 201 CREATED

- Caso Ship já exista:

```json
{
  "msg": "Ship already registered."
}
```

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

      GET /harbor_manager/ship/Navio N

  - Corpo da requisição:

    ```json
    {
      "company": "MSC"
    }
    ```

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
  {
    "company": "MSC"
  }
  ```

  - Não retorna corpo

  - Status: 204 NO CONTENT

<br>

**_Outras consultas relacionadas a Shipping Company:_**

### GET `/harbor_manager/ship/<string:name_ship>/travels`

> Retorna lista com todos Travel que o Ship fez.

- **Rota protegida**

- Corpo requisição:

- Exemplo de requisição

      GET /harbor_manager/ship/Navio N/travels

  ```json
  {
    "company": "MSC"
  }
  ```

- Corpo da resposta:

  ```json
  {
    "Alterar": ""
  }
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

POST /harbor_manager/container - cria containers. - **precisa de autorização**

GET /harbor_manager/container/<int:codigo_rastreio> - lista um container específico. - **precisa de autorização**

PATCH /harbor_manager/container/<int:codigo_rastreio> - atualiza um container específico. - **precisa de autorização**

DELETE /harbor_manager/container/<int:codigo_rastreio> - deleta um container específico. - **precisa de autorização**

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

### GET `/harbor_manager/container/<string:tracking_code>`

> Retorna informarções do Ship

- **Rota protegida**

- Corpo requisição:

- Exemplo de requisição

      GET /harbor_manager/container/7iE70

  - Corpo da requisição:

    ```json
    {
      "tracking_code": "7iE70",
      "teu": 1,
      "type": "dry box"
    }
    ```

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
  {
    "company": "MSC"
  }
  ```

  - Não retorna corpo

  - Status: 200 OK

<br>

---

GET /harbor_manager/container/<int:codigo_rastreio>/travel - lista as viagens de um container

GET /harbor_manager/container/<int:codigo_rastreio>/marine_terminal - lista os pátios nos quais o container esteve

## Endpoints Travel (tabela Travel)

### POST `/harbor_manager/travel`

> Rota responsável pelo cadastros de viagens.

- **Rota protegida**

- Corpo requisição:

```json
{
  "destination": "Santos",
  "id_ship": "1"
}
```

- Corpo da resposta:

```json
{
  "travel_code": "0gF28O",
  "destination": "Santos",
  "id_ship": "1"
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

**_Outras consultas relacionadas a Travel:_**

### GET `/harbor_manager/travel/<string:travel_code>/containers`

> Lista todos os containers da viagem.

- Rota protegida

<br>
<br>

---

## POST `/harbor_manager/harbor`

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
