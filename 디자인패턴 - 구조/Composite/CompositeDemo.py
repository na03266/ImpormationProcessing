from abc import ABC, abstractmethod

# Component: 파일과 디렉토리의 공통 인터페이스
class FileSystemItem(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

# Leaf: 파일 클래스
class File(FileSystemItem):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

# Composite: 디렉토리 클래스
class Directory(FileSystemItem):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_item(self, item):
        self.children.append(item)

    def remove_item(self, item):
        self.children.remove(item)

    def get_name(self):
        return self.name

    def get_size(self):
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size

# 사용 예시
# 파일 생성
file1 = File("file1.txt", 10)
file2 = File("file2.txt", 5)

# 디렉토리 생성
dir1 = Directory("Folder 1")
dir2 = Directory("Folder 2")

# 디렉토리에 파일 추가
dir1.add_item(file1)
dir2.add_item(file2)

# 디렉토리에 또 다른 디렉토리 추가
dir1.add_item(dir2)

# 디렉토리의 총 크기 확인
print(dir1.get_name(), "의 총 크기:", dir1.get_size())  # 출력 결과: Folder 1 의 총 크기: 15
