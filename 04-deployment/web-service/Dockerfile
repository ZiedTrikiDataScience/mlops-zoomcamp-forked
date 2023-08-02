FROM python:3.9.7-slim

RUN pip install --upgrade pip 

WORKDIR /app

COPY [ "requirements.txt", "./" ]

RUN  pip install --no-cache-dir -r requirements.txt

COPY [ "predict.py", "lin_reg.bin", "./" ]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696" ,"predict:app"]