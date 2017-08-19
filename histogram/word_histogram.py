# -*- coding: utf-8 -*-

from pprint import pprint

def word_histogram(lines):
    hist = {}
    for line in lines:
        for word in line.split(' '):
            # Clean word
            word = ''.join(c for c in word if c.isalnum())
            word = word.lower().strip()

            if word != '':
                hist[word] = 1 if word not in hist else hist[word] + 1

    pairs = zip(hist.iterkeys(), hist.itervalues())
    return sorted(pairs, key=lambda pair: -pair[1])

def get_column(file_path, col_name):
    f = open(file_path, 'r')
    # column names
    columns = f.readline().rstrip('\n').split('\t')
    idx = columns.index(col_name)
    lines = [line.rstrip('\n').split('\t')[idx] for line in f]
    f.close()
    return lines

if __name__ == '__main__':
    messages = get_column('topcomments.tab', 'comment_message')
    pprint(word_histogram(messages))
