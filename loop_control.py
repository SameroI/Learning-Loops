# loop control statments allow change in loop execution from normal sequence

# break = use to termintate a loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing/place holder

while True:
    name = input("Enter a name:")
    if name != "":  # != means not equal
        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)
