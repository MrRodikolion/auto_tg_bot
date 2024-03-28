import os
import json
from random import choice

dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dir, 'themes.json'), encoding='utf-8') as themes_json_file:
    themes = json.load(themes_json_file)


def get_theme() -> list[str, str]:
    return choice(themes)
