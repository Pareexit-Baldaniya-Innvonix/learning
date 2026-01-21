# Task 3:
# 3. Method overloading:
def Add(datatype, *args):
    if datatype == "int":
        answer = 0

    if datatype == "str":
        answer = ""

    for x in args:
        answer += x
    print(answer)


Add("int", 5, 6)
Add("str", "Hello ", "World")