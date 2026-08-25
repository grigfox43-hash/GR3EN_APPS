import os, glob, re
from html.parser import HTMLParser

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts = set()
        self.ignore = False
    def handle_starttag(self, tag, attrs):
        if tag in ['script', 'style']: self.ignore = True
    def handle_endtag(self, tag):
        if tag in ['script', 'style']: self.ignore = False
    def handle_data(self, data):
        if self.ignore: return
        text = data.strip()
        if re.search(r'[А-Яа-яЁё]', text): self.texts.add(text)

parser = TextParser()
html_files = [f for f in glob.glob('*.html') if not f.endswith('_en.html') and f != 'validator_dom.html']
for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        parser.feed(f.read())

ru_strings = sorted(list(parser.texts))

# Hardcode the translations!
translations = {
    "ПОЛЕЗНЫЕ": "USEFUL",
    "ИНСТРУМЕНТЫ": "TOOLS",
    "Набор утилит для проверки, оптимизации и создания контента для HTML5 игр и рекламных креативов (Playables).": "A set of utilities for validating, optimizing, and creating content for HTML5 games and playable ads.",
    "Валидатор Playable Ads. Проверка на соответствие требованиям 10+ рекламных площадок (AppLovin, ironSource, Mintegral и др).": "Playable Ads Validator. Check compliance with requirements of 10+ ad networks (AppLovin, ironSource, Mintegral, etc).",
    "Для разработчиков Playable Ads & WebGL": "For Playable Ads & WebGL Developers",
    "Открыть": "Open",
    "НА ГЛАВНУЮ": "HOME",
    "Пресет": "Preset",
    "Взрыв (Explosion)": "Explosion",
    "Огонь (Fire)": "Fire",
    "Магия (Sparkles)": "Sparkles",
    "Снег (Snow)": "Snow",
    "Дождь (Rain)": "Rain",
    "Конфетти (Confetti)": "Confetti",
    "Дым (Smoke)": "Smoke",
    "Космос (Stars)": "Stars",
    "Пузырьки (Bubbles)": "Bubbles",
    "Лазер (Laser Spark)": "Laser",
    "Галактика (Galaxy)": "Galaxy",
    "Портал (Portal)": "Portal",
    "Кровь (Blood Splatter)": "Blood",
    "Яд (Poison Gas)": "Poison Gas",
    "Метеорит (Meteor Shower)": "Meteor Shower",
    "Искры (Welding Sparks)": "Welding Sparks",
    "Сердечки (Hearts)": "Hearts",
    "Пыль (Ambient Dust)": "Ambient Dust",
    "Светлячки (Fireflies)": "Fireflies",
    "Молния (Lightning)": "Lightning",
    "Вьюга (Snowstorm)": "Snowstorm",
    "Тлеющие угли (Embers)": "Embers",
    "Глитч (Glitch Blocks)": "Glitch",
    "Матрица (Matrix Code)": "Matrix Code",
    "Водоворот (Swirl)": "Swirl",
    "Сохранить Мой Пресет": "Save My Preset",
    "Загрузить Мой Пресет": "Load My Preset",
    "Эффект (Пресет)": "Effect (Preset)",
    "Генератор 2D частиц (Canvas). Взрывы, магия, огонь и снег. Экспорт в Vanilla JS класс без зависимостей.": "2D Particle Generator (Canvas). Explosions, magic, fire and snow. Export to Vanilla JS class with zero dependencies.",
    "Создание и экспорт WebGL шейдеров для Three.js и PixiJS. Библиотека готовых эффектов с настройками.": "Create and export WebGL shaders for Three.js and PixiJS. Library of effects with settings.",
    "Валидатор интерактивной рекламы. Проверьте ваш архив или HTML файл на соответствие техническим требованиям рекламных сетей.": "Interactive Ads Validator. Check your archive or HTML file for compliance with network technical requirements.",
    "Рекламная сеть": "Ad Network",
    "Требования сети:": "Network Requirements:",
    "Лог проверки:": "Validation Log:",
    "Готов к проверке. Выберите файл.": "Ready for check. Select a file.",
    "ДЕТАЛИ": "DETAILS",
    "Сборка множества изображений в единый спрайт-лист (атлас) для оптимизации отрисовки. Экспорт в PNG + JSON.": "Assemble multiple images into a single sprite sheet (atlas). Export to PNG + JSON.",
    "Упаковка всего проекта (HTML, CSS, JS, картинки, звуки) в один index.html файл. Автоматическое кодирование в Base64.": "Pack the entire project (HTML, CSS, JS, images, sounds) into a single index.html file. Base64 encoding.",
    "Объединение множества звуков в один аудиотрек для обхода ограничений автовоспроизведения в мобильных браузерах.": "Combine multiple sounds into one audio track to bypass autoplay restrictions on mobile browsers.",
    "Быстрое кодирование шрифтов, изображений и любых файлов в Data URI (Base64) для вставки в CSS или JS.": "Fast encoding of fonts, images and files to Data URI (Base64).",
    "Сжатие и оптимизация PNG / JPG для Playable Ads прямо в браузере. Уменьшение веса креатива без потери качества.": "Compress and optimize PNG / JPG right in the browser. Reduce creative size.",
    "Удаление пробелов, комментариев и минификация кода (Terser). Экономия веса для соответствия жестким лимитам площадок.": "Remove spaces, comments and minify code (Terser). Save size.",
    "Все права защищены.": "All rights reserved."
}

import urllib.request, urllib.parse, json

def get_trans(s):
    if s in translations: return translations[s]
    # Simple fallback translation using memory
    print("Missing translation:", s)
    return s

for s in ru_strings:
    if s not in translations:
        translations[s] = get_trans(s)

sorted_keys = sorted(translations.keys(), key=len, reverse=True)

for f_name in html_files:
    with open(f_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    en_content = content
    for k in sorted_keys:
        en_content = en_content.replace(k, translations[k])
    
    en_file = f_name.replace('.html', '_en.html')
    
    content = re.sub(r' onclick=\"window\.location\.href=\'[^\']+\'\"', '', content)
    en_content = re.sub(r' onclick=\"window\.location\.href=\'[^\']+\'\"', '', en_content)
    
    content = content.replace('<button class=\"lang-btn active\" data-lang=\"ru\">RU</button>', f'<button class=\"lang-btn active\" data-lang=\"ru\" onclick=\"window.location.href=\'{f_name}\'\">RU</button>')
    content = content.replace('<button class=\"lang-btn\" data-lang=\"en\">EN</button>', f'<button class=\"lang-btn\" data-lang=\"en\" onclick=\"window.location.href=\'{en_file}\'\">EN</button>')
    content = content.replace('<script src=\"js/translate.js\"></script>', '')

    en_content = en_content.replace('<button class=\"lang-btn active\" data-lang=\"ru\">RU</button>', f'<button class=\"lang-btn\" data-lang=\"ru\" onclick=\"window.location.href=\'{f_name}\'\">RU</button>')
    en_content = en_content.replace('<button class=\"lang-btn\" data-lang=\"en\">EN</button>', f'<button class=\"lang-btn active\" data-lang=\"en\" onclick=\"window.location.href=\'{en_file}\'\">EN</button>')
    en_content = en_content.replace('<script src=\"js/translate.js\"></script>', '')
    
    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(content)
        
    with open(en_file, 'w', encoding='utf-8') as f:
        f.write(en_content)

if os.path.exists('js/translate.js'):
    os.remove('js/translate.js')
print('Done!')
