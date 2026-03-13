# 1. Base Image: We start with a tiny Linux OS that already has Python 3.12 installed.
FROM python:3.12-slim

# 2. Work Directory: We create a folder named /code inside the container and move into it.
WORKDIR /code

# 3. Cache Dependencies: We copy ONLY the requirements.txt file first.
COPY requirements.txt .

# 4. Install Dependencies: We run pip install inside the container. 
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Source Code: Now we copy your actual code and models into the container.
COPY ./app /code/app
COPY ./models /code/models

# 6. Expose Port: We tell Docker this container uses port 8000 to communicate.
EXPOSE 8000

# 7. Start Command: The exact terminal command the container runs when it boots up.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
