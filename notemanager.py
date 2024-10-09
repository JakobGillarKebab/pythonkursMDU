import os
import json



def main():
     load_todos()
     while True:
            clear()
            print("Current working directory:", os.getcwd())

            for i, task in enumerate(todos):
                status = '[X]' if task['done'] else '[ ]'
                print(f"{i} | {status} {task['title']}")
            user_want = input(">")
            if user_want == "A": 
                add()
            elif user_want == "D":
                 delete_todo()
            elif user_want == "H":
                 display_help()
            elif user_want == "C":
                 check()
            elif user_want == "X": 
                save_exit()
                break
            else:
                continue
def clear():
    os.system("cls")
    print("DODO manager")
    print("-" * 14)

def display_help():
    print("A | add a new todo")
    print("C | check a todo")
    print("D | delete todo")
    print("H | display help")
    print("X | exit program")
    input("Press enter to continue")    

def add():
    title = input("Enter Todo: ")
    todos.append({"title":title, "done": False})
    

def delete_todo():
    
    try:
        del_index = int(input("Index: "))
        todos.pop(del_index)
    except IndexError:
        print("Wrong index")
        input("Press enter to continue")
        main()
    except ValueError:
        print("Wrong input")
        input("press enter to continue")
        main()

def check():
     try:
        check_index = int(input("Index: "))
        todos[check_index]["done"] = True
     except IndexError:
        print("Wrong index")
        input("Press enter to continue")
        main()
     except ValueError:
        print("Wrong input")
        input("press enter to continue")
        main()

def save_exit():
     with open("todos.txt", "w") as f:
        json.dump(todos, f)

def load_todos():
    global todos
    try:
        with open("todos.txt", "r") as f:
            todos = json.load(f)
        print("Todos loaded successfully.")
    except FileNotFoundError:
        print("No todos file found. Starting with an empty list.")
        todos = []  
    except json.JSONDecodeError:
        print("Error reading the todos file. Starting with an empty list.")
        todos = []  
    except Exception as e:
        print(f"An error occurred: {e}")
        todos = []
     

todos = [{"title":"Eat kebab", "done": False },
         {"title":"Pet cat", "done": False },
        {"title":"play WarThunder", "done": True } ]





if __name__== "__main__":
     main()