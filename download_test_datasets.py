# -*- coding: utf-8 -*-
import os
import requests
import json
import tarfile

import pandas as pd

s = requests.Session()
s.auth = ('mymail@gmail.com', "d36dea77fbd01eaa1257e532841be0fd")
API_URL = "http://challenges.tmlc1.unpossib.ly/api/datasets"
response = s.get(API_URL)
response_data = json.loads(response.text)


folder_path = "/input/message_pred/"

def createFilename(url, name, folder):
    dotSplit = url.split('.gz')
    print(dotSplit)
    if name == None:
        # use the same as the url
        slashSplit = dotSplit[-2].split('/')
        name = slashSplit[-1]
    ext = 'gz'
    file = '{}{}.{}'.format(folder, name, ext)
    return file

def getDataset(url, name=None, folder=folder_path + 'datasets/'):
    file = createFilename(url, name, folder)
    with open(file, 'wb') as f:
        r = s.get(url, stream=True)
        for block in r.iter_content(1024):
            if not block:
                break
            f.write(block)

def downloadDatasets():
    #remove scoring dataset for now
    response_data['datasets'].pop(0)
    for dataset in response_data['datasets']:
        download_url = dataset['downloadUrl']
        print(download_url)
        file = createFilename(download_url, None, '')
        print(file)
        getDataset(download_url)


def extractFiles():
    filelist = os.listdir(folder_path + 'datasets/')
    for fname in filelist:
        if (fname.endswith("tar.gz")):
            tar = tarfile.open(fname, "r:gz")
            tar.extractall()
            tar.close()

if __name__ == '__main__':
    print('----')
    
    #download compressed datasets
    downloadDatasets()

    #extract all datasets
    extractFiles()