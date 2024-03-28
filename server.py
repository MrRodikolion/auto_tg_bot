import os
import logging
import asyncio

from flask import Flask
from main import main

app = Flask(__name__)


@app.route("/")
def index():
    return "Сервер стоит"

async def run_server():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

async def run_bot():
    await main()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='log.txt')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        run_bot(),
        # run_server()
    ))
    loop.close()
