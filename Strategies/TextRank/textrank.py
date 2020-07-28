# Used code (modified): https://towardsdatascience.com/textrank-for-keyword-extraction-by-python-c0bae21bcec0

from collections import OrderedDict, Counter
import statistics
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as en_STOP_WORDS
from spacy.lang.nl.stop_words import STOP_WORDS as nl_STOP_WORDS
import en_core_web_sm
import nl_core_news_sm
import pandas as pd

ensp = en_core_web_sm.load()
nlsp = nl_core_news_sm.load()

class TextRank4Keyword():
    """Extract keywords from text"""
    
    def __init__(self):
        self.d = 0.85 # damping coefficient, usually is .85
        self.min_diff = 1e-5 # convergence threshold
        self.steps = 10 # iteration steps
        self.node_weight = None # save keywords and its weight

    def set_stopwords(self, stopwords, langTag):  
        """function set_stopwords : sets stopwords

        Args: 
            stopwords: list of words that will be excluded as possible keywords
            langTag (string): the language of the words in wordList and the synonyms (e.g. 'eng' for English and 'nld' for Dutch)
        
        """
        if langTag == "en":
            for word in en_STOP_WORDS.union(set(stopwords)):
                lexeme = ensp.vocab[word]
                lexeme.is_stop = True
        elif langTag == "nl":
            for word in nl_STOP_WORDS.union(set(stopwords)):
                lexeme = nlsp.vocab[word]
                lexeme.is_stop = True            
    
    def sentence_segment(self, doc, candidate_pos, lower):
        """Store those words only in cadidate_pos"""
        """function sentence_segment : only store words with wanted pos tags

        Args: 
            candidate_pos: pos tags which serve as possible candidates, typically ['NOUN', 'PROPN']
            lower (boolean): should keywords be lowercased or not?

        Returns:
            list of lists: one list per sentence with single words as strings
        """
        sentences = []
        for sent in doc.sents:
            selected_words = []
            for token in sent:
                # Store words only with candidate POS tag
                if token.pos_ in candidate_pos and token.is_stop is False:
                    if lower is True:
                        selected_words.append(token.text.lower())
                    else:
                        selected_words.append(token.text)
            sentences.append(selected_words)
        return sentences
        
    def get_vocab(self, sentences):
        """function get_vocab : creates a vocabulary dictionary

        Args:
            sentences ([list of lists of strings]): single words from a sentence in a list of lists

        Returns:
            dictionary {"word":frequency}: dictionary with words and their frequency
        """
        vocab = OrderedDict()
        i = 0
        for sentence in sentences:
            for word in sentence:
                if word not in vocab:
                    vocab[word] = i
                    i += 1
        return vocab
    
    def get_token_pairs(self, window_size, sentences):
        """Build token_pairs from windows in sentences"""
        """function get_token_pairs : 
        Args:
            window_size: integer, defines 
            sentences: list of lists with words per sentence
        Returns:
            list of tuples [("word", sentence index)]: 
        """
        token_pairs = list()
        for sentence in sentences:
            for i, word in enumerate(sentence):
                for j in range(i+1, i+window_size):
                    if j >= len(sentence):
                        break
                    pair = (word, sentence[j])
                    if pair not in token_pairs:
                        token_pairs.append(pair)
        return token_pairs
        
    def symmetrize(self, matrix):
        """function symmetrize : symmetrizes the matrix

        Args:
            matrix (list of lists): list of lists

        Returns:
            matrix (list of lists): symmetrized matrix
        """
        return matrix + matrix.T - np.diag(matrix.diagonal())
    
    def get_matrix(self, vocab, token_pairs):
        """function get_matrix : builds a normalized matrix with the vocabulary and possible keywords
        
        Args:
            vocab: dictionary with words and their frequency
            token_pairs: list of tuples with words and their sentence (by index)
        Returns:
            list of lists (matrix)
        """
        # Build matrix
        vocab_size = len(vocab)
        g = np.zeros((vocab_size, vocab_size), dtype='float')
        for word1, word2 in token_pairs:
            i, j = vocab[word1], vocab[word2]
            g[i][j] = 1
            
        # Get Symmeric matrix
        g = self.symmetrize(g)
        
        # Normalize matrix by column
        norm = np.sum(g, axis=0)
        g_norm = np.divide(g, norm, where=norm!=0) 
        
        return g_norm

    
    def get_keywords(self, number=10):
        """function get_keywords : extracts the keywords with the highest scores
        Args:
            number: maximum number of keywords extracted
        Returns:
            keyword_list {"keyword":score}: dictionary with keywords and their scores
        """
        keyword_list = {}
        node_weight = OrderedDict(sorted(self.node_weight.items(), key=lambda t: t[1], reverse=True))
        if node_weight == OrderedDict():
            return keyword_list
        for i, (key, value) in enumerate(node_weight.items()):
            keyword_list[key] = str(value)
            if i == len(node_weight.items())-1:
                return keyword_list
            elif i > number:
                return keyword_list
            
        
        
    def analyze(self, text, langTag,
                candidate_pos=['NOUN', 'PROPN'], 
                window_size=4, lower=False, stopwords=list()
                ):
        """function analyze : main function to analyze a text and calculates the weighting of keywords

        Args:
            text (string): string to be analyzed (e.g. abstract)
            langTag (string): the language of the words in wordList and the synonyms (e.g. 'eng' for English and 'nld' for Dutch)
            candidate_pos (list, optional): the pos tags that are suitable candidates. Defaults to ['NOUN', 'PROPN'].
            window_size (int, optional): window size (dependency range). Defaults to 4.
            lower (bool, optional): lowercases all words or not. Defaults to False.
            stopwords ([type], optional): the list of excluded words. Defaults to list().
        """
        # Set stop words
        self.set_stopwords(stopwords, langTag)
        
        # Pare text by spaCy
        if langTag == "en":
            doc = ensp(text)
        elif langTag == "nl":
            doc = nlsp(text)
        
        # Filter sentences
        sentences = self.sentence_segment(doc, candidate_pos, lower) # list of list of words
        
        # Build vocabulary
        vocab = self.get_vocab(sentences)
        
        # Get token_pairs from windows
        token_pairs = self.get_token_pairs(window_size, sentences)
        
        # Get normalized matrix
        g = self.get_matrix(vocab, token_pairs)
        
        # Initionlization for weight(pagerank value)
        pr = np.array([1] * len(vocab))
        
        # Iteration
        previous_pr = 0
        for epoch in range(self.steps):
            pr = (1-self.d) + self.d * np.dot(g, pr)
            if abs(previous_pr - sum(pr))  < self.min_diff:
                break
            else:
                previous_pr = sum(pr)

        # Get weight for each node
        node_weight = dict()
        for word, index in vocab.items():
            node_weight[word] = pr[index]
        
        self.node_weight = node_weight

def textrank_keywords(abstract, langTag):
    """function textrank_keywords : main function to automatically extract keywords from an abstract with TextRank and 
    normalizes them between 0 and 1

   Args:
       abstract (string): an abstract (or paper) as a string
       langTag (string): the language of the words in wordList and the synonyms (e.g. 'eng' for English and 'nld' for Dutch)

   Returns:
       Counter(normalized_scores) {"keyword":score}: dictionary with keywords and their score
    """
    tr4w = TextRank4Keyword()
    tr4w.analyze(abstract, langTag, candidate_pos = ['NOUN', 'PROPN'], window_size=4, lower=False)
    score_dict = tr4w.get_keywords(10)
    scores = [float(score_dict[key]) for key in score_dict.keys()]
    if scores == []:
        return score_dict
    else:
        mean = statistics.mean(scores)
        stdev = statistics.stdev(scores)
        normalized_scores = {key:(float(value)-mean)/stdev for (key,value) in score_dict.items()}
        normalized_scores = {key:value/5+.5 for (key,value) in normalized_scores.items()}
        return Counter(normalized_scores)