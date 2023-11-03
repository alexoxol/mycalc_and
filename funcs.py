def fun_add(a,b):
    return a+b

def fun_sub(a,b):
    return a-b

def fun_mult(a,b):
    return a*b

def fun_div(a,b):
    return a/b if b != 0 else 0.0

def math_fun(list_nums, op):
    res = op(float(list_nums[0]), float(list_nums[1]))
    if res.is_integer():
        return str(int(res))
    else:
        return str(res)
