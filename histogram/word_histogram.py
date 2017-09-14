#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from pprint import pprint

word_map = {
    'javiir': 'javier',
    'javir': 'javier',
    'thanks': 'thank',
    'neonazi': 'trump',
    'neonazis': 'donald',
    'mrpresident': 'president',
    'bezos': 'trump',
    'mccain': 'person',
    'exofficials': 'nonofficial',
    'libtards': 'lips'
}

preps = ['it','be','not','with','all','we','this','have','they','on','i','your','that','are','for','in','is','a','of','you','to','and','the']


def word_histogram(lines):
    hist = {}
    dict_file = open('words.txt', 'r')

    words = { w.lower().strip(): 0 for w in dict_file }
    dict_file.close()
    for line in lines:
        for word in line.split(' '):
            # Clean word
            word = ''.join(c for c in word if c.isalnum())
            word = word.lower().strip()
            word = word_map[word] if word_map.has_key(word) else word

            if word != '' and words.has_key(word) and word not in preps:
                hist[word] = 1 if word not in hist else hist[word] + 1

    pairs = zip(hist.iterkeys(), hist.itervalues())
    return sorted(pairs, key=lambda pair: -pair[1])

def get_column(file_path, col_name, expr = lambda x: x):
    f = open(file_path, 'r')
    # column names
    columns = f.readline().rstrip('\n').split('\t')
    idx = columns.index(col_name)
    lines = [expr(line.rstrip('\n').split('\t')[idx]) for line in f]
    f.close()
    return lines

def remove_outliers(linespace):
    s = sum(linespace)
    n = len(linespace)
    media = s / n
    std = 1 / (n - 1) * sum([(media - x) ^ 2 for x in linespace])
    print s, n, media, std

if __name__ == '__main__':
    # messages = get_column('topcomments.tab', 'comment_message')
    # pprint(word_histogram(messages))
    likes = get_column('topcomments.tab', 'comment_like_count', lambda x: int(x))
    pprint(likes)
    remove_outliers(likes)
