def main():
    dollars=dollars_to_float(input("how much was the meal? "))
    percent=percent_to_float(input("what percentage would you like to tip? "))
    tip=dollars*percent
    print(f"leave ${tip:.2f}")
def dollars_to_float(d):
    d1=float(d.replace("$",""))
    return d1
def percent_to_float(p):
    p1=float(p.replace("%",""))/100
    return p1

main()
