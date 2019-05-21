# -*- coding: utf-8 -*-

import pandas as pd


# SEPARATE TOWNS, STATES & COUNTIES DATASETS

dataset = pd.read_csv('geoplanet_places.tsv', sep='\t')

dataset_towns = dataset.loc[dataset['PlaceType'] == "Town"]
dataset_towns = dataset_towns.iloc[:, [2,5,1,0]]


dataset_counties = dataset.loc[dataset['PlaceType'] == "County"]
dataset_counties = dataset_counties.iloc[:,[0,2]]

dataset_states = dataset.loc[dataset['PlaceType'] == "State"]
dataset_states = dataset_states.iloc[:,[0,2]]

################ 1

## REPLACE TOWNS PARENT_ID WITH COUNTY
replace_county = dict(dataset_counties.to_dict('split')['data'])
dataset_towns['Parent_ID'] = dataset_towns['Parent_ID'].map(replace_county)

dataset_towns_clean = dataset_towns.dropna()

dataset_nan = dataset_towns.loc[dataset_towns['Parent_ID'].isnull()]
dataset_nan['Parent_ID'] = dataset_nan['Name']


frames = [dataset_towns_clean, dataset_nan]
dataset_towns = pd.concat(frames)


dataset_clean = pd.DataFrame()

dataset_clean['locality'] =  dataset_towns['Name']
dataset_clean['area'] =  dataset_towns['Parent_ID']
dataset_clean['country'] =  dataset_towns['ISO']
dataset_clean['woeid'] = dataset_towns['WOE_ID']

dataset_clean.to_csv("geo_clean.csv", index = False, encoding = "utf-8")



## TEST
dataset_woe = dataset.loc[dataset['WOE_ID'] == 24548810]
dataset_mazow = dataset.loc[dataset['Name'] == "Mazowieckie"]
dataset_warsaw = dataset.loc[dataset['Name'] == "Warszawa"]
dataset_warszawa = dataset_clean.loc[dataset_clean['locality'] == "Warszawa"]
dataset_ny = dataset_clean.loc[dataset_clean['locality'] == "New York"]
dataset_war = dataset_clean.loc[dataset_clean['locality'] == "Warsaw"]


