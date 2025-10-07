FROM python:3.12-slim

WORKDIR /app

# Opcional: que Python no genere .pyc y logs bufferizados
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY src/ src/
COPY README.md .

# Ejecutar desde /app/src para que 'calculator' esté en sys.path
WORKDIR /app/src
CMD ["python", "-m", "calculator.app"]
