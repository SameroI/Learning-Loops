# lists are used to store multiple items in a single variable

food = ["ramen", "suhi", "burger", "fries", "udon"]  # [] turns it into a list

# food[0] = "pizza" #lists can be changed after the fact as well

food.append("ice cream")  # adds to the end
food.remove("burger")  # removes item
food.pop()  # removes last item
food.insert(0, "ice tea")  # will insert the item in the givin location
food.sort()  # will sort alpha
# food.clear will clear a list


for x in food:
    print(x)
