
# Allow users to create multiple events = create a class for <Events>. 
#Events attributes : event_name, a name of an organiser, event_description, an array for invited people.

#track whether or not each invitee has RSVP, whether or not if they are bringing a plus one. 
# + track whether they have any dietary or other requirements

#create a class for <invitee> ? 
#Inviteee attributes : name, gender, plusOne(boolean), dietary / requirements, meals? 

#Create a class for <set meal> 
#set meal attributes : meal name etc

from abc import ABC, abstractmethod

class SetMeal(ABC):
    @abstractmethod
    def get_drink(self):
        pass
    
    @abstractmethod
    def get_starter(self):
        pass

    @abstractmethod
    def get_main(self):
        pass

    @abstractmethod
    def get_desert(self):
        pass

class Invitee(ABC):
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender=gender
        self.plusOne = False
        self.plusOne_name = ""
        self.dietary_requirements = False
    
    @abstractmethod
    def set_plus_one(self):
        pass

    @abstractmethod
    def set_dietary_requirements(self):
        pass

class Rich_Invitee(Invitee):
    def set_plus_one(self,name):
        self.plusOne = True
        self.plusOne_name = name
        print("Im Rich")

    def set_dietary_requirements(self):
        self.dietary_requirements = True

class Standard_Invitee(Invitee):
    def set_plus_one(self,name):
        self.plusOne = True
        self.plusOne_name = name

    def set_dietary_requirements(self):
        self.dietary_requirements = True

class StandardSetMeal(SetMeal):
    def get_drink(self):
        print("Coke")
        #Print out a name of the drink here

    def get_starter(self):
        print("Chips")
        #Print out a name of the starter here

    def get_main(self):
        print("Cheese Burger")
        #print out a name of the main here

    def get_desert(self):
        print("Pudding")
        #print out a name of the desert here


class LuxurySetMeal(SetMeal):
    def get_drink(self):
        print("Wine")
        #Print out a name of the drink here

    def get_starter(self):
        print("Caesar Salad")
        #Print out a name of the starter here

    def get_main(self):
        print("Sirloin Steak")
        #print out a name of the main here

    def get_desert(self):
        print("Creme Brulee")
        #print out a name of the desert here


class EventFactory(ABC):
    def __init__(self,title,organizer,description):
        self.title = title
        self.organizer = organizer
        self.description = description
        self.invitees = []

    @abstractmethod
    def get_set_meal(self):
        pass

    @abstractmethod
    def get_invitee(self):
        pass

    @staticmethod
    def add_invitee(self,name):
        self.invitees.append(name)
        

class ExpensiveEventFactory(EventFactory):
    def get_set_meal(self) -> SetMeal:
        return LuxurySetMeal()

    def get_invitee(self,name,age,gender) -> Invitee:
        self.invitees.append(name)
        return Rich_Invitee(name,age,gender)

    def add_invitee(name):
        EventFactory.add_invitee(name)

class CheapEventFactory(EventFactory):
    def get_set_meal(self) -> SetMeal:
        return StandardSetMeal()

    def get_invitee(self,name,age,gender) -> Invitee:
        self.invitees.append(name)
        return Standard_Invitee(name,age,gender)

    def add_invitee(name):
        EventFactory.add_invitee(name)


#------------What users can do ----------------------------------------------------

def createEvent(event_type : str,title,organizer,description):
    factories = {
        "Expensive" : ExpensiveEventFactory(title,organizer,description),
        "Cheap" : CheapEventFactory(title,organizer,description)
    }
    event = factories[event_type]
    return event

    
def select_Meal(meal_type:str):
    meals = {
        "Standard" : StandardSetMeal(),
        "Luxury" : LuxurySetMeal()
    }
    set_meal = meals[meal_type]
    return set_meal


def invite(person_type:str,name,age,gender):
    invitee_type = {
        "Rich" : Rich_Invitee(name,age,gender),
        "Standard" : Standard_Invitee(name,age,gender)
    }

    invitee = invitee_type[person_type]
    return invitee