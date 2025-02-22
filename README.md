# Beer AI API

Esta é uma API que utiliza dados de cervejas em arquivos JSON para retornar cervejas com características específicas.

## Pré-requisitos

Certifique-se de ter o Python 3.9 instalado. Você pode verificar a versão do Python com o seguinte comando:

```sh
python --version
```

## Como executar

1.  **Crie um ambiente virtual (opcional, mas recomendado):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate.bat # No Windows
    ```

2.  **Instale as dependências:**

    ```sh
    pip install -r requirements.txt
    ```

3.  **Execute a aplicação:**

    ```sh
    python src/main.py
    ```

4.  **Acesse a API em** `http://localhost:8000`.

## Como usar

### Treinar o modelo

-   Faça uma requisição POST para `/treinar-modelo`.

    ```sh
    curl -X POST http://localhost:8000/treinar-modelo
    ```

    Isso irá treinar o modelo de análise de características de cervejas.

### Buscar cervejas por característica

-   Faça uma requisição GET para `/cervejas-caracteristicas` com os seguintes parâmetros:
    -   `caracteristica`: A característica da cerveja que você deseja buscar (ex: "amarga", "doce", "forte").
    -   `limiar` (opcional): Um valor entre 0 e 1 que representa o nível de similaridade aceitável para a característica (padrão: 0.1).
    -   `limite` (opcional): O número máximo de cervejas a serem retornadas (padrão: 10).
    -   `language` (opcional): O idioma em que os resultados (descrição das cervejas) devem ser retornados. Pode ser `eng` para inglês ou `pt-br` para português (padrão: `eng`).

    Exemplo:

    ```sh
    curl "http://localhost:8000/cervejas-caracteristicas?caracteristica=bitter&limiar=0.2&limite=5&language=eng"
    ```

    **Exemplo de resposta em inglês:**

    ```json
    [
        {
            "name": "Resting Brewer Face",
            "style": "American-Style Brown Ale",
            "description": "A traditional American Brown Ale, a sweet malt profile with hints of sweet chocolate & biscuity malt complement the addition of Cascade hops.",
            "label": "https://brewerydb-images.s3.amazonaws.com/beer/6qWuTW/upload_VWs8ru-contentAwareLarge.png",
            "abv": 5.5,
            "ibu": 31.0
        }
    ]
    ```

    **Exemplo de resposta em português:**
    
    - Respostas em pt-br tendem a demorar mais para serem retornadas, pois precisam ser traduzidas, em alguns casos, timeouts podem ocorrer!

    ```json
    [
        {
            "nome": "Resting Brewer Face",
            "estilo": "American-Style Brown Ale",
            "descricao": "Uma cerveja marrom americana tradicional, um perfil de malte doce com notas de chocolate doce e malte de biscuidade complementam a adição de lúpulos em cascata.",
            "rotulo": "https://brewerydb-images.s3.amazonaws.com/beer/6qWuTW/upload_VWs8ru-contentAwareLarge.png",
            "abv": 5.5,
            "ibu": 31.0
        }
    ]
    ```