class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            print("할 일이 없습니다.")
        else:
            print("할 일 목록:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

def display_menu():
    print("\n======= To-Do List =======")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 종료")
    choice = input("선택: ")
    return choice