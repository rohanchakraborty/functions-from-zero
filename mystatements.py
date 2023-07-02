myList = ["apple","cherry","mango"]
myDict = {
    "drink":"coffee",
    "milk":"whole milk"
}
for item in myList:
    print(f"item is:{item}")

for _,v in myDict.items():
    print(f"my favorite thing to drink is: {v}")

#myDict = myDict # No use, syntax will still work -> might be a bug in the future
#myList = # syntax error
#testing is needed, structural part of the project