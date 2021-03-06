from utils import print_table


def max_profits(k, prices):
    num_rows = k + 1 # k +1 to start with a 0 row
    num_cols = len(prices)

    t = []
    for i in range(num_rows):
        t.append([None for j in range(num_cols)])

    print_table(t)

    for j in range(num_cols):
        t[0][j] = 0

    for i in range(num_rows):
        t[i][0] = 0

    print('')
    print_table(t)


if __name__ == "__main__":
    k = 3
    prices = [2, 5, 7, 1, 4, 3, 1, 3]
    max_profits(k, prices)
    

                  
