import json

tasks = []
def add_task():
    task_name = input("Ввести название задачи:")
    task = {
    "title": task_name,
    "completed": False
}
    tasks.append(task)

#add_task()
#print(tasks)

tasks = [{"title": "Z777",
    "completed": False},{"title": "Z904",
    "completed": True}]
def show_tasks():
    for task in tasks:
        print(f"{task["title"]} - {task['completed']}" )
show_tasks()

def complete_task():
    try:
        number_task = int(input("Ввести номер задачи:"))
        tasks[number_task - 1]["completed"] = True
        print("Статус задачи перешел в выполненный")
    except ValueError:
        print("Ввод не числового значения")

complete_task()
print(tasks)

def delete_task():
    number_task = int(input("Ввести номер задачи:"))
    tasks.pop(number_task - 1)
#delete_task()
print(tasks)

def save_tasks():
    with open(
            "tasks.json",
            "w",
            encoding="utf-8"
    ) as file:
        json.dump(
            tasks,
            file,
            ensure_ascii=False,
            indent=4
        )

    print("Файл tasks.json создан.")
#save_tasks()

def load_tasks():
    try:
        with open(
                "tasks.json",
                "r",
                encoding="utf-8"
        ) as file:
            loaded_user = json.load(file)

        print("Данные из JSON:")
        print(loaded_user)
    except FileNotFoundError:
        tasks = []
load_tasks()






