


def comp(array1, array2):
    array1 = list(array1)
    array2 = list(array2)

    if array1 ==array2:
        return True
    
    else:
        array1 = sorted(array1,key=int)
        array2 = sorted([int(x**0.5) for x in array2],key=int)
        if array1 ==array2:
            return True
        else:
            return False

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
print(comp(a1,a2))
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a,b))