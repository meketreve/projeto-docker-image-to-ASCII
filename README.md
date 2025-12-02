# 🖼️ Image to ASCII Art Converter (Python & Docker)

Este projeto oferece um serviço simples e leve para converter imagens em arte ASCII, tudo empacotado em contêineres Docker para fácil implantação e escalabilidade. Desenvolvido em Python com o framework Flask e a biblioteca Pillow para processamento de imagens.

## 🌟 Descrição

O objetivo principal deste projeto é fornecer uma ferramenta acessível para transformar suas imagens favoritas em arte ASCII estilizada. A aplicação web permite o upload de imagens (JPG, PNG, etc.) e as converte para representações de texto, que podem ser visualizadas diretamente no navegador ou baixadas como um arquivo de texto. Ideal para quem busca um toque nostálgico ou artístico em suas imagens digitais.

## 📐 Arquitetura

O projeto segue uma arquitetura simples de microsserviço, onde uma única aplicação Python é conteinerizada usando Docker.

```
+-------------------+       +-------------------+
|     Usuário       |       |    Web Browser    |
| (Faz Requisição)  | <---> | (Acessa o Serviço)|
+-------------------+       +-------------------+
          |                           ^
          | HTTP/S                    | HTTP/S
          v                           |
+-------------------------------------+
|        Docker Host                  |
|                                     |
|  +--------------------------------+ |
|  |       image-to-ascii-app       | |
|  |                                | |
|  | +----------------------------+ | |
|  | | Python Flask Application   | | |
|  | |  - Recebe Imagem Upload    | | |
|  | |  - Usa Pillow para Converter | |
|  | |  - Retorna ASCII Art       | | |
|  | +----------------------------+ | |
|  +--------------------------------+ |
|                                     |
+-------------------------------------+
```

## 🚀 Demonstração do Funcionamento

1.  **Acesse a Interface Web:** Após iniciar o contêiner, abra seu navegador e vá para `http://localhost:5000`.
2.  **Faça o Upload da Imagem:** Você verá um formulário simples de upload. Clique em "Escolher arquivo", selecione uma imagem (JPG, PNG, etc.) do seu computador.
3.  **Escolha a Saída (Opcional):** Marque a caixa "Baixar como .txt" se desejar que a arte ASCII seja salva em um arquivo de texto. Caso contrário, ela será exibida diretamente na página.
4.  **Converta:** Clique no botão "Converter".
5.  **Visualize/Baixe:** A arte ASCII será exibida na página ou o download do arquivo `.txt` será iniciado, dependendo da sua escolha.

**(Placeholder para GIF/ASCII ou Diagrama Visual)**
*   No momento, não é possível gerar um GIF de demonstração automática, mas você pode facilmente criar um GIF da tela após rodar a aplicação para adicionar aqui!
*   Considere usar uma imagem de exemplo e seu resultado em ASCII para mostrar a transformação.

```text
Exemplo de entrada: Uma pequena imagem de um gato.

Exemplo de saída (parte):
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```

## 🛠️ Como Instalar o Docker

Para rodar este projeto, você precisará ter o Docker instalado em sua máquina. Siga as instruções para o seu sistema operacional:

