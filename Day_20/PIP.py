import requests
import collections 
import re
import webbrowser
import statistics


from collections import Counter
url = 'http://www.gutenberg.org/files/1112/1112.txt'  # countries api
response = requests.get(url)  # opening a network and fetching a data
text = (response.text)




list_of_words = re.findall(r'\b\w+\b', text.lower())
counted_words = Counter(list_of_words)
print('The 10 most common words in the text are:')
print(counted_words.most_common(10))


print('\n'*2)
url = 'https://api.thecatapi.com/v1/breeds'  # countries api
response = requests.get(url)  # opening a network and fetching a data
cat_json = (response.json())
print(cat_json[:1])

import math 

list_of_weights = [cat['weight']['metric'] for cat in cat_json]
list_of_weights = [weight.split(' - ') for weight in list_of_weights]
list_of_weights = [(float(sublist[0])+float(sublist[1]))/2 for sublist in list_of_weights]

if list_of_weights:
    min_w = min(list_of_weights)
    max_w = max(list_of_weights)
    mean_w = statistics.mean(list_of_weights)
    median_w = statistics.median(list_of_weights)
    stdev_sample = statistics.stdev(list_of_weights) if len(list_of_weights) > 1 else 0.0
    stdev_population = statistics.pstdev(list_of_weights)

    print("\nCats' weight statistics (kg, metric):")
    print(f"Min: {min_w:.2f}")
    print(f"Max: {max_w:.2f}")
    print(f"Mean: {mean_w:.2f}")
    print(f"Median: {median_w:.2f}")
    print(f"Std dev (sample): {stdev_sample:.2f}")
    print(f"Std dev (population): {stdev_population:.2f}")
else:
    print("No weights available.")


list_of_lifespans = [cat['life_span'] for cat in cat_json]
list_of_lifespans = [lifespan.split(' - ') for lifespan in list_of_lifespans]
list_of_lifespans = [(float(sublist[0])+float(sublist[1]))/2 for sublist in list_of_lifespans]

if list_of_lifespans:
    min_l = min(list_of_lifespans)
    max_l = max(list_of_lifespans)
    mean_l = statistics.mean(list_of_lifespans)
    median_l = statistics.median(list_of_lifespans)
    stdev_sample_l = statistics.stdev(list_of_lifespans) if len(list_of_lifespans) > 1 else 0.0
    stdev_population_l = statistics.pstdev(list_of_lifespans)

    print("\nCats' lifespan statistics (years):")
    print(f"Min: {min_l:.2f}")
    print(f"Max: {max_l:.2f}")
    print(f"Mean: {mean_l:.2f}")
    print(f"Median: {median_l:.2f}")
    print(f"Std dev (sample): {stdev_sample_l:.2f}")
    print(f"Std dev (population): {stdev_population_l:.2f}")


from collections import Counter
list_of_countries = [cat['origin'] for cat in cat_json]
list_of_breeds = [cat['name'] for cat in cat_json]
combined_list = list(zip(list_of_breeds, list_of_countries))
print(combined_list)

print('\n'*2)
list_of_countries_count = Counter(list_of_countries)
most_common_countries = list_of_countries_count.most_common()
print(most_common_countries)

import json

print('\n'*2)

with open('./Data/countries.json', encoding='utf-8') as f:
    countries = json.load(f)
    list_of_pops = [(country['name'], country['population']) for country in countries]
    sorted_pops = sorted(list_of_pops, key=lambda x: x[1], reverse=True)
    print(sorted_pops[:10])

print('\n'*2)
with open('./Data/countries.json', encoding='utf-8') as f:
    list_of_langs = [country['languages'] for country in countries]
    list_of_langs = [lang for sublist in list_of_langs for lang in sublist]
    common_langs = Counter(list_of_langs)
    most_common_langs = common_langs.most_common(10)
    print(most_common_langs)
    print('the total number of languages in the database is:', len(list_of_langs))

from bs4 import BeautifulSoup

print('\n'*5)
url = 'https://archive.ics.uci.edu/datasets?sakip=0&take=10&sort=desc&orderBy=NumHits&search='  # countries api
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()) 

