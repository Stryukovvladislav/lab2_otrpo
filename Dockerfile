FROM python:3.10.12-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt cv2

COPY . .

CMD [ "python", "./main.py" ]

