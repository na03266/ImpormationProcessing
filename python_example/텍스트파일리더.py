import pyttsx3

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found.")
        return None
    except IOError as e:
        print("Error reading the file:", e)
        return None

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    file_path = input("Enter the path of the text file you want to read: ")
    text = read_text_file(file_path)
    if text:
        print("File content:")
        print(text)
        print("Reading aloud...")
        text_to_speech(text)
