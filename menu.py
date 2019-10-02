import to_do_list


class Menu:
    def __init__(self):
        self.listy = ["1. Add a note", "2. Delete a note", "3. End the app"]
        self.to_do = to_do_list.Notebook()

    def print_menu(self):
        while True:
            print("\n")
            if len(self.to_do.all_notes) == 0:
                print ("*********      WARNING   ***********")
                print ("Not a single note in the notebook.")
                print ("************************************")
                print("\n")
            else:
                print ("---------")
                print ("List of notes:")
                print ("---------")
                for i in self.to_do.all_notes:
                    print ("| {:<5s} | Scheduled: {:<12s} ||| Note name: {:<5s} | Created: {:<5s} "\
                    .format( self.to_do.all_notes[i][0], self.to_do.all_notes[i][2], i,self.to_do.all_notes[i][1]))
                print ("---------------------------------------------------------------------")
                print("\n")
            for i in self.listy:
                print (i)
            try:
                print("\n")
                choice = int(input("Enter number for your choice: "))
                if choice < 1 or choice > 3:
                    raise Exeption()
                if choice == 3:
                    print("\n")
                    print ("The app is ended.")
                    break
            except:
                print("\n")
                print ("*********      WARNING   ***********")
                print("You must enter a number from 1 to 3.")
                print ("************************************")
                continue
            self.run_choice(choice)

    def run_choice(self, choice):
        choices_functions = {1: self.to_do.add_a_note, 2: self.to_do.delete_a_note, 3: self.end_menu}
        function = choices_functions[choice]
        return function()

    def end_menu(self):
        print ("Ending the app.")


if __name__ == "__main__":
    menu = Menu()
    menu.print_menu()