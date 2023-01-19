'''The Event class has a name, organizer, and description,
and it also has a list of invitees and a menu. The class has
 methods to add invitees and view the list of invitees.'''
class Event:
    def __init__(self, name, organizer, description):
        self.name = name  # Assign the parameter "name" to the instance variable "name"
        self.organizer = organizer # Assign the parameter "organizer" to the instance variable "organizer"
        self.description = description  # Assign the parameter "description" to the instance variable "description"
        self.invitees = [] # Create an empty list and assign it to the instance variable "invitees"
        self.menu = Menu() #Yus need to add comment
        self.track_invitee_meals = {} #Yus to add comment

    def add_invitee(self, invitee):
        self.invitees.append(invitee)  # Add the parameter "invitee" to the list stored in the instance variable "invitees"

    def view_invitees(self):
        for invitee in self.invitees: # Iterate through the list stored in the instance variable "invitees"
            print(invitee) # Print each invitee

'''The Invitee class has a name, RSVP status, whether or not
 they are bringing a plus one, and any dietary requirements.
 The class has a __str__ method that formats the
  invitee's information into a human-readable string.'''
class Invitee:
    def __init__(self, name, rsvp=False, plus_one=False, dietary_req=None):
        self.name = name  # Assign the parameter "name" to the instance variable "name"
        self.rsvp = rsvp # Assign the parameter "rsvp" to the instance variable "rsvp" with a default value of False
        self.plus_one = plus_one  # Assign the parameter "plus_one" to the instance variable "plus_one" with a default value of False
        self.dietary_req = dietary_req # Assign the parameter "dietary_req" to the instance variable "dietary_req" with a default value of None

    def __str__(self):
        return f"Name: {self.name}, RSVP: {'Yes' if self.rsvp else 'No'}, Plus One: {'Yes' if self.plus_one else 'No'}, Dietary Requirements: {self.dietary_req}"


'''The Menu class has a dictionary of items, where each
 item is a meal and the value is a list of invitees. 
 The class has methods to add items and view the menu.'''
class Menu:
    def __init__(self):
        self.items = [] # Create an empty list and assign it to the instance variable "items"

    def add_item(self, meal):
        self.items.append(meal) # Add the parameter "meal" to the list stored in the instance variable "items"

    def view_menu(self):
        for meal in self.items:
            print(meal)

'''The EventFactory class has methods to create events and invitees.'''
from abc import ABC, abstractmethod

class ICreateFactory(ABC):  #An interface for Event Factory. two functions are passed down to the subclass. 
    @abstractmethod
    def create_event():
        pass
    def create_invitee():
        pass

class EventFactory(ICreateFactory):
    def create_event(self, name, organizer, description):
        return Event(name, organizer, description) # creates and returns an Event object with the given name, organizer, and description.


    def create_invitee(self, name, rsvp=False, plus_one=False, dietary_req=None):
        return Invitee(name, rsvp, plus_one, dietary_req) # creates and returns an Invitee object with the given name, rsvp, plus_one, and dietary_req.


'''The EventView class has methods to create events, 
add invitees, view the list of invitees, add menu items,
 and view the menu. The class uses an EventFactory
  object to create events and invitees.'''
