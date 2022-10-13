'''Your task is to make a function that can take any non-negative integer as an argument 
and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321'''
def descending_order(num):
    #step 1: convert the number into positive and into list
    #step 2: sort the list using sorted built in function dont forget the key [int]
    #step 3: reverse the array and then join all the number and convert them into integer
    arr = int(''.join(sorted(list(str(abs(num)))[::-1], key=int)[::-1]))
    return arr

#shortcut
'''
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
'''