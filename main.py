# from functions import get_todos, write_todos
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")

print("It is ", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")

    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todo = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.title().strip("\n")
            print(f"{index + 1}. {item}")

    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()

            number = int(user_action[5:])
            new_todo = input("New todo: ") + "\n"
            todos[number - 1] = new_todo

            functions.write_todos(todos)
        except ValueError:
            print("Your comment is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)

            functions.write_todos(todos)

            print(f"Todo {todo_to_remove} was removed from the list.")
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Wrong command.")

print("Bye!")
