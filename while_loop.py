# while loops will execute code as long as it's condition remains true

name = ""  # replacing the quotes with NONE also works but you would need to change while to while not and adjust the rest of the code as needed

while len(name) == 0:  # if no name is eneter start loop over
    name = input("Eneter your name: ")

print("Hello " + name)
