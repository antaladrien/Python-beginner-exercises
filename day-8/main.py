def greet():
    print("Hello Adrien")
    print("How do you do Pjotr Anton?")
    print("Isn't the weather nice today?")
greet()

def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?")
greet_with_name("Pjotr Anton")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Pjotr Anton", "Nowhere")
greet_with("Nowhere", "Pjotr Anton")

greet_with(location = "Budapest", name = "Adrien")