FROM python:3.12

WORKDIR /app

EXPOSE 5000

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

CMD ["python3", "application.py"]