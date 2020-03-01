FROM python:3.7-slim
WORKDIR /app
COPY . /app/
RUN chmod +x ./startup.sh
CMD [ "./startup.sh" ]