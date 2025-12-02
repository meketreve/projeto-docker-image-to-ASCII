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