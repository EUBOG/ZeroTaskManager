class Task:
    def __init__(self, taskname, tasktale, taskpoint, taskstat):
        self.taskname = taskname  # наименование задачи
        self.tasktale = tasktale  # описание задачи
        self.taskpoint = taskpoint  # срок выполнения задачи
        self.taskstat = taskstat  # статус задачи


class TaskManager:
    def __init__(self):
        self.tasktable = []  # Список задач

    def add_task(self, task):
        self.tasktable.append(task)  # Добавление задачи в список

    def display_tasks(self):
        # Заголовки таблицы
        print(f"{'Наименование':<20} {'Описание':<30} {'Срок выполнения':<20} {'Статус':<10}")
        print("=" * 80)

        # Вывод задач
        for task in self.tasktable:
            print(f"{task.taskname:<20} {task.tasktale:<30} {task.taskpoint:<20} {task.taskstat:<10}")

# Пример использования
if __name__ == "__main__":
    task_manager = TaskManager()

    # Создание задач
    task1 = Task("Бег", "Пробежать 5 км", "2025-05-24", "New")
    task2 = Task("Душ", "Помыться", "2025-05-24", "New")
    task3 = Task("Кайф", "Кайфануть от бега и душа", "2025-05-24", "New")

    # Добавление задач в менеджер задач
    task_manager.add_task(task1)
    task_manager.add_task(task2)
    task_manager.add_task(task3)

    # Вывод таблицы задач
    task_manager.display_tasks()