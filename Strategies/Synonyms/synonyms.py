import nltk
nltk.download('wordnet')
nltk.download('omw')
from nltk.corpus import wordnet   #Import wordnet from the NLTK

def get_synonym_by_word(word, langTag, maxSynonyms): #langTag should be 'eng' for English and 'nld' for dutch
   syn = dict()
   for synset in wordnet.synsets(word, lang=langTag):
      for lemma in synset.lemmas(lang=langTag):
         syn[lemma.name()] = ''   #add the synonyms
   syn.pop(word.lower(), None)
   return list(syn)[:maxSynonyms]


def get_synonym_by_word_list(wordList, langTag, maxSynonyms): #langTag should be 'eng' for English and 'nld' for dutch
   synList = list()
   for word in wordList:
      syn = dict()
      for synset in wordnet.synsets(word, lang=langTag):
         for lemma in synset.lemmas(lang=langTag):
            syn[lemma.name()] = ''   #add the synonyms
      syn.pop(word.lower(), None)
      synList.append(list(syn)[:maxSynonyms])
   return [wordList, synList]

print(get_synonym_by_word("Bad", 'eng', 2))
print(get_synonym_by_word("Wetenschap", 'nld', 2))
print(get_synonym_by_word_list(["Bad", "Science", "Life"], 'eng', 2))
print(get_synonym_by_word_list(["Slecht", "Leven", "Onderzoek"], 'nld', 2))

