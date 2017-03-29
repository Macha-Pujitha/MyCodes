#import nltk
#nltk.download()
from nltk.corpus import wordnet as wn
def black(n, inputt_array_copy, word_array_copy, whites):
    blacks = 0
    #print(word_array_copy)
    #print("hi")
    for i in range (0,n):
        for j in range(0,n):
            if(word_array_copy[i]!='*'):
             if(word_array_copy[i]==inputt_array_copy[j]):
                 blacks+=1
                 #print("hi")
                 #print(word_array_copy)
                 # print(inputt_array_copy)
                 break
    print(blacks, "B ",whites,"W")
def whites(n, word_array_copy, inputt_array_copy):
    whites = 0
    #print(inputt_array_copy)
    #print(word_array_copy)
    for i in range(0, n):
        if word_array_copy[i] == inputt_array_copy[i]:
            inputt_array_copy[i] = '*'
            word_array_copy[i]='*'
            whites+=1
    #print(inputt_array_copy)
    blacks = black(n,inputt_array_copy,word_array_copy,whites)

def vocab(inputt):
    syns = wn.synsets(inputt)
    print('\033[1m',"DEFINITION",'\033[0m')
    print(syns[0].definition())
    synonyms = syns[0].lemmas()[0].name()
    #syn =[str(lemma.name()) for lemma in wn.synset('dog.n.01').lemmas()]
    #print(syn)
    if synonyms == inputt:
        pass
    else:
        print('\033[1m',"SYNONYMS",'\033[0m')
        print(synonyms)
    #print(syns)
    antonyms = syns[0].lemmas()[0].antonyms()
    if antonyms:
        print('\033[1m',"ANTONYMS",'\033[0m')
        print(antonyms)
    examples = syns[0].examples()
    n = len(examples)
    if examples == []:
        pass
    else:
        print('\033[1m',"EXAMPLES",'\033[0m')
        if n==1:
            print(examples[0])
        else:
            for i in range(0,n):
                print(i+1,". ",examples[i])

word = input("to guess?")
n = len(word)
word_array = list(word)
count = 0
var = 1
while var:
    count+=1
    inputt = input("Guess " + str(n)+ " letter word?")
    if len(inputt)!=n:
        print("OOPS! Enter only ",n, " digit word")
        continue
    inputt_array = list(inputt)
    if inputt == word:
        print('\033[1m',"You made it in ",count," attempts",'\033[0m')
        var = 0
    else:
        #print(word_array)
        word_array_copy=list(word_array)
        inputt_array_copy=list(inputt_array)
        whites(n,word_array_copy,inputt_array_copy)

vocab(inputt)










