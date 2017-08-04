# Desafio Pyramid

Desenvolver projeto contento aplicação web utilizando framework [Pyramid](https://docs.pylonsproject.org/projects/pyramid/en/latest/)


Desafio nível 1:
---
Utilizaremos nesse desafio uma API RESTful com os seguintes recursos:

**/quotes** que retorna json no formato:
```json
{
  "quotes": [
    "quote 1.",
    "quote 2."
  ]
}
```

**/quotes/<quote_number>** que retorna json no formato:
```json
{
  "quote": "Aqui está o quose numero quote_number."
}
```

Exemplo:
GET /quotes/2
```json
{
  "quote": "quote 2."
}
```

Essa API está disponível em: https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes

1 - Criar pacote python no projeto para realizar consultas a API contendo as seguintes funções:
 - get_quotes() -> consulta API e retorna dicionário python contendo os quotes
 - get_quote(quote_number) -> Consulta API e retorna o quote correspondente

2 - A aplicação deve contar 4 rotas sendo elas:
- / -> Apresenta página HTML simples contendo título "Desafio Web 1.0"
- /quotes -> Apresenta página contendo as frases em bullet points todos os quotes retornados pela API.
- /quotes/<quote_number> -> Apresentar página contendo o quote número <quotes_number> retornado pela API.
- /quotes/random -> Apresentar página contento um quote randomico.

Desafio nível 2:
---

Utilizando o mecanismo de sessão do framework criar um identificador único para todos os acessos a aplicação originadas de um mesmo browser.

Desafio nível 3:
---

Utilizando SQLAlchemy + sqlite criar modelo/modelos para registrar:
- Sessão de consultas a aplicação.
- Data, hora e página acessada dentro de uma sessão.

Desafio nível 4:
---
Criar endpoints RESTful para visualização das sessões/consultas.

Rotas Implementadas
===

Hello:
- Hello World:
    - /

Quotes:
- Listar todas:
    - /quotes/
- Listar Específica:
    - /quotes/{id}
- Listar Randômica:
    - /quotes/random/

Logs:
- Listar todos:
    - /logs/list
- Listar Específico:
    - /logs/list/{id}