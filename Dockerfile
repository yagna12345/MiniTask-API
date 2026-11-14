FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ ./app/
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# TODO 1: Copy requirements.txt into the image.
# TODO 2: Install Python dependencies with pip.
# TODO 3: Copy the app/ folder into /app/app/.
# TODO 4: Document the port the API listens on.
# TODO 5: Start uvicorn app.main:app on host 0.0.0.0 port 8000.
