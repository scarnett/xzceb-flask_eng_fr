import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

api_key = os.environ['API_KEY']
api_url = os.environ['API_URL']

authenticator = IAMAuthenticator(api_key)
language_translator = LanguageTranslatorV3(
    version='2021-12-01', authenticator=authenticator)
language_translator.set_service_url(api_url)


def english_to_french(text):
    if text:
        translation = language_translator.translate(
            text=text, model_id='en-fr').get_result()
        if has_translations(translation):
            return translation['translations'][0]['translation']
    return None


def french_to_english(text):
    if text:
        translation = language_translator.translate(
            text=text, model_id='fr-en').get_result()
        if has_translations(translation):
            return translation['translations'][0]['translation']
    return None


def has_translations(translation):
    return translation and \
        ('translations' in translation) and (
            len(translation['translations']) > 0)
