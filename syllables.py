'''
RULES TO COUNT SYLLABLES:
1.If you encounter a vowel increase syllable count(y is considered as a vowel in most cases
only exception is if syllable begins with y i.e when word begins with 'y' or 'y' is between two vowels(ex:yellow))
2.If two or three vowels(or y) are together(example:pie, i and e are together) increment the syllable count only once
for the entire vowel group
3.'e' is considered silent in the following cases:
  a.if the word ends with 'e'(exception:if word ends with 'le' ex: ankle )
     i. Exception to the 'le' rule:if the letter before 'le'(where word ends with 'le') is a vowel then the e is silent
     (example: in scale we have only one syllable, even though word ends with 'le')
  b.word ends with 'ed'(exception:if word ends with 'ted' or 'ded' ex:seated)
  c.word ends ley(lovely)
silent 'e's are not counted for syllables
'''
word = input("enter word")
wlist = list(word)
n = len(word)
count=0
vowel='aeiouy'
#checking for vowels and vowel groups
#count is decremented so that the vowels in a group are not counted more than once
for i in range (0,n):
    if(wlist[i] in vowel):
        if(i<n-1):
            if(wlist[i+1] in vowel):
                if(i<n-2):
                    if(wlist[i+2] in vowel):
                        count-=1
                    else:
                        count-=1
                else:
                    count-=1
        count+=1
if(wlist[0]=='y'):#checking if word begings with y
    count-=1
    if(wlist[1] in vowel):#if we have vowel next to y where y is starting letter we have to increment count
        count+=1
for i in range (1,n-1):
    if(wlist[i]=='y' and wlist[i-1] in vowel and wlist[i+1] in vowel):
        #if y is between two vowels then y will act as a consonant
        count+=1
if(wlist[n-1]=='e'):#checking for words ending with 'e'
    count-=1
    if(wlist[n-3] not in vowel):#to check if word ending with 'le' has a vowel before 'le' example file
      if(wlist[n-2]=='l'):#checking for exception case words ending with 'le'
        count+=1
if(wlist[n-2]=='e' and wlist[n-1]=='d'):#checking for words ending with 'ed'
    count-=1
    if(wlist[n-3] in 'td'):#checking for exception words ending with 'ted' or 'ded'
        count+=1
if(wlist[n-3]=='e' and wlist[n-2]=='l' and wlist[n-1]=='y'):#checking for words ending with 'ely'
    count-=1
print (count)


