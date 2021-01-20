#!/usr/bin/env python
# coding: utf-8

# In[35]:

import pandas as pd
import argparse
import numpy as np
from math import radians, degrees, sin, cos, asin, acos, sqrt
from itertools import combinations

# In[36]:

n = None

# In[37]:

parser = argparse.ArgumentParser()

parser.add_argument('user_input', type = int)

try:
    args = parser.parse_args()

    n = args.user_input
except:
    n = None

# In[3]:

df = pd.read_csv("places.csv")

# In[13]:

def get_place_combinations(places):
    temp = []
    for p in combinations(places, 2):
        temp.append(list(p))        
    return temp

# In[14]:

if n == None:
    places_pairs = get_place_combinations(list(df['Name']))
else:
    places_pairs = get_place_combinations(list(df['Name'].sample(n)))


# In[16]:

def get_pairs_distance(pair):
    
    lon1 = df[df['Name']== pair[0]]['Longitude']
    lat1 = df[df['Name']== pair[0]]['Latitude']
    lon2 = df[df['Name']== pair[1]]['Longitude']
    lat2 = df[df['Name']== pair[1]]['Latitude']
    
    # great circle distance
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])   
    return 6371*(acos(sin(lat1)*sin(lat2)+cos(lat1)*cos(lat2) * cos(lon1 - lon2)))

# In[17]:

places_pairs_distance = [[p[0],p[1],get_pairs_distance(p)] for p in places_pairs]

# In[30]:

output = pd.DataFrame(places_pairs_distance, columns = ["place_1", "place_2", "distance"])

# In[31]:

output = output.sort_values(by = 'distance')
output = output.reset_index(drop=True)

# In[34]:

print(output)
print('\n')

# average distance
mean_dist = output['distance'].mean()

min_dist_pair = []
diff = float('inf')

for p1,p2,d in zip(output['place_1'],output['place_2'],output['distance']):
    if abs(mean_dist - d) < diff:
        diff = abs(mean_dist - d)
        min_dist_pair = [p1,p2,d]

print(f"Average distance: {round(mean_dist,1)} km. Closest pair: {min_dist_pair[0]}-{min_dist_pair[1]} {round(min_dist_pair[2],1)} km.")