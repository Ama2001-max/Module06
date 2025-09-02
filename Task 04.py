def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
def main():
    numbers = [3,7,2,4,9]
    print(f"List : {numbers}")

    result = sum_of_list(numbers)
    print(f"Sum of numbers in the list : {result}")
if __name__ == "__main__":
    main()