import os
from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def show_tasks(self):
        if not self.tasks:
            print("할 일이 없습니다.")
        else:
            print("할 일 목록:")
            for idx, task_info in enumerate(self.tasks, start=1):
                task_status = "완료" if task_info["completed"] else "미완료"
                print(f"{idx}. [{task_status}] {task_info['task']}")

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


    def save_to_file(self):
        today_date = datetime.now().strftime("%Y-%m-%d")
        completed_filename = f"completed_tasks_{today_date}.txt"
        incomplete_filename = f"incomplete_tasks_{today_date}.txt"

        with open(completed_filename, "w") as completed_file:
            with open(incomplete_filename, "w") as incomplete_file:
                for task_info in self.tasks:
                    if task_info["completed"]:
                        completed_file.write(task_info["task"] + "\n")
                    else:
                        incomplete_file.write(task_info["task"] + "\n")

    def load_from_file(self, filename):
        if not os.path.isfile(filename):
            return

        with open(filename, "r") as file:
            for line in file:
                task = line.strip()
                self.add_task(task)

    def load_today_tasks(self):
        today_date = datetime.now().strftime("%Y-%m-%d")
        completed_filename = f"completed_tasks_{today_date}.txt"
        incomplete_filename = f"incomplete_tasks_{today_date}.txt"

        if os.path.isfile(completed_filename):
            self.load_from_file(completed_filename)

        if os.path.isfile(incomplete_filename):
            self.load_from_file(incomplete_filename)

def display_menu():
    print("\n======= To-Do List =======")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 할 일 삭제")
    print("4. 할 일 완료 처리")
    print("5. 할 일 수정")
    print("6. 오늘 완료한 일들 저장")
    print("7. 오늘 할 일 불러오기")
    print("8. 종료")
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
            task_idx = int(input("수정할 할 일 번호를 입력하세요: "))
            new_task = input("새로운 할 일 내용을 입력하세요: ")
            todo_list.modify_task(task_idx, new_task)
        elif choice == '6':
            todo_list.save_to_file()
            print("오늘 완료한 일들이 저장되었습니다.")
        elif choice == '7':
            today_date = datetime.now().strftime("%Y-%m-%d")
            completed_filename = f"completed_tasks_{today_date}.txt"
            incomplete_filename = f"incomplete_tasks_{today_date}.txt"
            todo_list = ToDoList()
            todo_list.load_from_file(completed_filename)
            todo_list.load_from_file(incomplete_filename)
            print("오늘 할 일을 불러왔습니다.")
        elif choice == '8':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택을 입력하세요.")

if __name__ == "__main__":
    main()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton, QLabel
from datetime import datetime

class ToDoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('To-Do List')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.tasks_list_widget = QListWidget()
        self.layout.addWidget(self.tasks_list_widget)

        self.add_task_input = QLineEdit()
        self.layout.addWidget(self.add_task_input)

        self.add_task_button = QPushButton('Add Task', self)
        self.add_task_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_task_button)

        self.delete_task_button = QPushButton('Delete Task', self)
        self.delete_task_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_task_button)

        self.complete_task_button = QPushButton('Complete Task', self)
        self.complete_task_button.clicked.connect(self.complete_task)
        self.layout.addWidget(self.complete_task_button)

        self.save_button = QPushButton('Save Today\'s Tasks', self)
        self.save_button.clicked.connect(self.save_to_file)
        self.layout.addWidget(self.save_button)

        self.load_button = QPushButton('Load Today\'s Tasks', self)
        self.load_button.clicked.connect(self.load_from_file)
        self.layout.addWidget(self.load_button)

        self.today_date_label = QLabel(self)
        self.layout.addWidget(self.today_date_label)

        self.central_widget.setLayout(self.layout)

        self.todo_list = []

        self.update_today_date_label()

    def update_today_date_label(self):
        today_date = datetime.now().strftime("%Y-%m-%d")
        self.today_date_label.setText(f"Today's Date: {today_date}")

    def add_task(self):
        task = self.add_task_input.text()
        self.todo_list.append({"task": task, "completed": False})
        self.add_task_input.clear()
        self.update_tasks_list()

    def delete_task(self):
        selected_index = self.tasks_list_widget.currentRow()
        if selected_index != -1:
            del self.todo_list[selected_index]
            self.update_tasks_list()

    def complete_task(self):
        selected_index = self.tasks_list_widget.currentRow()
        if selected_index != -1:
            self.todo_list[selected_index]["completed"] = True
            self.update_tasks_list()

    def update_tasks_list(self):
        self.tasks_list_widget.clear()
        for task_info in self.todo_list:
            task_status = "Completed" if task_info["completed"] else "Incomplete"
            self.tasks_list_widget.addItem(f"{task_info['task']} ({task_status})")

    def save_to_file(self):
        today_date = datetime.now().strftime("%Y-%m-%d")
        completed_filename = f"completed_tasks_{today_date}.txt"
        incomplete_filename = f"incomplete_tasks_{today_date}.txt"

        with open(completed_filename, "w") as completed_file:
            with open(incomplete_filename, "w") as incomplete_file:
                for task_info in self.todo_list:
                    if task_info["completed"]:
                        completed_file.write(task_info["task"] + "\n")
                    else:
                        incomplete_file.write(task_info["task"] + "\n")

    def load_from_file(self):
        today_date = datetime.now().strftime("%Y-%m-%d")
        completed_filename = f"completed_tasks_{today_date}.txt"
        incomplete_filename = f"incomplete_tasks_{today_date}.txt"

        if not os.path.isfile(completed_filename) and not os.path.isfile(incomplete_filename):
            return

        self.todo_list = []

        with open(completed_filename, "r") as completed_file:
            for line in completed_file:
                task = line.strip()
                self.todo_list.append({"task": task, "completed": True})

        with open(incomplete_filename, "r") as incomplete_file:
            for line in incomplete_file:
                task = line.strip()
                self.todo_list.append({"task": task, "completed": False})

        self.update_tasks_list()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToDoListApp()
    window.show()
    sys.exit(app.exec_())
