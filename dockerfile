FROM python:3.9-slim

# Evitar perguntas interativas
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependências do sistema e o navegador Chromium
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libxss1 \
    libgbm-dev \
    libxshmfence-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependências Python
RUN pip install --no-cache-dir selenium webdriver-manager beautifulsoup4

# Copiar o script Python para dentro do container
COPY scraper.py /app/scraper.py

# Definir o diretório de trabalho
WORKDIR /app

# Rodar o script automaticamente
CMD ["python3", "scraper.py"]
