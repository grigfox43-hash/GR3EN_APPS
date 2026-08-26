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
    "Запись (WebM)": "Record (WebM)",
    "Остановить": "Stop",
    "Загрузка:": "Upload:",
    "Ультра-сжатие (Minify HTML/JS/CSS)": "Ultra-Minify (HTML/JS/CSS)",
    "Удаляет все пробелы, переносы и минифицирует код для максимальной экономии веса.": "Removes all spaces, line breaks and minifies code for maximum size savings.",
    "Применяю ультра-сжатие (Minify)...": "Applying ultra-minify...",
    "Сжатие завершено! Сэкономлено: ": "Minification complete! Saved: ",
    "Код DAPI найден (рекомендуется для ironSource).": "DAPI code found (recommended for ironSource).",
    "ПРЕДУПРЕЖДЕНИЕ: ironSource предпочитает стандарт DAPI.": "WARNING: ironSource prefers the DAPI standard.",
    "Событие завершения игры (complete) найдено.": "Game complete event found.",
    "ПРЕДУПРЕЖДЕНИЕ: Vungle рекомендует отправлять событие complete.": "WARNING: Vungle recommends sending the complete event.",
    "11.025 kHz (Макс. сжатие для SFX)": "11.025 kHz (Max compression for SFX)",
    "22.05 kHz (Экономия 50% веса)": "22.05 kHz (Save 50% size)",
    "44.1 kHz (Стандарт)": "44.1 kHz (Standard)",
    "Mono (1 канал, экономия x2)": "Mono (1 channel, save 2x)",
    "Stereo (2 канала)": "Stereo (2 channels)",
    "🌐 Без задержки": "🌐 No Throttling",
    "⚡ Fast 3G (1.5 MB/s)": "⚡ Fast 3G (1.5 MB/s)",
    "🐢 Slow 3G (400 KB/s)": "🐢 Slow 3G (400 KB/s)",
    "❌ Офлайн (Offline)": "❌ Offline",
    "❌ Нет подключения (Offline)": "❌ No Connection (Offline)",
    "⚡ Эмуляция Fast 3G...": "⚡ Simulating Fast 3G...",
    "🐢 Эмуляция Slow 3G...": "🐢 Simulating Slow 3G...",
    "Скорость: 1.5 MB/s | RTT: 150ms": "Speed: 1.5 MB/s | RTT: 150ms",
    "Скорость: 400 KB/s | RTT: 400ms": "Speed: 400 KB/s | RTT: 400ms",
    "Реклама не может загрузиться без интернета": "Ad cannot load without internet connection",
    "Загрузите аудиофайл для отображения волны": "Load audio file to display waveform",
    "💡 Подсказка: Перетаскивайте левый и правый ползунки прямо по звуковой волне мышкой, чтобы обрезать лишнюю тишину.": "💡 Tip: Drag left and right handles directly across the waveform to trim silence.",
    "Скриншот Canvas": "Canvas Screenshot",
    "Запись WebM": "Record WebM",
    "Запись": "Record",
    "Стоп": "Stop",
    "Перезагрузить": "Reload",
    "ОШИБКА: Canvas не найден внутри iframe для скриншота.": "ERROR: Canvas not found inside iframe for screenshot.",
    "ОШИБКА: Canvas не найден внутри iframe для записи.": "ERROR: Canvas not found inside iframe for recording.",
    "Мульти-экран (Matrix 4x)": "Multi-Screen (Matrix 4x)",
    "Одиночный экран": "Single Screen",
    "Эмуляция сети...": "Network Emulation...",
    "Без задержки": "No Throttling",
    "Офлайн (Offline)": "Offline",
    "Поворот экрана": "Orientation",
    "Звук": "Sound",
    "Шторка (До / После)": "Split Slider (Before / After)",
    "Рядом": "Side-by-Side",
    "Масштаб:": "Zoom:",
    "По размеру": "Fit",
    "ДО (Оригинал)": "BEFORE (Original)",
    "ПОСЛЕ (Сжато)": "AFTER (Compressed)",
    "Обрезать прозрачность (Trim)": "Trim Transparent Pixels",
    "ПРЕДПРОСМОТР АНИМАЦИИ": "ANIMATION PREVIEW",
    "Кадр:": "Frame:",
    "Скорость (FPS):": "Speed (FPS):",
    "Режим воспроизведения": "Playback Mode",
    "Зациклить (Loop)": "Loop",
    "Туда-обратно (Ping-Pong)": "Ping-Pong",
    "Один раз (Once)": "Play Once",
    "Пауза": "Pause",
    "Играть": "Play",
    "Свой спрайт (Custom PNG/SVG)": "Custom Sprite (PNG/SVG)",
    "Выбрать файл": "Choose File",
    "Обрезка & Оптимизация (Trimmer)": "Trim & Optimize (Trimmer)",
    "Audio Sprite (Склейка)": "Audio Sprite (Merge)",
    "НАСТРОЙКИ ЗВУКА": "AUDIO SETTINGS",
    "Перетащите 1 аудиофайл сюда": "Drop 1 audio file here",
    "Частота (Sample Rate)": "Sample Rate",
    "Каналы": "Channels",
    "Скачать .WAV": "Download .WAV",
    "Скопировать Base64 (Data URI)": "Copy Base64 (Data URI)",
    "ВОЛНОВАЯ ФОРМА (WAVEFORM)": "WAVEFORM VISUALIZER",
    "▶ Играть выделение": "▶ Play Selection",
    "⏹ Стоп": "⏹ Stop",
    "Старт:": "Start:",
    "Конец:": "End:",
    "Длина:": "Length:",
    "ДИАГРАММА ВЕСА АССЕТОВ": "ASSET SIZE BREAKDOWN",
    "Картинки (Base64)": "Images (Base64)",
    "Аудио": "Audio",
    "HTML Разметка": "HTML Markup",
    "Медиа:": "Media:",
    "Конструктор конвертящих рекламных кнопок для Playables с анимациями (блик, пульс, 3D, свечение) и чистым HTML/CSS.": "High-converting CTA button maker for Playables with animations (shimmer, pulse, 3D, glow) and pure HTML/CSS.",
    "Генератор растровых шрифтов и таблицы глифов для Canvas. Исключает тяжелые TTF шрифты и экономит сотни килобайт.": "Bitmap font generator & glyph sheet for Canvas. Eliminates heavy TTF fonts and saves hundreds of KB.",
    "Преобразование векторных SVG иконок в нативный JavaScript Canvas 2D код (Path2D) без картинок и сторонних библиотек.": "Convert vector SVG icons directly into native JS Canvas 2D code (Path2D) without images or dependencies.",
    "Визуальный генератор конвертящих рекламных кнопок для Playable Ads с готовыми анимациями (блик, пульс, 3D, свечение) и чистым HTML/CSS экспортом.": "Visual CTA button studio for Playable Ads with ready animations (shimmer, pulse, 3D, glow) and clean HTML/CSS export.",
    "Генерация растровых шрифтов (BMFont) и таблицы глифов для Canvas. Исключает подключение тяжелых TTF файлов и экономит 100–300 КБ в Playable Ads.": "BMFont raster generator & glyph metrics for Canvas. Eliminates heavy TTF fonts, saving 100-300 KB in Playables.",
    "Конвертация векторных SVG иконок прямо в нативный JavaScript Canvas 2D код (Path2D). Идеально для легковесных UI элементов без растровых картинок.": "Convert vector SVG icons into native JS Canvas 2D code (Path2D). Perfect for lightweight UI elements.",
    "Анимационный пресет": "Animation Preset",
    "Скользящий блик (Shimmer)": "Shimmer / Light Sheen",
    "Неоновый пульс (Pulse Glow)": "Neon Pulse Glow",
    "Покачивание (Wiggle / Attention)": "Wiggle / Attention",
    "Ритмичный пульс (Heartbeat)": "Heartbeat",
    "3D Нажатие (3D Press & Shadow)": "3D Press & Shadow",
    "Живой градиент (Gradient Wave)": "Gradient Wave",
    "Без анимации (Static)": "Static (No Animation)",
    "Текст кнопки": "Button Text",
    "Иконка": "Icon",
    "Стрелка (➔)": "Arrow (➔)",
    "Геймпад (🎮)": "Gamepad (🎮)",
    "Искра (✨)": "Sparkle (✨)",
    "Скачать (⬇)": "Download (⬇)",
    "Огонь (🔥)": "Fire (🔥)",
    "Без иконки": "No Icon",
    "Цвета кнопки (Градиент)": "Button Colors (Gradient)",
    "Цвет 1 | Цвет 2 | Текст | Свечение": "Color 1 | Color 2 | Text | Glow",
    "Скругление углов:": "Border Radius:",
    "Размер шрифта:": "Font Size:",
    "Отступы (Padding)": "Padding",
    "Скопировать HTML + CSS": "Copy HTML + CSS",
    "ИНТЕРАКТИВНЫЙ ПРЕДПРОСМОТР (Кликните по кнопке)": "INTERACTIVE PREVIEW (Click button)",
    "ГОТОВЫЙ КОД ДЛЯ PLAYABLE AD:": "READY CODE FOR PLAYABLE AD:",
    "Скопировать": "Copy",
    "Набор символов (Charset)": "Charset",
    "Только цифры и знаки (0-9 + - = : % $)": "Digits & Symbols only (0-9 + - = : % $)",
    "Латиница + Цифры (A-Z, a-z, 0-9, знаки)": "Latin + Digits (A-Z, a-z, 0-9, symbols)",
    "Кириллица + Цифры (А-Я, а-я, 0-9)": "Cyrillic + Digits (А-Я, а-я, 0-9)",
    "Пользовательский набор": "Custom Charset",
    "Шрифт и размер": "Font Family & Size",
    "Заливка символов": "Glyph Fill",
    "Градиент": "Gradient",
    "Обводка (Stroke, px):": "Stroke (px):",
    "Тень (Shadow, px):": "Shadow (px):",
    "Отступ между глифами (Padding, px)": "Glyph Padding (px)",
    "Скачать .PNG атлас": "Download .PNG Atlas",
    "Скачать .JSON метрики": "Download .JSON Metrics",
    "ИНТЕРАКТИВНЫЙ ТЕСТ ШРИФТА (CANVAS)": "INTERACTIVE FONT TEST (CANVAS)",
    "АТЛАС РАСТРОВЫХ СИМВОЛОВ": "BITMAP GLYPH ATLAS",
    "JS ФУНКЦИЯ ДЛЯ ОТРИСОВКИ ТЕКСТА:": "JS FUNCTION FOR TEXT RENDERING:",
    "ВХОДНОЙ SVG": "INPUT SVG",
    "Перетащите .SVG файл сюда": "Drop .SVG file here",
    "Готовые пресеты иконок": "Icon Presets",
    "Кубок (Trophy)": "Trophy",
    "Геймпад (Gamepad)": "Gamepad",
    "Звезда (Star)": "Star",
    "Сердце (Heart)": "Heart",
    "Монета (Coin)": "Coin",
    "Щит (Shield)": "Shield",
    "Или вставьте SVG код:": "Or paste SVG code:",
    "Цвет заливки (Fill Override)": "Fill Color Override",
    "Применить цвет": "Apply Color",
    "Конвертировать в JS": "Convert to JS",
    "ПРЕДПРОСМОТР CANVAS РЕНДЕРА": "CANVAS RENDER PREVIEW",
    "Размер:": "Size:",
    "JS CANVAS ФУНКЦИЯ:": "JS CANVAS FUNCTION:",
    "Скопировать код": "Copy Code",
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
    try:
        print("Missing translation:", s)
    except:
        pass
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
