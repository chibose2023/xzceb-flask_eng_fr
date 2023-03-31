""" Language translator"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2022-08-05',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishText):
    #write the code here
    translate = language_translator.translate(text=englishText, model_id='en-fr')
    translation = translate.get_result()
    french_text = translation['translations'][0]['translation']
    return french_text.lower()

def french_to_english(frenchText):
    #write the code here
    translate = language_translator.translate(text=frenchText, model_id='fr-en')
    translation = translate.get_result()
    english_text = translation['translations'][0]['translation']
    return english_text.lower()