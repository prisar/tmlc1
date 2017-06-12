# -*- coding: utf-8 -*-

import json
import os
import pandas as pd

file = '/input/message_pred/json/old/tmlc1-training-01/tmlc1-training-001.json'

with open(file) as f:
    train = json.load(f)

df = pd.read_json(file)
print(df.columns)

print(len(df['entitiesFull'][0]))
print(len(df['text'][0].split(' ')))
print(df['text'][0])
