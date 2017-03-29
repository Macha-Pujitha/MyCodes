from nltk.corpus import wordnet as wn
import sys
import pandas as pd
#print(wn.all_synsets())
f1 = open('words.txt','wt')
#f2 = open('words.xlsx','wt')
words = [ n for n in wn.all_lemma_names() ]
words = sorted(words)
print(words, file = f1)
#input = sys.argv[1]
#pd.read_csv(input, encoding='utf8', sep=',', dtype='unicode').to_excel('output/' + input + '.xlsx', sheet_name='sheet1', index=False)


