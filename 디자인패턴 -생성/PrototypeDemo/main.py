from animal import Dog, Cat

if __name__ == "__main__":
    original_dog = Dog("Buddy") # 원본 객체 생성
    original_cat = Cat("Whiskers")

    cloned_dog = original_dog.clone() # 객체 복제
    cloned_cat = original_cat.clone() 

#원본과 복제된 동물 객체들의 정보 출력
    print(f"Original Dog: {original_dog.species}, Name: {original_dog.name}")
    print(f"Cloned Dog: {cloned_dog.species}, Name: {cloned_dog.name}")

    print(f"Original Cat: {original_cat.species}, Name: {original_cat.name}")
    print(f"Cloned Cat: {cloned_cat.species}, Name: {cloned_cat.name}")