class EventView:
    def __init__(self, event_factory):
        self.event_factory = event_factory # Assign the parameter "event_factory" to the instance variable "event_factory"
        self.events = [] # Create an empty list and assign it to the instance variable "events"

    def create_event(self):
        name = input("Enter event name: ") # Prompt the user for input and assign it to the variable "name"
        organizer = input("Enter organizer name: ") # Prompt the user for input and assign it to the variable "organizer"
        description = input("Enter event description: ") # Prompt the user for input and assign it to the variable "description"
        event = self.event_factory.create_event(name, organizer, description) # Create an Event object using the "event_factory" instance variable and the input from the user
        self.events.append(event) # Add the newly created event object to the list stored in the "events" instance variable
        print(f"Event {name} created successfully!") # Print a message confirming the event has been created

    def addPlusOne(self,event_name):
        event = next((x for x in self.events if x.name == event_name), None) # Iterate through the list stored in the instance variable "events" and return the first event object whose "name" attribute matches the parameter "event_name" or return None
        if event:
            name = input("\nEnter Plus one invitee name: ") # Prompt the user for input and assign it to the variable "name"
            rsvp = input("Has Plus one invitee RSVPd? (y/n)").lower() == "y" # Prompt the user for input, convert it to lowercase, and check if it is equal to "y" and assign the boolean value to "rsvp"
            dietary_req = input("Enter invitee dietary requirements: ") # Prompt the user for input and assign it to the variable "dietary_req"
            invitee = self.event_factory.create_invitee(name, rsvp, False, dietary_req) # Create an Invitee object using the "event_factory" instance variable and the input from the user, with the plus_one attribute set to true
            event.add_invitee(invitee) # Add the newly created invitee object to the list of invitees of the event
            print(f"Invitee {name} added to event {event_name} as plus One") # Print a message confirming the invitee has been added as plus one
        else:
            print(f"Event {event_name} not found.") # Print an error message if the event is not found

    def add_invitee(self):
        event_name = input("Enter event name: ") # Prompt the user for input and assign it to the variable "event_name"
        event = next((x for x in self.events if x.name == event_name), None) # Iterate through the list stored in the instance variable "events" and return the first event object whose "name" attribute matches the input event_name or return None
        if event:
            name = input("Enter invitee name: ") # Prompt the user for input and assign it to the variable "name"
            rsvp = input("Has invitee RSVPd? (y/n)").lower() == "y" # Prompt the user for input, convert it to lowercase, and check if it is equal to "y" and assign the boolean value to "rsvp"
            dietary_req = input("Enter invitee dietary requirements: ") # Prompt the user for input and assign it to the variable "dietary_req"
            plus_one = input("Is invitee bringing a plus one? (y/n)").lower() == "y" # Prompt the user for input, convert it to lowercase, and check if it is equal to "y" and assign the boolean value to "plus_one"
            if plus_one:
                self.addPlusOne(event_name) # If the invitee is bringing a plus one, call the addPlusOne method and pass the event_name
            invitee = self.event_factory.create_invitee(name, rsvp, plus_one, dietary_req) # Create an Invitee object using the "event_factory" instance variable and the input from the user
            event.add_invitee(invitee) # Add the newly created invitee object to the list of invitees of the event
            print(f"Invitee {name} added to event {event_name}") # Print a message confirming the invitee has been added
        else:
            print(f"Event {event_name} not found.") # Print an error message if the event is not found

    def view_invitees(self):
        event_name = input("Enter event name: ")  # Prompt the user for input and assign it to the variable "event_name"
        event = next((x for x in self.events if x.name == event_name), None) # Iterate through the list stored in the instance variable "events" and return the first event object whose "name" attribute matches the input event_name or return None
        if event:
            event.view_invitees() # call the view_invitees method on the event object
        else:
            print(f"Event {event_name} not found.") # Print an error message if the event is not found

    def add_menu_item(self):
        event_name = input("Enter event name: ") # Prompt the user for input and assign it to the variable "event_name"
        event = next((x for x in self.events if x.name == event_name), None)
        if event:
            meal = input("Enter meal name: ") # Prompt the user for input and assign it to the variable "meal"
            event.menu.add_item(meal)
            print(f"Meal {meal} added to event {event_name}")  # Print a message confirming the meal has been added
        else:
            print(f"Event {event_name} not found.") # Print an error message if the event is not found

    def view_menu(self):
        event_name = input("Enter event name: ") # Prompt the user for input and assign it to the variable "event_name"
        event = next((x for x in self.events if x.name == event_name), None) #needs commenting
        if event:
            event.menu.view_menu()
        else:
            print(f"Event {event_name} not found.") # Print an error message if the event is not found

    def search_invitee(self):
        invitee_name = input("Enter invitee name: ") # Prompt the user for input and assign it to the variable "invitee_name"
        for event in self.events:  # Iterate through the list stored in the instance variable "events"
            invitee = next((x for x in event.invitees if x.name == invitee_name), None) # Iterate through the list of invitees of the event and return the first invitee object whose "name" attribute matches the input invitee_name or return None
            if invitee:
                print(f"Invitee {invitee_name} found in event {event.name}") # Print a message with the event name where the invitee is found
                print(f"RSVP: {invitee.rsvp}") # Print the invitee RSVP status
                print(f"Plus One: {invitee.plus_one}") # Print the invitee plus one status
                print(f"Dietary Requirements: {invitee.dietary_req}") # Print the invitee dietary requirements
                return
        print(f"Invitee {invitee_name} not found.") # Print an error message if the invitee is not found

    def view_events(self):
        for event in self.events: 
            print(event.name) #Print out all the events stored in self.events. 

    def select_menu(self):
        event_name = input("Enter event name: ") # Prompt the user for input and assign it to the variable "event_name"
        event = next((x for x in self.events if x.name == event_name), None)
        if event:
            invitee_name = input("Enter your name : ") #If the event exists, prompt the user for input and assign it to the variable "invitee_name"
            for event in self.events: 
                invitee = next((x for x in event.invitees if x.name == invitee_name), None) 
                if invitee: #If the event exists in the list of events and if the list of invitee contains the variable invitee_name, start the while loop.
                    while True : #The while loop will not end unless something returns False
                        if len(event.menu.items) > 0 : #If the length of an item list is more than 0, continue. 
                                    meal_name = input("What are you having? : ") #Prompt the user for input and assign it to the variable meal_name
                                    if meal_name in event.menu.items: #If the given meal_name from the invitee is in the menu, order is successful and the invitee_name and the ordered meal get stored.
                                        event.track_invitee_meals[invitee_name] = meal_name
                                        print("Ordered Successfully")
                                        return False
                                    else:
                                        print(f"{meal_name} not found. try again.") # Print an error message if the meal name is not found
                                        return True
                        else:
                            print("Add menu before selecting menu.") # Print a prompt message to add menu item before selcting  a menu
                            return False
                else :
                    print(f"{invitee_name} is not in the invitee_list") # Print an error message if the invitee is not in the invitee list
        else:
            print(f"Event {event_name} not found.") # Print an error message if the event is not found
    
    def track_meals(self):
        event_name = input("Enter event name: ") #Prompt the user for input and assign it to the variable event_name
        event = next((x for x in self.events if x.name == event_name), None)
        if event: #If the event exists, Go through the dictionary of track_invitee_meals using for loop. 
            for invitee, meal in event.track_invitee_meals.items():
                print(f"{invitee}: {meal}") #Print out the result of track_invitee_meals
        else:
            print(f"Event {event_name} not found.")

