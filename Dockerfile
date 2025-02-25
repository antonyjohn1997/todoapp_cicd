# Use Python base image  
FROM python:3.9-slim

# Set working directory  
WORKDIR /app

# Copy files  
COPY app/ /app/

# Install dependencies  
RUN pip install --no-cache-dir -r requirements.txt

# Expose port  
EXPOSE 5000

# Run the app  
CMD ["python", "app.py"]



