def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number //2
    else:
        print((number * 3)+1)
        return (number * 3)+1
    


def main():
    num = int(input('Enter number: \n'))

    while num != 1:
        num = collatz(num)

if __name__ == "__main__":
    main()