def main():
    # Create an instance of the EventFactory class
    event_factory = EventFactory()
    # Create an instance of the EventView class, passing in the event_factory object
    event_view = EventView(event_factory)
    # Run a loop to display menu options to the user
    while True:
        print("1. Create Event")
        print("2. Add Invitee")
        print("3. View Invitees")
        print("4. Add Menu Item")
        print("5. View Menu")
        print("6. Select menu")
        print("7. Search Invitee")
        print("8. View events")
        print("9. Track meals")
        print("10. Exit")
        # Get the user's choice of menu option
        choice = input("Enter your choice: ")
        # Check the user's choice and call the corresponding method from the event_view object
        if choice == "1":
            event_view.create_event()
        elif choice == "2":
            event_view.add_invitee()
        elif choice == "3":
            event_view.view_invitees()
        elif choice == "4":
            event_view.add_menu_item()
        elif choice == "5":
            event_view.view_menu()
        elif choice == "6":
            event_view.select_menu()
        elif choice == "7":
            event_view.search_invitee()
        elif choice == "8":
            event_view.view_events()
        elif choice == "9":
            event_view.track_meals()
        elif choice == "10":
            # Exit the loop if the user chooses the "Exit" option
            break


if __name__ == "__main__":
     # Check if the script is being run as the main program
     # If so, call the main() function
    main()
