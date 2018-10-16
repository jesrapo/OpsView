'''
    File name: Person.py
    Author: Jesse Rapoport
    Date created: 10/15/2018
    Date last modified: 10/15/2018
    Python Version: 2.7.12
    Created for OpsView
'''

class Person:
    """A class of Persons who are potential candidates for OpsView"""
    
    def set_name(self, name):
        #sets the name of the current Person
        
        self.name = name

    def set_description(self, description):
        #sets the description of the current Person
        
        self.description = description

    def set_characteristics(self, characteristics):
        #sets the characteristics of the current Person
        
        self.characteristics = characteristics

    def compare_characteristics(self, other_characteristics):
        #compare external characteristics with the characteristics of the current Person

        percentage_similar = 0

        #percentage that they're the same, starting at 0

        
        for i, current in enumerate(self.characteristics, start=0):
            if(self.characteristics[i] == other_characteristics[i]):
                #percentage goes up 10% each time, because there are 10 questions
                percentage_similar += 10

                
        self.similarity = percentage_similar
        #set the similarity of the current Person to the one just calculated

