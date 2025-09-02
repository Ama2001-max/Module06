def gallons_to_liters(gallons):
    return gallons * 3.78541
def main():
    while True :
        gallons = float(input("Enter Volume in gallons (Negative to Quit): "))
        if gallons < 0 :
            print("Exiting Program...")
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons = {liters: .2f} liters")
if __name__ == "__main__":
    main()