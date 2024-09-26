def main():
    message=input()
    expression=convert(message)
    print(expression)
def convert(message):
    smiling_message=message.replace(":)","🙂")
    angry_message=smiling_message.replace(":(","🙁")
    return angry_message
main()
