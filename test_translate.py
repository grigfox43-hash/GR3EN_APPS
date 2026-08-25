from deep_translator import MyMemoryTranslator
try:
    print(MyMemoryTranslator(source='ru', target='en').translate('Валидатор'))
except Exception as e:
    print('Error:', repr(e))
