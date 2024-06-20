# Task 1: Vehicle Registration System:

class Vehicle(): # Creating our class
    def __init__(self, reg_num, type, owner): # Creating instances of our Vehicle class using __init__. The function always takes in self as the first parameter.
        self.registration_number = reg_num # Using self.<instance> and assigning it to each instance we've created.
        self.type = type
        self.owner = owner

    def change_owner(self): # Always take in the parameter self.
        new_owner = input("What is the name of the new owner? ") # Asks the user for the new owner.
        self.owner = new_owner # Asssigning the user input (new_owner) to our variable self.owner.
        print(f"The new owner's name is {self.owner}.") # Printing out a statement displaying the new owner so it is readable to the user.

Vehicle1 = Vehicle("1234", "Sedan", "John Smith") # Creating a value to store inside our Vehicle class.

Vehicle1.change_owner() # Calling our new_owner funciton to display the new owner of the vehicle.

# Task 2: Event Management System Enhancement:

class Event(): # Creating our class
    def __init__(self, name, date, participants=0): # Creating our __init__ function to create instances for our Event class. Self is always the first parameter.
        self.name = name
        self.date = date
        self.participants = participants
    
    def add_participant(self):
        new_participant = input("What is the name of the new participant? ") # Asks the user for the new participant
        self.participants += 1 # Adds 1 to our participants count which starts at 0 by default.
        print(f"Since {new_participant} arrived, We now have {self.participants} participant(s) in our event!")

    def get_participant_count(self):
        print(f"There are {self.participants} participants in this event!") # The value of our participants count is stored inside self.participants. This f string prints out the value of self.participants inside a sentance that is readable to the user.

participant1 = Event("Dustin Pedroia", "6/18/2024") # Storing a value of a participant inside of our Event class.

participant1.add_participant() # Calling our add_participant() function with our participant value we created.
participant1.get_participant_count() # Calling our get_participant_count() function with our participant value we created.