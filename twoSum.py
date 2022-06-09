my_list = [2, 5, 10, 20, 44, 32, 12, -45]

def two_sum(my_list, target):
    for i in range(len(my_list)):
        for j in range(i+1,len(my_list)):
            if my_list[i] + my_list[j] == target:
                return (i,j)
            

def one_pass(my_list, target):
    complement = {}
    for i in range(len(my_list)):
        num = my_list[i]
        comp = target - num
        complement[comp] = i
        if (complement.get(num) != None):
            return (complement.get(num), i)

print(two_sum(my_list, 52))
print(two_sum(my_list, -33))

print(one_pass(my_list, 52))
print(one_pass(my_list, -33))

