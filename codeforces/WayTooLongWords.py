t = int(input())
for _ in range(t):
    string = input()
    length = len(string)
    if(length > 10):
        print("{}{}{}".format(string[0],length-2,string[length-1]))
    else:
        print(string)