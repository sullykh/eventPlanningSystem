'''The Event class has a name, organizer, and description,
and it also has a list of invitees and a menu. The class has
 methods to add invitees and view the list of invitees.'''
class Event:
    def __init__(self, name, organizer, description):
        self.name = name
        self.organizer = organizer
        self.description = description
        self.invitees = []
        self.menu = Menu()

    def add_invitee(self, invitee):
        self.invitees.append(invitee)

    def view_invitees(self):
        for invitee in self.invitees:
            print(invitee)

'''The Invitee class has a name, RSVP status, whether or not
 they are bringing a plus one, and any dietary requirements.
 The class has a __str__ method that formats the
  invitee's information into a human-readable string.'''
class Invitee:
    def __init__(self, name, rsvp=False, plus_one=False, dietary_req=None):
        self.name = name
        self.rsvp = rsvp
        self.plus_one = plus_one
        self.dietary_req = dietary_req

    def __str__(self):
        return f"Name: {self.name}, RSVP: {'Yes' if self.rsvp else 'No'}, Plus One: {'Yes' if self.plus_one else 'No'}, Dietary Requirements: {self.dietary_req}"


'''The Menu class has a dictionary of items, where each
 item is a meal and the value is a list of invitees. 
 The class has methods to add items and view the menu.'''
class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, meal, invitees):
        self.items[meal] = invitees

    def view_menu(self):
        for meal, invitees in self.items.items():
            print(f"{meal}: {', '.join(invitees)}")

'''The EventFactory class has methods to create events and invitees.'''
class EventFactory:
    def create_event(self, name, organizer, description):
        return Event(name, organizer, description)

    def create_invitee(self, name, rsvp=False, plus_one=False, dietary_req=None):
        return Invitee(name, rsvp, plus_one, dietary_req)


'''The EventView class has methods to create events, 
add invitees, view the list of invitees, add menu items,
 and view the menu. The class uses an EventFactory
  object to create events and invitees.'''
class EventView:
    def __init__(self, event_factory):
        self.event_factory = event_factory
        self.events = []

    def create_event(self):
        name = input("Enter event name: ")
        organizer = input("Enter organizer name: ")
        description = input("Enter event description: ")
        event = self.event_factory.create_event(name, organizer, description)
        self.events.append(event)
        print(f"Event {name} created successfully!")

    def add_invitee(self):
        event_name = input("Enter event name: ")
        event = next((x for x in self.events if x.name == event_name), None)
        if event:
            name = input("Enter invitee name: ")
            rsvp = input("Has invitee RSVPd? (y/n)").lower() == "y"
            plus_one = input("Is invitee bringing a plus one? (y/n)").lower() == "y"
            dietary_req = input("Enter invitee dietary requirements: ")
            invitee = self.event_factory.create_invitee(name, rsvp, plus_one, dietary_req)
            event.add_invitee(invitee)
            print(f"Invitee {name} added to event {event_name}")
        else:
            print(f"Event {event_name} not found.")

    def view_invitees(self):
        event_name = input("Enter event name: ")
        event = next((x for x in self.events if x.name == event_name), None)
        if event:
            event.view_invitees()
        else:
            print(f"Event {event_name} not found.")

    def add_menu_item(self):
        event_name = input("Enter event name: ")
        event = next((x for x in self.events if x.name == event_name), None)
        if event:
            meal = input("Enter meal name: ")
            invitees = input("Enter invitees (comma separated): ").split(",")
            event.menu.add_item(meal, invitees)
            print(f"Meal {meal} added to event {event_name}")
        else:
            print(f"Event {event_name} not found.")

    def view_menu(self):
        event_name = input("Enter event name: ")
        event = next((x for x in self.events if x.name == event_name), None)
        if event:
            event.menu.view_menu()
        else:
            print(f"Event {event_name} not found.")

    def search_invitee(self):
        invitee_name = input("Enter invitee name: ")
        for event in self.events:
            invitee = next((x for x in event.invitees if x.name == invitee_name), None)
            if invitee:
                print(f"Invitee {invitee_name} found in event {event.name}")
                print(f"RSVP: {invitee.rsvp}")
                print(f"Plus One: {invitee.plus_one}")
                print(f"Dietary Requirements: {invitee.dietary_req}")
                return
        print(f"Invitee {invitee_name} not found.")


def main():
    event_factory = EventFactory()
    event_view = EventView(event_factory)
    while True:
        print("1. Create Event")
        print("2. Add Invitee")
        print("3. View Invitees")
        print("4. Add Menu Item")
        print("5. View Menu")
        print("6. Search Invitee")
        print("7. Exit")
        choice = input("Enter your choice: ")
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
            event_view.search_invitee()
        elif choice == "7":
            break


if __name__ == "__main__":
    main()
