# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 08:42:20 2019

@author: shindig7
"""
from fuzzywuzzy.fuzz import ratio
import warnings
warnings.filterwarnings("ignore")

class MatchDict(object):
    def __init__(self, word_list):
        self.Words = word_list
        
    def findMostSimilar(self, search_word):
        return sorted(self.Words, key=lambda k: ratio(k, search_word), reverse=True)[0]
    

def main():
    fruit = MatchDict(['cherry', 'pineapple', 'melon', 'strawberry', 'raspberry'])
    print(fruit.findMostSimilar('strawbery'))
    print(fruit.findMostSimilar('berry'))
    
    plang = ['javascript', 'java', 'ruby', 'php', 'python', 'coffeescript']
    plang = MatchDict(plang)
    print(plang.findMostSimilar('jav'))
    print(plang.findMostSimilar('javasit'))
    print(plang.findMostSimilar('cofeescripte'))
    
    
if __name__ == "__main__":
    main()
    
