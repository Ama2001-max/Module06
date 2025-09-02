def remove_odds(numbers):
    even_numbers = []
    for num in numbers:
      if num % 2 == 0:
         even_numbers.append(num)
    return even_numbers
def main():
    numbers = [3,7,2,9,6,20,18]
    print(f"original list : {numbers}")
    filtered = remove_odds(numbers)
    print(f"List without odd numbers  : {filtered}")
if __name__ == "__main__":
    main()
