with open('css/modern.css', 'a', encoding='utf-8') as f:
    f.write('\n/* Google Translate Hide aggressive */\n')
    f.write('body { top: 0 !important; }\n')
    f.write('.skiptranslate iframe { display: none !important; visibility: hidden !important; }\n')
    f.write('.goog-te-banner-frame { display: none !important; visibility: hidden !important; }\n')
    f.write('.VIpgJd-ZVi9od-aZ2wEe-wOHMyf { display: none !important; }\n')
    f.write('.VIpgJd-ZVi9od-aZ2wEe-wOHMyf-ti6hGc { display: none !important; }\n')
    f.write('#goog-gt-tt { display: none !important; }\n')
    f.write('.goog-tooltip { display: none !important; }\n')
