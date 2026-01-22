# Use a lightweight python image
FROM python:3.10-slim

# Set environment variables to keep the container clean
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies needed for libraries like BeautifulSoup or PyPDF
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements and install WITHOUT saving cache files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application (the .dockerignore will skip the 10GB rag_env)
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "rag_streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]