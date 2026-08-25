import glob

for f_name in glob.glob('*.html'):
    with open(f_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix textareas
    if '<textarea ' in content:
        content = content.replace('<textarea ', '<textarea class="notranslate" translate="no" ')
    
    # Fix validator log box
    if 'id="logBox"' in content:
        content = content.replace('id="logBox" class="log-box"', 'id="logBox" class="log-box notranslate" translate="no"')
        
    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(content)
print("Done")
