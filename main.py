# -*- coding: utf-8 -*-
import os
import requests
import json
import tarfile

import pickle
import time

s = requests.Session()
s.auth = ('mymail@gmail.com', "d36dea77fbd01eaa1257e532841be0fd")
endpoint = "http://challenges.tmlc1.unpossib.ly/api/tests"

folder_path = "/input/message_pred/"

def entitiesDic(tweet):
    res = {}
    for idx in len(tweet['entitiesFull']):
        res.update(tweet['entitiesFull'][idx], tweet['entitiesShortened'][idx])
    return res

def fileList(folder):
    filelist = os.listdir(folder)
    res=[]
    for fname in filelist:
        res.append(fname)
    return res

def findId(obj):
    res = obj['id']
    return res

# list of letter entities
def listLetters(obj):
    res = []
    for entities in obj['entitiesShortened']:
        if entities['type'] == 'letter':
            res.append(entities['value'])
    return res

if __name__ == '__main__':
    print('-------------')
    '''
    file = folder_path + 'json/score/tmlc1-scoring-001.json'
    with open(file) as f:
        train_001 = json.load(f)
    '''
    for file in os.listdir(folder_path + 'json/score/'):
        json_file = folder_path + 'json/score/' + file
        data = {}
        with open(json_file) as f:
            test_file = json.load(f)
            for tweet in test_file:
                twitter_id = findId(tweet)
                letters_list = listLetters(tweet)
                array_list = []
                array_list.append(letters_list)
                array_list.append(letters_list)
                array_list.append(letters_list)
                data[twitter_id] = array_list

        # create json object from data
        json_obj = json.dumps(data)
        time.sleep(1)

        # Store data (serialize)
        with open('{:s}.pickle'.format(file), 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print('-------------')