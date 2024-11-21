# def max_fun(arg_a, arg_b, arg_c):
#     return 
#     pass

# print(max_fun(6, 2, 5))

def max_fun(arg_a, arg_b, arg_c):
    
    max_num = arg_a

    if arg_b > max_num:
        max_num = arg_b
    if arg_c > max_num:
        max_num = arg_c

    return max_num
    
print(max_fun(6, 2, 5))