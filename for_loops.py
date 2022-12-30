import time  # need for the count down!

# for loops act like while loops but have a set number of times they can be exectuted

for i in range(10):  # this loop would count from 1-10
    print(i + 1)

for i in range(50, 100 + 1, 2):
    # this would count from 50-100 the +1 makes it count to 100 instead of 99 and the 2 makes it count it up by 2
    print(i)

for i in "Samero":  # this would print every letter in the givin "name"
    print(i)

for seconds in range(10, 0, -1):  # this is going to give us a count down from 10
    print(seconds)
    time.sleep(1)
print("I can count :)")
