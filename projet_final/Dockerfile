FROM python:3.6-alpine
WORKDIR /opt
COPY . .
RUN pip install flask
EXPOSE 8080
CMD ["python", "app.py"]
