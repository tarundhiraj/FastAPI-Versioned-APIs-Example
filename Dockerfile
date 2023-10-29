from python:3.11-slim

WORKDIR /app

COPY ./src/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /app/src/start_app.sh

EXPOSE 8080

CMD ["/app/src/start_app.sh"]
