import os
import time
from celery import Celery
import requests
import json
import urllib2
import spacy
from celery import Celery
from rails_api import RailsAPI
import secrets as config

env=os.environ
CELERY_BROKER_URL=env.get('CELERY_BROKER_URL','redis://localhost:6379'),
CELERY_RESULT_BACKEND=env.get('CELERY_RESULT_BACKEND','redis://localhost:6379')


celery= Celery('tasks',
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)


@celery.task(name='parse_text')
def parse_text(target_language_cd,fluent_language_cd,model,model_id,text):
    print('\n' + '<------ task ------>')
    print('target_language_cd: ' + target_language_cd)
    print('fluent_language_cd: ' + fluent_language_cd)
    print('model: ' + model)
    print('model_id: ' +  str(model_id))
    print('text: ' + text)
    print '\n'
    parsed = None

    try:
        nlp = spacy.load(target_language_cd)
        doc = nlp(unicode(text))
        parsed = [(w.text, w.whitespace_, w.pos_, w.is_alpha, w.is_stop, w.lower_) for w in doc]
        # TODO raise exception if results of parser are empty
    except Exception as e:
        #logger.info  ('{}: '.format(sys.exc_info()[-1].tb_lineno))
        raise e
    finally:
        api = RailsAPI()
        api.parsed(model,model_id,parsed,fluent_language_cd)
        return True
