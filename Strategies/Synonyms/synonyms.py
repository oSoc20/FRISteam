"""
The module containing functions for finding synonyms
"""
import nltk
# nltk.download('wordnet')
# nltk.download('omw')
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
   syncounterdict = Counter()
   for synset in wordnet.synsets(word, lang=langTag):
      for lemma in synset.lemmas(lang=langTag):
         key = lemma.name()
         #add the synonyms + frequency
         syncounterdict[key] += 1

   syncounterdict.pop(word.lower(), None) #remove the original word from the synonym list
   
   return syncounterdict


def get_synonym_by_word_list(wordList, langTag, max_nr_synonyms=10): 
   """function get_synonym_by_word_list : get synonyms from a list of words in a specified language

   Args:
       wordList (list(string)): the list of words to find synonyms for
       langTag (string):  the language of the words in wordList and the synonyms (e.g. 'eng' for English and 'nld' for Dutch)
       max_nr_synonyms (int): limits the number of synonyms in the output dictionary 

   Returns:
       counter dictionary : [synonym_string, frequency_score] in order of highest score
   """
   totalsyncounterdict = Counter()
   for word in wordList:
      totalsyncounterdict += get_synonym_by_word(word, langTag)

   normalize_denom = sum(totalsyncounterdict.values())   
   totalsyncounterdict_norm = {k: v/normalize_denom for k, v in totalsyncounterdict.items()}
   normalized_counter_dict = Counter(totalsyncounterdict_norm)
   result_synonyms_dict = Counter()
   ctr = 0
   for keyword, score in normalized_counter_dict.items():
        if ctr < max_nr_synonyms:
            result_synonyms_dict[keyword] = score
            ctr += 1
        else:
            break
   return result_synonyms_dict