#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
Created on Fri Mar 25 09:21:43 2022

@author: joaquingalindo
"""



import requests

class Definitions:
    def __init__(self):
        self.url="https://api.dictionaryapi.dev/api/v2/entries/en/"
    def get_definitions(self, first_list):
        self.words_for_definition = first_list
        self.defintion=[]
        self.separated_definitions_clean=[]
        for i in first_list:
            adder=requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{i}")
            self.defintion.append(adder)

        for b in self.defintion:
            temporal1=""
            for n in b:
                temporal=bytes.decode(n,encoding="utf-8",errors="strict")
                temporal1+=temporal
            self.separated_definitions_clean.append(str(temporal1))

    def clean_definitions(self):
        self.definition_list=[]
        definition_for_moment=[]
        fake_list=[]

        for i in self.separated_definitions_clean:
            adder=i.replace("[","")
            adder1=adder.replace("]","")
            adder2=adder1.replace("'","")
            adder3=adder2.replace('"',"")
            adder4=adder3.replace("{", "")
            adder5=adder4.replace("}", "")
            spliter_variable=adder5.split(":")
            fake_list.append(spliter_variable)

        for i in fake_list:
            definitory=i[1].split(",")
            if definitory[0] == "No Definitions Found":
                definition_for_moment.append("No Definitions For This Word") 
            else:
                ind = i.index("definition")
                definition_for_moment.append(i[ind+1])

        for i in definition_for_moment:
            if i == "No Definitions For This Word":
                self.definition_list.append(i)
            else:
                split_definition=i.replace(",synonyms","")
                self.definition_list.append(split_definition)

    def printer(self):
        print()
        for i in range(len(self.definition_list)):
            print(f"===== {self.words_for_definition[i]} =====")
            print()
            print(self.definition_list[i]) 
            print()