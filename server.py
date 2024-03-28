import os
import logging
import asyncio

from flask import Flask
from main import main

app = Flask(__name__)


@app.route("/")
def index():
    return "Сервер стоит"


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='log.txt')
    asyncio.run(main())
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)