import os
from datetime import datetime
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLineEdit, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QFont, QFontMetrics, QPainter, QPen, QTextOption
from PyQt5.QtCore import Qt

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def show_tasks(self):
        return self.tasks

    def delete_task(self, task_idx):
        if 0 <= task_idx < len(self.tasks):
            del self.tasks[task_idx]

    def complete_task(self, task_idx):
        if 0 <= task_idx < len(self.tasks):
            self.tasks[task_idx]["completed"] = not self.tasks[task_idx]["completed"]

    def modify_task(self, task_idx, new_task):
        if 0 <= task_idx < len(self.tasks):
            self.tasks[task_idx]["task"] = new_task

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for task_info in self.tasks:
                task_status = "completed" if task_info["completed"] else "incomplete"
                file.write(f"{task_info['task']},{task_status}\n")

    def load_from_file(self, filename):
        if not os.path.isfile(filename):
            return

        with open(filename, "r") as file:
            for line in file:
                task_data = line.strip().split(',')
                if len(task_data) == 2:
                    task = task_data[0]
                    completed = True if task_data[1] == "completed" else False
                    self.tasks.append({"task": task, "completed": completed})

class CompletedTaskListWidget(QListWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self.viewport())
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        for row in range(self.count()):
            item = self.item(row)
            if item and item.data(Qt.UserRole):
                rect = self.visualRect(self.indexFromItem(item))
                text = item.text()
                metrics = QFontMetrics(self.font())
                width = metrics.width(text)
                height = metrics.height()
                line_x = rect.x() + width
                line_y = rect.y() + height // 2
                painter.drawLine(rect.x(), line_y, line_x, line_y)

    def editorEvent(self, event, option, index):
        if event.type() == QEvent.MouseButtonRelease and event.button() == Qt.LeftButton:
            rect = self.visualRect(index)
            checkbox_rect = option.rect.adjusted(5, 0, 0, 0)
            if checkbox_rect.contains(event.pos()):
                item = self.itemFromIndex(index)
                task_idx = self.row(item)
                self.itemClicked.emit(item)
                self.parent().complete_task(task_idx)
                return True

        return super().editorEvent(event, option, index)

class ToDoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('To-Do List')
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.tasks_list_widget = CompletedTaskListWidget()
        self.tasks_list_widget.setFont(QFont("Arial", 14))
        self.layout.addWidget(self.tasks_list_widget)

        self.add_task_input = QLineEdit()
        self.add_task_input.setFont(QFont("Arial", 14))
        self.add_task_input.setPlaceholderText("Enter a new task")
        self.layout.addWidget(self.add_task_input)

        self.buttons_layout = QHBoxLayout()

        self.add_task_button = QPushButton('Add', self)
        self.add_task_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.add_task_button.clicked.connect(self.add_task)
        self.buttons_layout.addWidget(self.add_task_button)

        self.delete_task_button = QPushButton('Delete', self)
        self.delete_task_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.delete_task_button.clicked.connect(self.delete_task)
        self.buttons_layout.addWidget(self.delete_task_button)

        self.complete_task_button = QPushButton('Complete', self)
        self.complete_task_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.complete_task_button.clicked.connect(self.complete_task)
        self.buttons_layout.addWidget(self.complete_task_button)

        self.save_button = QPushButton('Save', self)
        self.save_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.save_button.clicked.connect(self.save_to_file)
        self.buttons_layout.addWidget(self.save_button)

        self.load_button = QPushButton('Load', self)
        self.load_button.setFont(QFont("Arial", 14, QFont.Bold))
        self.load_button.clicked.connect(self.load_from_file)
        self.buttons_layout.addWidget(self.load_button)

        self.layout.addLayout(self.buttons_layout)

        self.today_date_label = QLabel(self)
        self.today_date_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.layout.addWidget(self.today_date_label)

        self.central_widget.setLayout(self.layout)

        self.todo_list = ToDoList()
        self.load_from_file()

        self.update_today_date_label()
        self.update_tasks_list()

    def update_today_date_label(self):
        today_date = datetime.now().strftime("%Y-%m-%d")
        self.today_date_label.setText(f"Today's Date: {today_date}")

    def add_task(self):
        task = self.add_task_input.text().strip()
        if task:
            self.todo_list.add_task(task)
            self.add_task_input.clear()
            self.update_tasks_list()

    def delete_task(self):
        selected_item = self.tasks_list_widget.currentItem()
        if selected_item:
            task_idx = self.tasks_list_widget.row(selected_item)
            self.todo_list.delete_task(task_idx)
            self.update_tasks_list()

    def complete_task(self):
        selected_item = self.tasks_list_widget.currentItem()
        if selected_item:
            task_idx = self.tasks_list_widget.row(selected_item)
            self.todo_list.complete_task(task_idx)
            self.update_tasks_list()

    def update_tasks_list(self):
        self.tasks_list_widget.clear()
        tasks = self.todo_list.show_tasks()
        for task_info in tasks:
            task_text = f"{task_info['task']}"
            if task_info["completed"]:
                task_text = f"<s>{task_text}</s>"
            self.tasks_list_widget.addItem(task_text)
            item = self.tasks_list_widget.item(self.tasks_list_widget.count() - 1)
            item.setData(Qt.UserRole, task_info["completed"])

    def save_to_file(self):
        today_date = datetime.now().strftime("%Y-%m-%d")
        filename = f"tasks_{today_date}.txt"
        self.todo_list.save_to_file(filename)
        QMessageBox.information(self, "Information", "Tasks have been saved successfully.", QMessageBox.Ok)

    def load_from_file(self):
        today_date = datetime.now().strftime("%Y-%m-%d")
        filename = f"tasks_{today_date}.txt"
        self.todo_list.load_from_file(filename)
        self.update_tasks_list()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToDoListApp()
    window.show()
    sys.exit(app.exec_())
