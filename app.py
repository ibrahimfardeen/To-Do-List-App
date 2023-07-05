from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

    def view_tasks(self):
        return self.tasks

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def load_tasks(self, filename):
        with open(filename, 'r') as file:
            self.tasks = [line.strip() for line in file]


todolist = ToDoList()


@app.route('/')
def index():
    tasks = todolist.view_tasks()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    todolist.add_task(task)
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete():
    task = request.form['task']
    todolist.delete_task(task)
    return redirect('/')


@app.route('/save', methods=['POST'])
def save():
    filename = request.form['filename']
    todolist.save_tasks(filename)
    return redirect('/')


@app.route('/load', methods=['POST'])
def load():
    filename = request.form['filename']
    todolist.load_tasks(filename)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
