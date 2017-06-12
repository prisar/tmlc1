# -*- coding: utf-8 -*-

import os
import requests
import json

s = requests.Session()
s.auth = ('mymail@gmail.com', "d36dea77fbd01eaa1257e532841be0fd")
API_URL = "http://challenges.tmlc1.unpossib.ly/api/datasets"
response = s.get(API_URL)
response_data = json.loads(response.text)

folder_path = "/input/message_pred/json/score/"

def createFilename(url, name, folder):
    dotSplit = url.split('.json')
    if name == None:
        # use the same as the url
        slashSplit = dotSplit[-2].split('/')
        name = slashSplit[-1]
    ext = 'json'
    file = '{}{}.{}'.format(folder, name, ext)
    return file

def getDataset(url, name=None, folder=folder_path):
    file = createFilename(url, name, folder)
    with open(file, 'wb') as f:
        r = s.get(url, stream=True)
        for block in r.iter_content(1024):
            if not block:
                break
            f.write(block)


def downloadScoringDatasets():
    download_url1 = response_data['datasets'][0]['downloadUrl']
    getDataset(download_url1)
    download_url2 = response_data['datasets'][1]['downloadUrl']
    getDataset(download_url2)
    download_url3 = response_data['datasets'][2]['downloadUrl']
    getDataset(download_url3)

downloadScoringDatasets()