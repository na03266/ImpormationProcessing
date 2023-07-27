from animal import Dog, Cat

if __name__ == "__main__":
    original_dog = Dog("Buddy")
    original_cat = Cat("Whiskers")

    cloned_dog = original_dog.clone()
    cloned_cat = original_cat.clone()

    print(f"Original Dog: {original_dog.species}, Name: {original_dog.name}")
    print(f"Cloned Dog: {cloned_dog.species}, Name: {cloned_dog.name}")

    print(f"Original Cat: {original_cat.species}, Name: {original_cat.name}")
    print(f"Cloned Cat: {cloned_cat.species}, Name: {cloned_cat.name}")
