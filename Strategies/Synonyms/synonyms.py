import nltk
nltk.download('wordnet')
nltk.download('omw')
from nltk.corpus import wordnet   #Import wordnet from the NLTK

def get_synonym_by_word(word, langTag, maxSynonyms): #langTag should be 'eng' for English and 'nld' for dutch
   syn = dict()
   for synset in wordnet.synsets(word, lang=langTag):
      for lemma in synset.lemmas(lang=langTag):
         key = lemma.name()
         #add the synonyms + frequency
         if key in syn:
            syn[key] = syn[key] + 1
         else:
            syn[key] = 1   
   syn.pop(word.lower(), None) #remove the original word from the synonym list
   syn = {k: v for k, v in sorted(syn.items(), key=lambda item: item[1], reverse=True)} #sort the dictionary by most frequent synonym
   dictList = [] 
   for key, value in syn.items(): #convert dictionary to list of key-value pairs ([synonym, frequency_score])
      temp = [key,value]
      dictList.append(temp)
   return list(dictList)[:maxSynonyms] #return 'maxSynonyms' number of synonyms


def get_synonym_by_word_list(wordList, langTag, maxSynonyms): #langTag should be 'eng' for English and 'nld' for dutch
   synList = list()
   for word in wordList:
      syn = get_synonym_by_word(word, langTag, maxSynonyms)
      synList.append(syn)
   return [wordList, synList]

print(get_synonym_by_word("Bad", 'eng', 2))
print(get_synonym_by_word("Wetenschap", 'nld', 2))
print(get_synonym_by_word_list(["Bad", "Science", "Life"], 'eng', 2))
print(get_synonym_by_word_list(["Slecht", "Leven", "Onderzoek"], 'nld', 2))

