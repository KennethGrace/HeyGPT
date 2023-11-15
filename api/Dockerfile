FROM python:3.10

# Copy all files from current directory to /app inside container
COPY . /app

# Set working directory to /app
WORKDIR /app

# Volume mount for persistent model storage
VOLUME /app/models
ENV TRANSFORMERS_CACHE=/app/models

# Volume mount for persistent cache storage
VOLUME /app/cache

# Expose application port 49488
EXPOSE 23450

# Install requirements without any cache
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Run uvicorn server
ENTRYPOINT [ "uvicorn", "heygpt:application", "--host", "0.0.0.0", "--port", "23450"]