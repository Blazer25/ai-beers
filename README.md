# Beer AI API

Esta é uma API que utiliza dados de cervejas em arquivos JSON para retornar cervejas com características específicas.

## Como executar

1. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

2. Execute a aplicação:

   ```sh
   python src/main.py
   ```

3. Acesse a API em `http://localhost:8000`.

## Como usar

- Para treinar o modelo, faça uma requisição POST para `/treinar-modelo`.
- Para buscar cervejas por uma característica, faça uma requisição GET para `/cervejas-caracteristicas?characteristic=<característica>`.
