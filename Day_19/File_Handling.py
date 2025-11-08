import re 
with open('./Data/obama_speech.txt') as f:
    lines = f.read()
    print(lines)

with open('./Data/obama_speech.txt') as f:
    lines = f.read()
    print(type(lines))
    list_of_words = re.findall(r'\b\w+\b', lines.lower())
    print('The total number of words in obama_speech.txt:', len(list_of_words))
    line_count = len(lines.splitlines())
    print('The total number of lines in obama_speech.txt:', line_count)

with open('./Data/michelle_obama_speech.txt') as f:
    lines = f.read()
    print(type(lines))
    list_of_words = re.findall(r'\b\w+\b', lines.lower())
    print('The total number of words in michelle_obama_speech.txt:', len(list_of_words))
    line_count = len(lines.splitlines())
    print('The total number of lines in michelle_obama_speech.txt:', line_count)

with open('./Data/donald_speech.txt') as f:
    lines = f.read()
    print(type(lines))
    list_of_words = re.findall(r'\b\w+\b', lines.lower())
    print('The total number of words in donald_speech.txt:', len(list_of_words))
    line_count = len(lines.splitlines())
    print('The total number of lines in donald_speech.txt:', line_count)

with open('./Data/melina_trump_speech.txt') as f:
    lines = f.read()
    print(type(lines))
    list_of_words = re.findall(r'\b\w+\b', lines.lower())
    print('The total number of words in melina_trump_speech.txt:', len(list_of_words))
    line_count = len(lines.splitlines())
    print('The total number of lines in melina_trump_speech.txt:', line_count)

print('\n'*2)
from collections import *
import json


def most_spoken_languages(filename, number):
    with open(filename, encoding='utf-8') as f:
        countries = json.load(f) 
    list_of_languages = [language for country in countries for language in country['languages']]
    list_of_languages = Counter(list_of_languages)
    print('The 10 most spoken languages in the world are:')
    print(list_of_languages.most_common(number))
    print(type(countries))

most_spoken_languages('./Data/countries.json', 15)


def most_populated_countries(filename, number):
    with open(filename, encoding='utf-8') as f:
        countries = json.load(f) 
    sorted_countries = sorted(countries,key=lambda c: c['population'],reverse=True)[:number]

    for c in sorted_countries:
        print(f"{c['name']}: {c['population']:,}")

most_populated_countries('./Data/countries.json', 15)

def find_most_common_words(filename, number):
    with open(filename, encoding='utf-8') as f:
        lines = f.read()
        list_of_words = re.findall(r'\b\w+\b', lines.lower())
        word_counts = Counter(list_of_words)
        print(f'The {number} most common words in {filename} are:')
        print(word_counts.most_common(number))

find_most_common_words('./Data/obama_speech.txt', 10)

print('\n'*2)

def remove_support_words(filename):
    with open(filename, encoding='utf-8') as f:
        lines = f.read()
        list_of_words = re.findall(r'\b\w+\b', lines.lower())
        stop_words = set()
        with open('./Data/stop_words.py', encoding='utf-8') as sw:
            stop_words = set(re.findall(r'\b\w+\b', sw.read().lower()))
        filtered_words = [word for word in list_of_words if word not in stop_words]
        return filtered_words


def check_text_similarity(file1, file2):
    words_file1 = set(remove_support_words(file1))
    words_file2 = set(remove_support_words(file2))
    list_of_similar_words = [word for word in words_file1 if word in words_file2]
    similarity = (len(list_of_similar_words) / ((len(words_file1) + len(words_file2)) / 2)) * 100
    print(f'The text similarity between {file1} and {file2} is {similarity:.2f}%')

def check_text_similarity1(file1, file2):
    words_file1 = set(remove_support_words(file1))
    words_file2 = set(remove_support_words(file2))
    common_words = words_file1.intersection(words_file2)
    total_unique_words = words_file1.union(words_file2)
    similarity_percentage = (len(common_words) / len(total_unique_words)) * 100
    print(f'The text similarity between {file1} and {file2} is {similarity_percentage:.2f}%')

check_text_similarity('./Data/obama_speech.txt', './Data/michelle_obama_speech.txt')
check_text_similarity1('./Data/obama_speech.txt', './Data/michelle_obama_speech.txt')


find_most_common_words('./Data/romeo_and_juliet.txt', 10)

import csv 
def word_count(*words):
    with open('./Data/HN_posts_year_to_Sep_26_2016.csv') as f:
        reader = (csv.reader(f))
        reader = list(reader)
        return {word: sum(1 for row in reader if word in row[1].lower()) for word in words}
    return (f'The word/words {words} appear {word_count("python","python b")} rows respectively in HN_posts_year_to_Sep_26_2016.csv')

print(word_count('python','python b'))

print(word_count('javascript','javascript c'))


def word_not_word(word, not_word):
    with open('./Data/HN_posts_year_to_Sep_26_2016.csv') as f:
        reader = (csv.reader(f))
        reader = list(reader)
        return {word: sum(1 for row in reader if (word in row[1].lower()) and not_word not in row[1].lower())}
    

print(word_not_word('java','javascript'))