text=input("Input: ")
print("Output: ",end="")
for i in text:
    if not i in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
        text=text.replace(i, "")
        print(i, end="" )

print()
