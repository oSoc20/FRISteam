"""
The module containing functions for finding synonyms
"""
import nltk
nltk.download('wordnet')
nltk.download('omw')
from nltk.corpus import wordnet   #Import wordnet from the NLTK
from collections import Counter

def get_synonym_by_word(word, langTag):
   """function get_synonym_by_word: get synonyms from a word in a specified language

   Args:
       word (string): the word to find synonyms for
       langTag (string): the language of the word (e.g. 'eng' for English and 'nld' for Dutch)

   Returns:
       dictionary: Counter dictionary of [synonym_string, frequency_score]
   """
   syn = dict()
   normalize_denom = 0
   for synset in wordnet.synsets(word, lang=langTag):
      for lemma in synset.lemmas(lang=langTag):
         normalize_denom = normalize_denom + 1
         key = lemma.name()
         #add the synonyms + frequency
         if key in syn:
            syn[key] = syn[key] + 1
         else:
            syn[key] = 1   
   syn.pop(word.lower(), None) #remove the original word from the synonym list
   syn = {k: v for k, v in sorted(syn.items(), key=lambda item: item[1], reverse=True)} #sort the dictionary by most frequent synonym
   syn_norm = {k: v/normalize_denom for k, v in syn.items()}
   return Counter(syn_norm)


def get_synonym_by_word_list(wordList, langTag): 
   """function get_synonym_by_word_list : get synonyms from a list of words in a specified language

   Args:
       wordList (list(string)): the list of words to find synonyms for
       langTag (string):  the language of the words in wordList and the synonyms (e.g. 'eng' for English and 'nld' for Dutch)

   Returns:
       list: [list of original words, list of counter dictionaries : [synonym_string, frequency_score] in order of original words]
   """
   synList = list()
   for word in wordList:
      syn = get_synonym_by_word(word, langTag)
      # print("\n Synonym DEBUG: ")
      # print(syn)
      synList.append(syn)
   return [wordList, synList]

#print(get_synonym_by_word("Bad", 'eng', 2))
#print(get_synonym_by_word("Wetenschap", 'nld', 2))
#print(get_synonym_by_word_list(["Bad", "Science", "Life"], 'eng', 2))
#print(get_synonym_by_word_list(["Slecht", "Leven", "Onderzoek"], 'nld', 2))