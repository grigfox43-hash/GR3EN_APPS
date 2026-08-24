// js/translate.js
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
