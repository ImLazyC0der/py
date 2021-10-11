#pip install googletrans==3.1.0a0

import googletrans

translator = googletrans.Translator()
translated = translator.translate('Your sentence',dest='es')
print(translated.text)
print(googletrans.Languages)
