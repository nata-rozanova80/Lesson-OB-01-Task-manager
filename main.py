# Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
import sys
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

    @classmethod
    def list_tasks(cls):
        if not cls.task_list:
            print("Список задач пуст.")
            return
        for i, task in enumerate(cls.task_list, start=1):
            print(f"{i}. {task}")

    @classmethod
    def mark_task_completed(cls):
        cls.list_tasks()
        if cls.task_list:
            index = int(input("Введите номер задачи, которую хотите отметить как выполненную: ")) - 1
            if 0 <= index < len(cls.task_list):
                cls.task_list[index].mark_as_completed()
                print("Задача отмечена как выполненная.")
            else:
                print("Некорректный номер задачи.")

def start_work():
    while True:
        print(f"\nМЕНЮ ПРОГРАММЫ")
        print(f"1. Список всех задач")
        print(f"2. Добавить задачу")
        print(f"3. Отметить выполненную задачу")
        print(f"4. Список невыполненных задач")
        print(f"5. Выход")

        number = input("Выберите номер действия: ")

    # Выбор действия соответственно меню
        if number == "1":
            Task.list_tasks()
        elif number == "2":
            Task.add_task()
        elif number == "3":
            Task.mark_task_completed()
        elif number == "4":
            print("Список невыполненных задач:")
            for task in Task.task_list:
                if not task.completed:
                    print(task)
        elif number == "5":
            print("Выход из программы.")
            #break
            sys.exit() # Завершение работы программы
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер от 1 до 5.")
# Запуск программы
start_work()


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

