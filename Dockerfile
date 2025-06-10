FROM python:3.11-slim

# Install cowsay
RUN apt-get update && \
    apt-get install -y cowsay && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy files
COPY app.py .
COPY requirements.txt .

# Install Flask
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for web
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
