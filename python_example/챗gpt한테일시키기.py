def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    file_path = input("Enter the path to the text file: ") #텍스트 파일 경로 넣는 곳 
    content = read_text_file(file_path)
    if content is not None:
        print("File content:")
        print(content)

if __name__ == "__main__":
    main()
