from utils import print_table


def knapsack(items, capacity):
    num_rows = len(items) + 1 
    num_cols = capacity + 1 

    t = []
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            row.append(None)
        t.append(row)

    for i in range(num_rows):
        #set the first column of every row to 0  
        t[i][0] = 0

    for j in range(num_cols):
        t[0][j] = 0

    
    print('items: ', items)
    for i in range(1, num_rows):
        value = items[i - 1][1]
        weight = items[i - 1][0]
        print('value: ' , value)
        print('weight: ', weight) 
        for j in range(1, num_cols):
            if j >= weight:
                t[i][j] = max(
                    value + t[i - 1][j - weight],
                    t[i - 1][j])
            else:
                #detemine if choice is even valid
                #if the item is too heavy
                #keep best value from previous item
                t[i][j] = t[i - 1][j]

    print_table(t)            
    return t[num_rows - 1][num_cols - 1]
                
def main():
    items = [
        (1, 1,),
        (3, 4,),
        (4, 5,),
        (5, 7,),
    ]
    capacity = 7
    result = knapsack(items, capacity)
    print('result: ', result)
    


if __name__ == "__main__":
    main()
    

