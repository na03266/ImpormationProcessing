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

def main():
    todo_list = ToDoList()

    while True:
        choice = display_menu()

        if choice == '1':
            task = input("추가할 할 일을 입력하세요: ")
            todo_list.add_task(task)
            print("할 일이 추가되었습니다.")
        elif choice == '2':
            todo_list.show_tasks()
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택을 입력하세요.")

if __name__ == "__main__":
    main()