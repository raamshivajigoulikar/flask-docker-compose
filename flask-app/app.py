import os
from flask import Flask
from flask import url_for
from flask import jsonify
from flask import request
import json
from worker import celery
from celery.result import AsyncResult
import celery.states as states

env=os.environ
app = Flask(__name__)

LANGUAGES = ['en','fr','es','pt','it','nl']

class LanguageNotImplemented(Exception):
    pass

@app.route('/')
def index():
    return "<p>Hello, world!</p>"

# curl -X POST -H "Content-Type: application/json" --data '{"model": "Sentence", "model_id": "123", "fluent_language_cd": "fr", "target_language_cd": "en", "text": "A very simple sentence"}' http://127.0.0.1:5000/api/parser

@app.route('/api/inbound', methods=['POST'])
def parser():
  try:
    payload = request.json
    target_language_cd = request.json.get('target_language_cd')
    text = request.json.get('text')
    if not target_language_cd in ['en','fr']:
        raise LanguageNotImplemented("Not a supported language %s" % (target_language_cd))

    task = celery.send_task('parse_text', args=[target_language_cd,text], kwargs={})
    resp = jsonify({"status": "submitted", "message": "submitted for processing" })
    resp.status_code = 200
    return resp
  except Exception as e:
    resp = jsonify({"status":"failed", "message": repr(e), "payload_received": payload })
    resp.status_code = 500
    return resp

if __name__ == '__main__':
    app.run(debug=env.get('DEBUG',True),
            port=int(env.get('PORT',5000)),
            host=env.get('HOST','0.0.0.0')
    )
