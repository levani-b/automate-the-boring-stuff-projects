def comma_code(arr):
    if len(arr) <= 0:
        return f'List is empty'
    
    comma_str = ''
    length = len(arr)
    for i, item in enumerate(arr):
        if i == length - 1:
            comma_str += f'and {arr[i]}'
        else:
            comma_str += f'{item}, '

    return comma_str


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    empty_spam = []
    print('non empty list \n',comma_code(spam))
    print('empty list \n',comma_code(empty_spam))


if __name__ == "__main__":
    main()