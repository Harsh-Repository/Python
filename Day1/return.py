def substract(a,b):
    result = a - b
    return result

r = substract(10,7)
print(r)

#########################

def find_max_in_list(some_list):
    max_element = some_list[0]
    length = len(some_list)

    for i in range(1, length):
        
        if some_list[i] >max_element:
            max_element=some_list[i]
        
    return max_element

arr = [12,32,143,1445,245,1242]
print(find_max_in_list(arr))
arr.append(1241241)
print(find_max_in_list(arr))
