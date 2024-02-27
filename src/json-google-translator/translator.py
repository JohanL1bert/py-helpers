import json
import os
import httpx
from googletrans import Translator


timeout = httpx.Timeout(5) # 5 seconds timeout

translator = Translator(timeout=timeout)

""" Setup init """

""" must be in curr directory """
JSON_FILE_NAME = 'words.json' 
ENC_FILE = 'utf-8'

""" Template String. Need to create by u own. For example """
FIRST_Temaplte = 'textExampleTranslate'
SECOND_TEMPLATE = 'textMeaningTranslate'
THIRTH_TEMPLATE = 'wordTranslate'
""" Template string is column name in your json. What you need to translate. For example
column name - translate sentence
"wordTranslate": "alcohol"
"""

""" LANG  SRC = from what lang, DESt = translate to"""
SRC = 'en'
DEST= 'uk'


counter = 0
filepath = os.path.join(os.path.dirname(__file__), JSON_FILE_NAME)
with open(filepath, 'r', encoding=ENC_FILE) as i18n_file:
    parsed_json = json.loads(i18n_file.read())
    for i in parsed_json:
        for k, v in i.items():
            if (k == FIRST_Temaplte or k == SECOND_TEMPLATE or k == THIRTH_TEMPLATE):
                translate_sentence = translator.translate(v, src=SRC, dest=DEST)
                i[k] = translate_sentence.text
                counter+= 1


y = json.dumps(parsed_json)
with open(filepath, 'w', errors='ignore', encoding=ENC_FILE) as b:
    b.write(y)




