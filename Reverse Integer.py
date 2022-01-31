def reverse(x):
    def strip_zero(n):
        x = str(n//10)
        x = x[::-1]
        return int(x)
    def thirty_two_bit_checker(num):
        if (num>2**31 -1) or (num<(-2)**31):
            return 0
        else:
            return num
    if x == 0:
        return 0
    elif x>0:
        if x%10 == 0:
            return thirty_two_bit_checker(strip_zero(x))
        else:
            return thirty_two_bit_checker(int(str(x)[::-1]))
    else:
        if x%10 == 0:
            return thirty_two_bit_checker(-strip_zero((-1)*x))
        else:
            return thirty_two_bit_checker(-int(str(-x)[::-1]))
