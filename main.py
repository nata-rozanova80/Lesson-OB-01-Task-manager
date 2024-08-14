# Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    # Создаем пустой список для хранения задач
    task_list = []

    def __init__(self, title, description, due_date):
        self.title = title          # Заголовок задачи
        self.description = description  # Описание задачи
        self.due_date = due_date    # Дата выполнения задачи
        self.completed = False       # Статус выполнения задачи, по умолчанию - не выполнена

    def mark_as_completed(self):
        self.completed = True        # Метод для отметки задачи как выполненной

    def __str__(self):
        return f"Task: {self.title}, Description: {self.description}, Due date: {self.due_date}, Completed: {self.completed}"

    # Функция для добавления новой задачи
    @classmethod
    def add_task(cls):
        print("Добавление задачи...")
        title = input("Введите заголовок задачи: ")
        description = input("Введите описание задачи: ")
        due_date = input("Введите дату выполнения задачи: ")
        new_task = cls(title, description, due_date)
        cls.task_list.append(new_task)
        print(f"Задача '{title}' добавлена.")

# Пример использования класса Task
task1 = Task("Сделать домашнее задание", "Выполнить задачи по математике", "2023-10-31")
print(task1)
task1.mark_as_completed()

# Запрашиваем у пользователя ввод новой задачи
Task.add_task()

# Выводим список задач
print("Список задач:")
for i, task in enumerate(Task.task_list, start=1):
    print(f"{i}. {task}")

