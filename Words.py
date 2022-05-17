#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
Created on Fri Mar 25 09:21:43 2022

@author: joaquingalindo
"""




import requests

class Words:
    def __init__(self, lenguage="en"):
        self.lenguage= lenguage
        self.url ="https://random-word-api.herokuapp.com/"
    def How_many_words(self, word):
        self.words=word 
    def get_words(self):
        self.get=requests.get(f"https://random-word-api.herokuapp.com/word?number={self.words}&lang=en")
        for i in self.get:
            self.separated_words=bytes.decode(i,encoding="utf-8",errors="strict") 
    def clean_word_list(self):
        cleaning_words=self.separated_words.replace("[", "")
        cleaning_words1=cleaning_words.replace("]", "")
        cleaning_words2=cleaning_words1.replace('"', "")
        self.clean_list=cleaning_words2.split(",")
        
        return self.clean_list