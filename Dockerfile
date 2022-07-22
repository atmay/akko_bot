FROM python:3.10-slim

RUN mkdir /bot

COPY requirements.txt /bot

RUN pip3 install -r /bot/requirements.txt --no-cache-dir

COPY akko_bot/ /bot

WORKDIR /bot

CMD ["python3", "bot.py", "main"]