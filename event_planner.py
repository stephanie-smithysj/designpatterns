
#3 SHOULD BE ABLE TO STORE MENUS OF SET MEALS AND TRACK WHICH INVITEES ARE HAVING WHICH MEALS


import pandas as pd
import os



class MainInvitees():
    def __init__(self):
        return
    
    def event(self):
        event_name = input("Event Name: ")
        guests = pd.DataFrame(columns=['First_Name','Last_Name','RSVP_Status','Dietary Requirements','Starter','Main','Dessert'])
        guests.to_csv(f'{event_name},INVITEES.csv', index=False)
        return event_name

    def add_guest(self):
        p1 = self.event()

        FName = input("First Name: ")
        LName = input("Last Name: ")
        RSVP_Status = input("RSVP Status (yes/no)? ")
        dietary = input("Any Dietary Requirements? ")
        starter = input("Starter Meal: ")
        main = input("Main Meal: ")
        dessert = input("Dessert choice: ")
        plusone = int(input("Plus one (1 - Yes, 2 - No) "))

        
        while FName:

            data = {
                'First_Name': [FName],
                'Last_Name': [LName],
                'RSVP_Status': [RSVP_Status],
                'Dietary Requirements': [dietary],
                'Starter': [starter],
                'Main': [main],
                'Dessert': [dessert]
        
            }

            if plusone == 1:
                FName1 = input("Plus One First Name: ")
                LName1 = input("PLus One Last Name: ")
                dietary1 = input("Plus One Dietary Requirements? ")
                starter = input("Starter Meal: ")
                main = input("Main Meal: ")
                dessert = input("Dessert choice: ")            
                plus1 = {
                    'First_Name': [FName1],
                    'Last_Name': [LName1],
                    'RSVP_Status': 'N/A',
                    'Dietary Requirements': [dietary1],
                    'Starter': [starter],
                    'Main': [main],
                    'Dessert': [dessert]
                }
                self.guests = pd.DataFrame(plus1)
                # append data frame to CSV file
                self.guests.to_csv(f'{p1},INVITEES.csv', mode='a', index=False, header=False)
            


            self.guests = pd.DataFrame(data)
            # append data frame to CSV file
            self.guests.to_csv(f'{p1},INVITEES.csv', mode='a', index=False, header=False)
            
            add_more = int(input("Add Another Guest?(1-YES, 2-NO"))
            if add_more == 1:

                FName = input("First Name: ")
                LName = input("Last Name: ")
                RSVP_Status = input("RSVP Status (yes/no)? ")
                dietary = input("Any dietary requirements? ")
                starter = input("Starter Meal: ")
                main = input("Main Meal: ")
                dessert = input("Dessert choice: ")
                plusone = int(input("Plus one (1 - Yes, 2 - No)? "))
            elif add_more == 2:
                option = options()
                option.option1()
            

    def main(self):
        p1 = MainInvitees()
        p1.add_guest()


class EventDetails():
    def __init__(self):
        return
    #NAME,ORGANISER,DESCRIPTION
    def event(self):
        event_name = input("Event Name: ") 
        guests = pd.DataFrame(columns=['Event Name','Organiser','Description'])
        guests.to_csv(f'{event_name},EVENT-DETAILS.csv', index=False)
        return event_name

    def add_event_info(self):
        p1 = self.event()
        Organiser = input("Organiser: ")
        Desc = input("Description of Event: ")
        data = {
            'Event Name': [p1],
            'Organiser': [Organiser],
            'Description': [Desc],
          
        }
        self.guests = pd.DataFrame(data)
        # append data frame to CSV file
        self.guests.to_csv(f'{p1},EVENT-DETAILS.csv', mode='a', index=False, header=False)
        option = options()
        option.option1()


    def main(self):
        p1 = EventDetails()
        p1.add_event_info()
        

class makeFolders():
    def folders(self):
        name = input("Name Of Folder: ")
        os.mkdir(name)
        option = options()
        option.option1()

class makeMenus():
    def menu(self):
        event_name = input("Event Name: ") 
        guests = pd.DataFrame(columns=['Starters','Mains','Desserts'])
        guests.to_csv(f'{event_name},EVENT-MENU.csv', index=False)
        return event_name

    def createMenu(self):
        p1 = self.menu()

        starter = input("Starter: ")
        main = input("Main: ")
        dessert = input("Dessert ")
        while starter:

            data = {
                'Starters': [starter],
                'Mains': [main],
                'Desserts': [dessert],
            }

            self.guests = pd.DataFrame(data)
            # append data frame to CSV file
            self.guests.to_csv(f'{p1},EVENT-MENU.csv', mode='a', index=False, header=False)
            
            add_more = int(input("Add More Food?(1-YES, 2-NO) "))
            if add_more == 1:

                starter = input("Starter: ")
                main = input("Main: ")
                dessert = input("Dessert ")
            elif add_more == 2:
                option = options()
                option.option1()

    def main(self):
        menu1 = makeMenus()
        menu1.createMenu()
    

class options():
    def option1(self):
        choice = int(input("What would you like to do?\n Enter 1 for adding event information\n Enter 2 to be able to add invitees\n Enter 3 to make a folder\n Enter 4 to be able to make a menu\n Enter 5 To EXIT\n "))

        if choice == 1:
            
            p1 = EventDetails()
            p1.main()

        elif choice == 2:
            
            p1 = MainInvitees()
            p1.main()
        elif choice == 3:
            
            p1 = makeFolders()
            p1.folders()
        
        elif choice == 4:
            
            p1 = makeMenus()
            p1.main()
        
        elif choice == 5:
            return
            

o1 = options()
o1.option1()