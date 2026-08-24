import os, glob

os.makedirs('js', exist_ok=True)
with open('js/translate.js', 'w', encoding='utf-8') as f:
    f.write('''// js/translate.js
function setCookie(key, value, expiry) {
  var expires = new Date();
  expires.setTime(expires.getTime() + (expiry * 24 * 60 * 60 * 1000));
  document.cookie = key + '=' + value + ';expires=' + expires.toUTCString() + ';path=/';
}
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'ru', includedLanguages: 'ru,en', autoDisplay: false}, 'google_translate_element');
}
document.addEventListener('DOMContentLoaded', () => {
  const lang = localStorage.getItem('lang') || 'ru';
  setCookie('googtrans', lang === 'en' ? '/ru/en' : '/ru/ru', 1);
  const gt = document.createElement('div');
  gt.id = 'google_translate_element';
  gt.style.display = 'none';
  document.body.appendChild(gt);
  const script = document.createElement('script');
  script.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
  document.body.appendChild(script);
  const btns = document.querySelectorAll('.lang-btn');
  btns.forEach(b => {
    if (b.dataset.lang === lang) b.classList.add('active');
    else b.classList.remove('active');
    b.addEventListener('click', (e) => {
      e.preventDefault();
      const targetLang = e.target.dataset.lang;
      localStorage.setItem('lang', targetLang);
      setCookie('googtrans', targetLang === 'en' ? '/ru/en' : '/ru/ru', 1);
      window.location.reload();
    });
  });
});
''')

with open('css/tools.css', 'a', encoding='utf-8') as f:
    f.write('\n/* Google Translate Hide */\nbody { top: 0 !important; }\n.goog-te-banner-frame { display: none !important; }\n.goog-tooltip { display: none !important; }\n.goog-te-combo { display: none !important; }\n')

nav_li = '''          <li>
            <div class="lang-switcher">
              <button class="lang-btn active" data-lang="ru">RU</button>
              <button class="lang-btn" data-lang="en">EN</button>
            </div>
          </li>'''
script_tag = '<script src="js/translate.js"></script>\n</body>'

for html_file in glob.glob('*.html'):
    if html_file == 'validator_dom.html': continue
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<div class="lang-switcher">' not in content:
        content = content.replace('<ul class="nav-menu">', '<ul class="nav-menu">\n' + nav_li)
    
    if 'js/translate.js' not in content:
        content = content.replace('</body>', script_tag)
        
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
