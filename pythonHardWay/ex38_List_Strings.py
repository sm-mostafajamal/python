ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there ae not 10 things in that list . Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ['Day',"Night","Song","Frisbee", "Corn", "Banana","Girl","Boy"]

# print(len(stuff))

while len(stuff) != 10 :
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("let's do some things with stuff.")

print(stuff[1])             # printing 1 index
print(stuff[-1])            # printig last index
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))