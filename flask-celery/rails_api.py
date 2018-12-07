import requests
import secrets as config

class RailsAPI(object):
  def __init__(self):
    token=config.RAILS_API_KEY
    self.base_url = config.RAILS_API_SERVER + 'api/'
    self.headers = { 'Authorization': 'Token token=' + token, "Content-Type": "application/json" }

  def parsed(self,model,model_id,parsed,fluent_language_cd):
    url = self.base_url + 'parsed'
    payload = {"model": model, "model_id": model_id, "parsed": parsed, "fluent_language_cd": fluent_language_cd}
    print 'CALLING RAILS'
    response = requests.post(url, json=payload, headers=self.headers, verify=False)
    print response


    # curl -X PUT -G http://localhost:3000/api/submissions/24 -d "score=999999" -d "score_secondary=123456" -H 'Authorization: Token token="3224e9e60547e19f8dfd377999895b391735a2f63e5d5cfceb7eae887b20ccfa66102bf56f8f0af2e3e1071fc4317683c2c84cb3bdc8c497531740b9e3b54d0a"'