*   **Windows:** [Instalar Docker Desktop no Windows](https://docs.docker.com/desktop/install/windows-install/)
*   **Linux:** [Instalar Docker Engine no Linux](https://docs.docker.com/engine/install/)
*   **macOS:** [Instalar Docker Desktop no Mac](https://docs.docker.com/desktop/install/mac-install/)

## ▶️ Como Rodar o Projeto

Você tem duas maneiras principais de rodar este projeto conteinerizado: usando comandos `docker build` e `docker run` separadamente, ou usando `docker-compose` para orquestração.

### Opção 1: Usando `docker build` e `docker run`

Esta opção é útil para entender as etapas individuais de construção da imagem e execução do contêiner.

1.  **Navegue até o diretório do projeto:**
    ```bash
    cd /caminho/para/seu/projeto-docker
    ```
2.  **Construa a imagem Docker:**
    Este comando irá construir a imagem Docker para a aplicação, usando o `Dockerfile` localizado em `./image_to_ascii`.
    ```bash
    docker build -t image-to-ascii-app ./image_to_ascii
    ```
    *   `-t image-to-ascii-app`: Atribui a tag `image-to-ascii-app` à imagem.
    *   `./image_to_ascii`: Indica o contexto da construção (onde o Dockerfile está localizado).

3.  **Execute o contêiner Docker:**
    Após a imagem ser construída, você pode executar um contêiner a partir dela.
    ```bash
    docker run -p 5000:5000 --name ascii-converter image-to-ascii-app
    ```
    *   `-p 5000:5000`: Mapeia a porta 5000 do host para a porta 5000 do contêiner, permitindo que você acesse a aplicação.
    *   `--name ascii-converter`: Atribui um nome ao contêiner para facilitar o gerenciamento.
    *   `image-to-ascii-app`: O nome da imagem a ser usada.

4.  **Acesse a aplicação:**
    Abra seu navegador e vá para `http://localhost:5000`.

### Opção 2: Usando `docker-compose`

Esta é a forma recomendada para rodar o projeto, pois `docker-compose` gerencia a construção da imagem e a execução do contêiner com um único comando.

1.  **Navegue até o diretório raiz do projeto:**
    ```bash
    cd /caminho/para/seu/projeto-docker
    ```
2.  **Inicie o serviço com Docker Compose:**
    Este comando irá construir a imagem (se ainda não existir ou se houver mudanças) e iniciar o serviço definido no `docker-compose.yml`.
    ```bash
    docker-compose up --build
    ```
    *   `up`: Inicia os serviços definidos no `docker-compose.yml`.
    *   `--build`: Garante que a imagem seja reconstruída, caso haja atualizações no código ou no `Dockerfile`.

3.  **Acesse a aplicação:**
    Abra seu navegador e vá para `http://localhost:5000`.

4.  **Para parar o serviço:**
    Pressione `Ctrl+C` no terminal onde `docker-compose up` está rodando, ou execute em outro terminal:
    ```bash
    docker-compose down
    ```

## 📄 Explicação do `Dockerfile`

O `Dockerfile` (localizado em `./image_to_ascii/Dockerfile`) é o conjunto de instruções que o Docker usa para construir a imagem da sua aplicação.

```dockerfile
# Usar a imagem oficial do Python como base
FROM python:3.9-slim-buster

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo de requisitos e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação para o diretório de trabalho
COPY . .

# Expor a porta que a aplicação Flask usa
EXPOSE 5000

# Definir a variável de ambiente FLASK_APP
ENV FLASK_APP=app.py

# Comando para iniciar a aplicação Flask
CMD ["flask", "run", "--host", "0.0.0.0"]
```

*   `FROM python:3.9-slim-buster`: Define a imagem base. Usamos uma imagem Python leve (`slim-buster`) para reduzir o tamanho final da imagem.
*   `WORKDIR /app`: Define `/app` como o diretório de trabalho padrão para quaisquer comandos subsequentes.
*   `COPY requirements.txt .`: Copia o arquivo `requirements.txt` do diretório local para o diretório `/app` no contêiner.
*   `RUN pip install --no-cache-dir -r requirements.txt`: Instala as dependências listadas em `requirements.txt`. `--no-cache-dir` ajuda a manter a imagem menor, evitando o cache do pip.
*   `COPY . .`: Copia todo o conteúdo do diretório atual (o contexto da construção, que é `./image_to_ascii`) para o diretório `/app` no contêiner.
*   `EXPOSE 5000`: Informa ao Docker que o contêiner escutará na porta 5000 em tempo de execução. Isso é apenas uma documentação; o mapeamento real da porta é feito com `-p` no `docker run` ou no `docker-compose.yml`.
*   `ENV FLASK_APP=app.py`: Define uma variável de ambiente necessária para o Flask encontrar o arquivo da aplicação.
*   `CMD ["flask", "run", "--host", "0.0.0.0"]`: Define o comando padrão que será executado quando o contêiner for iniciado. Ele inicia o servidor de desenvolvimento do Flask, tornando-o acessível de qualquer IP (`--host 0.0.0.0`).

## 🐳 Explicação do `docker-compose.yml`

O arquivo `docker-compose.yml` (localizado na raiz do projeto) é usado para definir e rodar aplicações Docker multi-contêiner. Neste projeto, ele orquestra um único serviço.

```yaml
version: '3.8'
services:
  image-to-ascii-app:
    # Construir a imagem a partir do Dockerfile localizado em ./image_to_ascii
    build: ./image_to_ascii
    # Mapear a porta 5000 do contêiner para a porta 5000 do host
    ports:
      - "5000:5000"
    # Montar o volume para facilitar o desenvolvimento (opcional)
    # Qualquer alteração nos arquivos locais ./image_to_ascii será refletida no contêiner
    volumes:
      - ./image_to_ascii:/app
    # Reiniciar o contêiner se ele parar inesperadamente
    restart: always
```

*   `version: '3.8'`: Especifica a versão da sintaxe do Docker Compose.
*   `services:`: Define os serviços que compõem sua aplicação.
*   `image-to-ascii-app:`: É o nome do seu serviço.
    *   `build: ./image_to_ascii`: Diz ao Docker Compose para construir a imagem para este serviço usando o `Dockerfile` encontrado no diretório `./image_to_ascii`.
    *   `ports: - "5000:5000"`: Publica a porta 5000 do contêiner para a porta 5000 no host. Isso significa que você pode acessar a aplicação Flask em `http://localhost:5000` a partir do seu navegador.
    *   `volumes: - ./image_to_ascii:/app`: Cria um volume de montagem. O diretório `./image_to_ascii` do seu host é montado como `/app` dentro do contêiner. Isso é **extremamente útil para desenvolvimento**, pois qualquer alteração que você faça nos arquivos Python locais será refletida instantaneamente no contêiner (após reiniciar o servidor Flask ou com a detecção de alterações do Flask em modo debug).
    *   `restart: always`: Garante que o contêiner sempre tentará reiniciar se ele falhar ou se o Docker for reiniciado.

## 📤 Exemplo de Requisição (Upload de Imagem)

A aplicação é acessada via um navegador web. Você pode usar o formulário de upload fornecido pela própria aplicação Flask.

Para testar, basta seguir os passos da seção "Demonstração do Funcionamento" acessando `http://localhost:5000` após iniciar o serviço.

Se você quisesse fazer uma requisição via cURL (para testes de API, por exemplo), seria algo como:

```bash
curl -X POST -F "file=@/caminho/para/sua/imagem.jpg" -F "download_txt=true" http://localhost:5000/convert
```
*Substitua `/caminho/para/sua/imagem.jpg` pelo caminho real da sua imagem.*

## 🔮 Melhorias Futuras

*   **Customização de Caracteres ASCII:** Permitir que o usuário defina o conjunto de caracteres ASCII a ser usado.
*   **Ajuste de Resolução:** Opções para o usuário controlar a resolução da arte ASCII gerada (número de colunas/linhas).
*   **Suporte a Cores:** Implementar arte ASCII colorida (exigiria mais complexidade e possivelmente um terminal com suporte a 256 cores ou HTML com estilos).
*   **Otimização de Performance:** Para imagens muito grandes, otimizar o processamento.
*   **Interface do Usuário Aprimorada:** Uma interface mais moderna e responsiva (com frameworks front-end como React, Vue ou Angular).
*   **Controle de Erros Aprimorado:** Mensagens de erro mais amigáveis e tratamento de borda para uploads inválidos.
*   **Testes Automatizados:** Adicionar testes unitários e de integração para a aplicação Flask e a lógica de conversão.
*   **Persistência:** Opção de armazenar as imagens originais ou as artes ASCII geradas.
*   **Kubernetes Deployment:** Configurações para implantação em um cluster Kubernetes.

## 🤝 Créditos e Licença

**Desenvolvido por:** [Seu Nome ou Nome da Organização]

Este projeto está licenciado sob a Licença MIT. Sinta-se à vontade para usar, modificar e distribuir o código, desde que as condições da licença sejam mantidas.

---
**MIT License**

Copyright (c) [Ano] [Seu Nome ou Nome da Organização]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
