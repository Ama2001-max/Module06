import math
def pizza_unit_price(diameter_cm,price_eur):
    radius_cm = diameter_cm / 2
    area_cm2 = math.pi * (radius_cm ** 2)
    area_m2 = area_cm2 / 1000
    return price_eur * area_m2
def main():
    print("Enter Details for Pizza 01 ")
    d1 = float(input("Enter Diameter (cm): "))
    p1 = float(input("Enter Price (eur): "))

    print(f"\nEnter Details for Pizza 02 ")
    d2 = float(input("Enter Diameter (cm): "))
    p2 = float(input("Enter Price (eur): "))

    u1 = pizza_unit_price(d1,p1)
    u2 = pizza_unit_price(d2,p2)

    print(f"\nPizza 01 unit price: {u1:.2f} eur/m2")
    print(f"\nPizza 02 unit price: {u2:.2f} eur/m2")
    if u1 < u2 :
        print("Pizza O1 offers better value for money.")
    elif u2 < u1 :
        print("Pizza O2 offers better value for money.")
    else :
        print("Both pizzas offer the same value.")
if __name__ == "__main__":
    main()


