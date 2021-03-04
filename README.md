# python-playground

Ambiente de aprendizado para [Python](https://python.org)

## Desenvolvimento

>> Considerando que está dentro do diretório do projeto

1. Renomeie o arquivo `.env.example` para `.env`

    ```bash
    mv .env.example .env
    ```

    >> Caso necessário, customize as variávis de ambiente

2. Utilize a imagem docker:

    * Executar diretamente o arquivo `src/index.py`

    ```bash
    docker-compose up py-playground
    ```

    * Utilizar o CLI interno do _service_

    ```bash
    docker-compose run --rm --service-ports py-playground bash
    ```
