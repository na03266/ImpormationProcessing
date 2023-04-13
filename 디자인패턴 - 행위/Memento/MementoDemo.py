# 메멘토 클래스
class TextMemento:
    def __init__(self, text):
        self.text = text

    def get_saved_text(self):
        return self.text

# 텍스트 에디터 클래스
class TextEditor:
    def __init__(self):
        self.text = ""

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def create_memento(self):
        return TextMemento(self.text)

    def restore_from_memento(self, memento):
        self.text = memento.get_saved_text()

# 텍스트 히스토리 클래스
class TextHistory:
    def __init__(self):
        self.history = []

    def save_text(self, text_memento):
        self.history.append(text_memento)

    def get_last_saved_text(self):
        if self.history:
            return self.history.pop()
        return None

# 사용 예시
text_editor = TextEditor()
text_history = TextHistory()

text_editor.set_text("첫 번째 내용 저장")
text_history.save_text(text_editor.create_memento())

text_editor.set_text("두 번째 내용 저장")
text_history.save_text(text_editor.create_memento())

print("현재 텍스트:", text_editor.get_text())  # 출력 결과: 현재 텍스트: 두 번째 내용 저장

last_saved_text = text_history.get_last_saved_text()
if last_saved_text:
    text_editor.restore_from_memento(last_saved_text)

print("복원된 텍스트:", text_editor.get_text())  # 출력 결과: 복원된 텍스트: 첫 번째 내용 저장
