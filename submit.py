# -*- coding: utf-8 -*-
import os
import requests
import json
import pickle

s = requests.Session()
s.auth = ('mymail@gmail.com', "d36dea77fbd01eaa1257e532841be0fd")

# submit tests
test_endpoint = "http://challenges.tmlc1.unpossib.ly/api/tests"
submission_endpoint = "http://challenges.tmlc1.unpossib.ly/api/submissions"
endpoint = submission_endpoint

'''
folder_path = "/input/message_pred/json/score/"

# Load data (deserialize)
for file in os.listdir(folder_path):
    with open('{:s}.pickle'.format(file), 'rb') as handle:
        data = pickle.load(handle)
        
        # create json object from data
        json_obj = json.dumps(data)
        response = s.post(endpoint, json_obj)
        print(json.loads(response.text))
'''
with open('tmlc1-scoring-003.json.pickle', 'rb') as handle:
    data = pickle.load(handle)
    
    # create json object from data
    json_obj = json.dumps(data)
    response = s.post(endpoint, json_obj)
    print(json.loads(response.text))
