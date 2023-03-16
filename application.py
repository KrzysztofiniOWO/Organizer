import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import widget_templates as wt

widgets = {
    "button": [],
    "image": [],
    "input": [],
    "group_box": [],
}


class Application(QWidget):
    """Main class to maintain out application functionalities"""

    def __init__(self):
        super().__init__()

        #We set some parameters of our main window
        self.move(100, 100)
        self.setStyleSheet("background-color: '#3e305a';")
        self.setWindowTitle("Organizer")
        self.setWindowIcon(QtGui.QIcon('app_icon.png'))

        #We create grid and set it for our layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        #We set a dictionary to store events in our app
        self.events_container = {
            "name": [],
            "date": [],
            "description": [],
        }

        #We show first frame of our app and load events that were added
        self.load_events()
        self.main_menu_frame()

    def main_menu_frame(self):
        """Frame for main menu of our app"""

        #We prepare screen for new frame
        self.clear_grid()

        #We create logo for our main menu
        logo = wt.create_image("main_logo.png")
        widgets["image"].append(logo)

        #We create check button for our main menu
        check_butt = wt.create_button("Check", self.check_events_frame, 200, 200)
        widgets["button"].append(check_butt)

        # We create add button for our main menu
        add_butt = wt.create_button("Add", self.add_event_frame, 200, 200)
        widgets["button"].append(add_butt)

        # We create edit button for our main menu
        edit_butt = wt.create_button("Edit", self.edit_event_frame, 200, 200)
        widgets["button"].append(edit_butt)

        # We create exit button for our main menu
        exit_butt = wt.create_button("Quit", self.save_events_and_close_app, 200, 200)
        widgets["button"].append(exit_butt)

        #We add our elements to grid
        self.grid.addWidget(widgets["image"][-1], 0, 0, 1, 2)
        widgets["button"][-4].move(100, 100)
        self.grid.addWidget(widgets["button"][-4], 1, 0, 1, 1, alignment=Qt.AlignRight)
        self.grid.addWidget(widgets["button"][-3], 1, 1, 1, 1, alignment=Qt.AlignLeft)
        self.grid.addWidget(widgets["button"][-2], 2, 0, 1, 1, alignment=Qt.AlignRight)
        self.grid.addWidget(widgets["button"][-1], 2, 1, 1, 1, alignment=Qt.AlignLeft)
        #alignment=Qt.AlignHCenter

        self.show()

    def add_event_frame(self):
        """Frame used to add events in our app"""

        # We prepare screen for new frame
        self.clear_grid()

        #We create box for user to enter event name
        event_name_input = wt.create_user_input("Enter name of event", 760, 100)
        widgets["input"].append(event_name_input)

        #We create box for user to enter year of event
        event_year_input = wt.create_user_input("yyyy", 240, 100)
        widgets["input"].append(event_year_input)

        # We create box for user to enter month of event
        event_month_input = wt.create_user_input("mm", 240, 100)
        widgets["input"].append(event_month_input)

        # We create box for user to enter day of event
        event_day_input = wt.create_user_input("dd", 240, 100)
        widgets["input"].append(event_day_input)

        # We create box for user to enter description of event
        event_desc_input = wt.create_user_input("Enter description", 760, 200)
        widgets["input"].append(event_desc_input)

        # We create button to go back to main menu
        go_back_butt = wt.create_button("Go back", self.main_menu_frame, 200, 120)
        widgets["button"].append(go_back_butt)

        # We create button to confirm and save new event
        confirm_butt = wt.create_button("Confirm", self.add_event, 200, 120)
        widgets["button"].append(confirm_butt)

        # We add our elements to grid
        self.grid.addWidget(widgets["input"][-5], 0, 0, 1, 3, alignment=Qt.AlignHCenter)
        self.grid.addWidget(widgets["input"][-4], 1, 0, 1, 1, alignment=Qt.AlignCenter)
        self.grid.addWidget(widgets["input"][-3], 1, 1, 1, 1, alignment=Qt.AlignCenter)
        self.grid.addWidget(widgets["input"][-2], 1, 2, 1, 1, alignment=Qt.AlignCenter)
        self.grid.addWidget(widgets["input"][-1], 2, 0, 1, 3, alignment=Qt.AlignCenter)
        self.grid.addWidget(widgets["button"][-2], 3, 0, 1, 1, alignment=Qt.AlignCenter)
        self.grid.addWidget(widgets["button"][-1], 3, 2, 1, 1, alignment=Qt.AlignCenter)

    def check_events_frame(self):
        """Frame used to check events in our app"""

        # We prepare screen for new frame
        self.clear_grid()

        # Check how many entries we already have
        length = len(self.events_container["name"])

        # We add all events we have in our application to the screen
        for counter in range(0, length):
            gb = wt.create_event_group_box(
                self.events_container["name"][counter],
                self.events_container["date"][counter],
                self.events_container["description"][counter],
                (lambda state, edit_counter=counter: self.edit_event_frame(edit_counter)),
                (lambda state, delete_counter=counter: self.delete_event(delete_counter))
            )
            widgets["group_box"].append(gb)
            self.grid.addWidget(widgets["group_box"][-1], counter, 0)

        # We create button to go back to main menu
        go_back_butt = wt.create_button("Go back", self.main_menu_frame, 200, 120)
        widgets["button"].append(go_back_butt)

        #We add rest of our elements to the grid
        self.grid.addWidget(widgets["button"][-1], length+2, 0, 1, 1, alignment=Qt.AlignCenter)

        self.show()

    def add_event(self):
        """Add event after pressing confirm button"""

        #Add name of new event to our dict
        self.events_container["name"].append(widgets["input"][-5].text())

        #Add date of new event to our dict
        self.events_container["date"].append(f'{widgets["input"][-4].text()}.{widgets["input"][-3].text()}.{widgets["input"][-2].text()}')

        #Add description of new event to our dict
        self.events_container["description"].append(widgets["input"][-1].text())

        #Redirect user to main menu after event was added
        self.main_menu_frame()

    def save_events_and_close_app(self):
        """Save our events before closing our app"""

        #Check how many entries we already have
        length = len(self.events_container["name"])

        #Save our entries to a file
        with open("event_file.txt", "w") as f:
            for counter in range(0, length):
                f.write(f'{self.events_container["name"][counter]}\n')
                f.write(f'{self.events_container["date"][counter]}\n')
                f.write(f'{self.events_container["description"][counter]}\n')

            #Close file after all events were added
            f.close()

        #close our app when all events were saved
        QCoreApplication.quit()

    def load_events(self):
        """Load events when starting app"""

        with open("event_file.txt", "r") as f:

            #We read all lines from a file
            lines = [line.strip() for line in f.readlines()]

            #We loop through lines and add them to their slots in our dict
            for counter in range(0, len(lines)):

                if (counter % 3) == 0:
                    self.events_container["name"].append(lines[counter])

                if (counter % 3) == 1:
                    self.events_container["date"].append(lines[counter])

                if (counter % 3) == 2:
                    self.events_container["description"].append(lines[counter])

            #We close file after we load all events
            f.close()

    def edit_event_frame(self, event_number):
        """Frame used to edit events in our app"""

        # We prepare screen for new frame
        self.clear_grid()

        # We create box for user to enter event name if he wants to edit it
        event_name_input = wt.create_user_input(f'{self.events_container["name"][event_number]}', 760, 100)
        widgets["input"].append(event_name_input)

        # We create box for user to enter year of event he wants to edit it
        event_year_input = wt.create_user_input(f'{self.events_container["date"][event_number][:4]}', 240, 100)
        widgets["input"].append(event_year_input)

        # We create box for user to enter month of event he wants to edit it
        event_month_input = wt.create_user_input(f'{self.events_container["date"][event_number][5:7]}', 240, 100)
        widgets["input"].append(event_month_input)

        # We create box for user to enter day of event he wants to edit it
        event_day_input = wt.create_user_input(f'{self.events_container["date"][event_number][8:]}', 240, 100)
        widgets["input"].append(event_day_input)

        # We create box for user to enter description of event he wants to edit it
        event_desc_input = wt.create_user_input(f'{self.events_container["description"][event_number]}', 760, 200)
        widgets["input"].append(event_desc_input)

        # We create button to go back to main menu
        go_back_butt = wt.create_button("Go back", self.main_menu_frame, 200, 120)
        widgets["button"].append(go_back_butt)

        # We create button to confirm and save new event
        confirm_butt = wt.create_button("Confirm", (lambda: self.change_after_edit(event_number)),  200, 120)
        widgets["button"].append(confirm_butt)

        # We add our elements to grid
        self.grid.addWidget(widgets["input"][-5], 0, 0, 1, 3, alignment=Qt.AlignHCenter)
        self.grid.addWidget(widgets["input"][-4], 1, 0, 1, 1, alignment=Qt.AlignCenter)
        self.grid.addWidget(widgets["input"][-3], 1, 1, 1, 1, alignment=Qt.AlignCenter)
        self.grid.addWidget(widgets["input"][-2], 1, 2, 1, 1, alignment=Qt.AlignCenter)
        self.grid.addWidget(widgets["input"][-1], 2, 0, 1, 3, alignment=Qt.AlignCenter)
        self.grid.addWidget(widgets["button"][-2], 3, 0, 1, 1, alignment=Qt.AlignCenter)
        self.grid.addWidget(widgets["button"][-1], 3, 2, 1, 1, alignment=Qt.AlignCenter)

        #

        print("dziba")

    def change_after_edit(self, number_of_event):
        """Save edited event information"""

        #save changed information to our dict
        self.events_container["name"][number_of_event] = widgets["input"][-5].text()
        self.events_container["date"][number_of_event] = f'{widgets["input"][-4].text()}.{widgets["input"][-3].text()}.{widgets["input"][-2].text()}'
        self.events_container["description"][number_of_event] = widgets["input"][-1].text()

        # Redirect user to main menu after event was added
        self.main_menu_frame()

    def delete_event(self, number_of_event):
        """Function used to delete certain event from app and reload screen"""

        #We delete event that user selected to delete
        del self.events_container["name"][number_of_event]
        del self.events_container["date"][number_of_event]
        del self.events_container["description"][number_of_event]

        #We reload frame with events without this event
        self.check_events_frame()

    def clear_grid(self):
        """Clear grid of all old elements"""

        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)


def main():
    app = QApplication(sys.argv)
    gui = Application()
    sys.exit(app.exec_())


main()
