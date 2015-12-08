__author__ = 'rauts3'

def _findmultiples_(num):
    sumtotal = 0
    for i in range(1, num+1):
        if num % i == 0:
            sumtotal += i
    return sumtotal


def _finddeficient_(num, sumtotal):
     if sumtotal < 2*num:
         print("Number is dificient by " + str(2*num - sumtotal))
     elif sumtotal == num:
         print("Number is perfect " )
     else:
         print("Number is abundant by " + str(sumtotal-2*num))


if __name__ == "__main__":
    ret_num = input("Enter a number: ")
    num = int(ret_num)
    if num > 0:
        sumtotal = _findmultiples_(num)
        _finddeficient_(num, sumtotal)