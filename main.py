from post_gen import gen_img, yandex
from theme import get_theme
import config

import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from io import BytesIO

bot = Bot(token=config.bot_token, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())


async def post_creation():
    while True:
        post_theme = get_theme()
        text = yandex.gen_text(post_theme[0])[:1024]
        img = gen_img(post_theme[1])

        img_bytes = BytesIO()
        img.save(img_bytes, format='png')
        img_bytes.seek(0)

        await bot.send_photo(
            config.group_id,
            types.BufferedInputFile(img_bytes.read(), 'chay.png'),
            caption=text,
            parse_mode=ParseMode.MARKDOWN
        )

        await asyncio.sleep(60)


async def main():
    # dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)

    await asyncio.create_task(post_creation())

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='log.txt')
    asyncio.run(main())
