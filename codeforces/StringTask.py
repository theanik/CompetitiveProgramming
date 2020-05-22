string = input()
string = string.lower()
voule = ['a','e','i','o','u','y','A','E','I','O','U','Y',' ']
newStr = ""
for i in string:
    if i not in voule:
        newStr += "."
        newStr += i
print(newStr)