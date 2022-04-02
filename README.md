# python-poo
Assuntos estudados no projeto:

* ParadigmaPOO
* Operações CRUD
---
* Query para iniciar os estudos:
```shell
CREATE TABLE uuser(
  id serial PRIMARY KEY,
  name VARCHAR ( 50 ) NOT NULL,
  email VARCHAR ( 255 ) UNIQUE NOT NULL,
  password VARCHAR ( 50 ) NOT NULL
);
```