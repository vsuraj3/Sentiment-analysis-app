import pickle
import pandas as pd

data = pd.read_csv("HindiSentiWordnet.txt", delimiter=' ')

fields = ['POS_TAG', 'ID', 'POS', 'NEG', 'LIST_OF_WORDS']

#Creating a dictionary which contain a tuple for every word. Tuple contains a list of synonyms,
# positive score and negative score for that word.
words_dict = {}
for i in data.index:
    # print (data[fields[0]][i], data[fields[1]][i], data[fields[2]][i], data[fields[3]][i], data[fields[4]][i])

    words = data[fields[4]][i].split(',')
    for word in words:
        words_dict[word] = (data[fields[0]][i], data[fields[2]][i], data[fields[3]][i])

file = open('word_dict', 'wb')
pickle.dump(words_dict, file)
file.close()

