count = 0
max_value = 1

if __name__ == '__main__':
    print('enter a decimal number')
    n = int(input())
    binary_num = bin(n).split("b")
    binary_num = binary_num[1]
    print(binary_num)
    for index, i in enumerate(binary_num):
        if i == "1":
            count += 1
            next_item = index + 1 
            while next_item < len(binary_num):           
                if binary_num[next_item] == "1":
                    count += 1
                    counter = count
                    temp = counter                    
                    next_item += 1
                    if temp > max_value:
                        max_value = temp
                else:
                    counter = count                 
                    count = 0 
                    break
        if next_item == (len(binary_num)):
            break

    print("count is =",max_value)
