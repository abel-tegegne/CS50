greeting=input("Greeting: ")
if "hello" in greeting.lower().strip():
    print("$0")
elif greeting.lower().strip()[0]=="h":
    print("$20")
else:
    print("$100")





