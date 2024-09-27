def main():
    ans=input("what time is it? ")
    time=convert(ans)
    if 7<=time<=8:
        print("breakfast time")
    if 12<=time<=13:
        print("lunch time")
    if 18<=time<=19:
        print("dinner time")

def convert(time):
    hours, minutes=time.split(":")
    min=float(minutes)/60
    return float(hours) + min

if __name__ == "__main__":
    main()
