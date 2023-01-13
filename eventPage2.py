class Events:
    def __init__(self, name, organiser, description):
        self.name = name
        self.organiser = organiser
        self.description = description # describing the event

    def get_name(self):
        return self.name
class Invitees: 
     def __init__(self, name, plus_one, max_invitees):
        self.name = name
        self.plus_one = plus_one
        self.max_invitees = max_invitees
        self.events = []


     def add_invitees(self, name):
        if len(self.events) < self.max_invitees:
           self.events.append(event)
           return True
        return False

     def get_average_grade(self):
         pass


event1 = Events("Testing", "Jack", "first edition")
event2 = Events("Release", "John","Main release")



