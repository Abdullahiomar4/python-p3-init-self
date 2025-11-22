#!/usr/bin/env python3

class Dog:
 
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")


    def get_adopted(self, owner_name):
        self.owner = owner_name




    # testing

fido = Dog("Fido")
snoopy = Dog("Snoopy", "Beagle")

print(fido.name)      
print(fido.breed)     
print(snoopy.name)    
print(snoopy.breed)   


fido.bark()           


fido.get_adopted("Sophie")
print(fido.owner)    
