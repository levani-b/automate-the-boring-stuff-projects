from the_collatz_sequence import collatz

def main():
    try:
        num = int(input('Enter number: \n')) 
    except ValueError:
        print('User must enter an integer')
        return 
    
    while num != 1:
        num = collatz(num)

if __name__ == "__main__":
    main()