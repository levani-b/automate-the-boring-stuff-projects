def print_table(table):
    col_width  = []
    for col in table:
        max_len = 0
        for item in col:
            max_len = max(max_len, len(item))
        col_width.append(max_len)

    for row in zip(*table):
        for i in range(len(row)):
            print(row[i].rjust(col_width[i]), end='   ') 
        print()



def main():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
    print_table(table_data)

if __name__ == "__main__":
    main()