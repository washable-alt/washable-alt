def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

#positional argument
greet_with("Jack Bauer", "Nowhere")

#keyword argument

greet_with(location="Nowhere", name="Jack Bauer")