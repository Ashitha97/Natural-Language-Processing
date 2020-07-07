# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:42:55 2020

@author: Ashitha A Nair
"""

import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from string import punctuation
stop_nltk=stopwords.words('english')



#This fucntion is used for cleaning and getting the pos tag
def clean_postag(text):    
    text=text.lower()
    #Taking out Noun and Verb for comparison word based
    tokens = nltk.word_tokenize(text)
    tokens=[text for text in tokens if text not in stop_nltk]
    tokens=[text for text in tokens if text not in list(punctuation)]
    pos = nltk.pos_tag(tokens)
    #pos = [p for p in pos if p[1].startswith('N') or p[1].startswith('V')]     
    return pos



#function is used to get the synonymns of the word
def synonym(text):
    tokens= clean_postag(text)
    l=[]
    for synset,i in tokens:
        l.append(synset)
    l1=[]
    for text in l:
        l1.append((wn.synsets(text)))
        print(text)
    return l1



#use to find the definition of the given word
def findDefinition(text):
    tokens=clean_postag(text)
    for i,k in tokens:
        print(i)
        print(wn.synsets(i))
        for l in range(len(wn.synsets(i))):
            rsp = wn.synsets(i)[l].definition()
            examp=wn.synsets(i)[l].examples()
            names=wn.synsets(i)[l].lemmas()
            print("Lemma:",names)
            print("Definition:",rsp)
            if(len(examp)>0):
                print("Examples are given below")
                print(*examp[:2],sep=" ")
            else:
                print("No example found")
        print("__________"*10)


#used to find the antonyms of the given word
def findAntonyms(text):
    synonyms=[]
    antonyms=[]
    tokens=clean_postag(text)
    for i,k in tokens:
        print(i)
        for syn in wn.synsets(i):
            for l in syn.lemmas():
                synonyms.append(l.name())
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
                    print('synonyms are:',synonyms)
                    print("Antonyms are:",antonyms)
        
                    
def main():
    clean_pos=clean_postag('the world is so cruel and even more beatiful')
    defi=findDefinition('world is bad')
    print('This is clean_pos:',clean_pos)
    print('These are:',defi)


if __name__== "__main__":
    main()    