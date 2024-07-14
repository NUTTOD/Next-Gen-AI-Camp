s = input()
s = s.strip('[]')
string_list = s.split(',')

input_list = [int(x) for x in string_list]

def count_greater_pairs(input_list):
    count = 0
    n = len(input_list)
    for i in range(n - 1):
        if input_list[i] > input_list[i + 1]:
            count += 1
    return count


result = count_greater_pairs(input_list)
print(result)