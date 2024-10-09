import os
import json
 
notes = {}
 
def main():
     load_notes()
     while True:
            clear()
 
            for task in notes:
                print(f"{notes[task]['title']}")
            print("-" * 14)
            display_help()
            print("Current working directory:", os.getcwd())
            user_want = input(">")
            if user_want == "add":
                add()
            elif user_want == "rm":
                 delete_note()
            elif user_want == "view":
                 view()
            elif user_want == "exit":
                save_exit()
                break
            else:
                print("Wrong index")
                input("Press enter to continue")
                continue
           
 
def clear():
    os.system("cls")
    print(".:ALWAYSNOTE:.")
    print("-" * 14)
 
def display_help():
    print("add | add a new note")
    print("view | view note")
    print("rm | remove note")
    print("exit | exit program")
    print("-" * 14)
 
def add():
    global notes
    try:
        title = input("Enter name for note: ")
        description = input("Enter description for note: ")
        notes[title] = {"title":title, "description": description}
    except ValueError:
        print("wrong input")
 
 
def delete_note():
    global notes
    del_name = input("Name of note to remove: ")
    if del_name in notes:
            notes.pop(del_name)
            print(f"Note '{del_name}' has been removed")
    else:
        print("Wrong index")
        input("Press enter to continue")
        main()
 
def view():
    try:    
        view_name = input("Name of note for viewing: ")
        print(notes[view_name]["description"])
        input("Press enter to continue")
   
    except KeyError:
        print("Wrong name")
        input("press enter to continue")
        main()
    except ValueError:
        print("Wrong input")
        input("press enter to continue")
        main()
 
def save_exit():
     with open("notes.txt", "w") as f:
        json.dump(notes, f)
 
def load_notes():
    global notes
    try:
        with open("notes.txt", "r") as f:
            notes = json.load(f)
        print("Notes loaded successfully.")
    except FileNotFoundError:
        print("No notes file found. Starting with an empty list.")
        notes = {}
    except json.JSONDecodeError:
        print("Error reading the notes file. Starting with an empty list.")
        notes = {}
    except Exception as e:
        print(f"An error occurred: {e}")
        notes = {}
 
 
 
if __name__== "__main__":
     main()