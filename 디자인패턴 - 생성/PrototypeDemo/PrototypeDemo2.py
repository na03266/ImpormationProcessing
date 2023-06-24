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
                
    def delete_task(self, task_idx):
        if 1 <= task_idx <= len(self.tasks):
            del self.tasks[task_idx - 1]
            print("할 일이 삭제되었습니다.")
        else:
            print("올바른 할 일 번호를 입력하세요.")
    def complete_task(self, task_idx):
        if 1 <= task_idx <= len(self.tasks):
            self.tasks[task_idx - 1]["completed"] = True
            print("할 일이 완료 상태로 변경되었습니다.")
        else:
            print("올바른 할 일 번호를 입력하세요.")

    def modify_task(self, task_idx, new_task):
        if 1 <= task_idx <= len(self.tasks):
            self.tasks[task_idx - 1]["task"] = new_task
            print("할 일이 수정되었습니다.")
        else:
            print("올바른 할 일 번호를 입력하세요.")


def display_menu():
    print("\n======= To-Do List =======")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 할 일 삭제")
    print("4. 할 일 완료 처리")
    print("5. 할 일 수정")
    print("6. 종료")
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
            task_idx = int(input("삭제할 할 일 번호를 입력하세요: "))
            todo_list.delete_task(task_idx)
        elif choice == '4':
            task_idx = int(input("완료 처리할 할 일 번호를 입력하세요: "))
            todo_list.complete_task(task_idx)
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택을 입력하세요.")

if __name__ == "__main__":
    main()