
sorted_fruit_list = ["apple", "banana", "coconut", "durian", "eggplant"]

def find_fruit(list, target):
    first_index = 0
    last_index = (len(list) - 1)
    first_letter = ord(target[0])
    

    while first_index < last_index:
        mid_index = (first_index + last_index) // 2

        if list[mid_index] == target:
            return True
        else:
            if ord(target[0]) > ord(list[mid_index][0]):
                first_index = mid_index + 1
            else:
                last_index = mid_index - 1
    return False

print (find_fruit(sorted_fruit_list, "Durian"))

            

    


