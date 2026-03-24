FROM python:3.11-slim

# 作業ディレクトリ
WORKDIR /app

# システム依存パッケージ
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Pythonパッケージ
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコピー
COPY . .

# 環境変数（.envで上書き可能）
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

CMD ["python", "src/main.py"]
