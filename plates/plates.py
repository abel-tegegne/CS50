def main():
    plate=input("plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not s[:2].isalpha():
        return False
    if not(2<=len(s)<=6):
        return False
    for letter in range(len(s)):
        if s[letter].isdigit():
            if not s[letter:].isdigit():
                return False
    for letter in s:
        if letter.isdigit():
            if int(letter) == 0:
                return False
            else:
                break
    if not s.isalnum():
        return False

    else:
        return True

main()
