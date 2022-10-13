'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
'''

def find_it(seq):
    num = 0 #number to return for odd number

    if(len(seq) == 1): #if the length of the seq is one return that number
        return seq[0]
    else: 
        counts = {} #else create a dictionary and count  the number of elements in the array [seq]
        for i in seq:
            counts[i] = seq.count(i)
        for i in counts: #if the count of element is odd return the key
            if counts[i]%2 == 1:
                num += i
        return num
#test
# print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
# #print(find_it([0,1,0,1,0]))
# print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

'''
shortcut
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
'''