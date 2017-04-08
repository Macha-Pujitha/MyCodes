'''
#Uncomment this to download nltk database
import nltk
nltk.download()
'''

from nltk.corpus import wordnet as wn
import pyttsx
import webbrowser
import time
def black(n, inputt_array_copy, word_array_copy, whites):
    blacks = 0
    #print(word_array_copy)
    #print("hi")
    for i in range (0,n):
        for j in range(0,n):
            if(word_array_copy[i]!='*'):
             if(word_array_copy[i]==inputt_array_copy[j]):
                inputt_array_copy[j]='$'
                #print("hi")
                #print(word_array_copy)
               # print(inputt_array_copy)
                break
    for i in range(0,n):
        if(inputt_array_copy[i]=='$'):
            blacks+=1
    print blacks, "B ",whites,"W"
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
def definition(syns):
    print "DEFINITION"
    print(syns[0].definition())
def TextToSpeech(Pronounce):
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-85)
    engine.say(Pronounce)
    engine.runAndWait()
def synonyms(inputt, syns):
    synonyms = syns[0].lemmas()[0].name()
    #syn =[str(lemma.name()) for lemma in wn.synset('dog.n.01').lemmas()]
    #print(syn)
    if synonyms == inputt:
        pass
    else:
        print "SYNONYMS"
        print synonyms
def examples(syns):
    examples = syns[0].examples()
    n = len(examples)
    if examples == []:
        pass
    else:
        print"EXAMPLES"
        if n==1:
            print examples[0]
        else:
            for i in range(0,n):
                print i+1,". ",examples[i]
    time.sleep(10)
def ConnectToWeb(inputt):
    new = 2 #for a new tab
    url = "http://www.ipicthat.com/index.php?m=dictionary&t=az&w="+inputt
    #print(url)
    webbrowser.open(url,new=new)

def vocab(inputt):
    syns = wn.synsets(inputt)
    definition(syns)
    TextToSpeech(inputt)
    TextToSpeech(syns[0].definition())
    synonyms(inputt, syns)
    examples(syns)
    ConnectToWeb(inputt)
word = raw_input("to guess?")
n = len(word)
word_array = list(word)
count = 0
var = 1
while var:
    count+=1
    inputt = raw_input("Guess " + str(n)+ " letter word?")
    if len(inputt)!=n:
        print "OOPS! Enter only ",n, " digit word"
        continue
    inputt_array = list(inputt)
    if inputt == word:
        print "You made it in ",count," attempts"
        var = 0
    else:
        #print(word_array)
        word_array_copy=list(word_array)
        inputt_array_copy=list(inputt_array)
        whites(n,word_array_copy,inputt_array_copy)

vocab(inputt)
