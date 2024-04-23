import os
os.system('cls')
class Application:
    def __init__(self, name, todo_list=[]):
        self.name = name
        self.todo_list = todo_list
        
    def add_todo(self, title, description, completed=False, id=None):

        todo = {
            'title': title,
            'description': description,
            'completed': completed,
            'id': id
        }
        self.todo_list.append(todo)

    def update_todo(self, todo_id, title=None, description=None, completed=None):
        
        for todo in self.todo_list:
            if todo['id'] == todo_id:
                if title is not None:
                    todo['title'] = title
                if description is not None:
                    todo['description'] = description
                if completed is not None:
                    todo['completed'] = completed
                break

    def delete_todo(self, todo_id):
        for todo in self.todo_list:
            if todo['id'] == todo_id:
                self.todo_list.remove(todo)
                break

    def show_list(self):
        for todo in self.todo_list:
            print(f"ID: {todo['id']}, Title: {todo['title']}, Description: {todo['description']}, Completed: {todo['completed']}")


