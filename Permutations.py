#descriptions [this was difficult for me lol good luck ]
'''
In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

* With input 'a'
* Your function should return: ['a']
* With input 'ab'
* Your function should return ['ab', 'ba']
* With input 'aabb'
* Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
'''
def permutations(s):
    from itertools import permutations as p #imoprt permutations from itertools 
    new_array = [''.join(p) for p in p("".join(s))]
    return list(dict.fromkeys(new_array)) #remove the duplicates from the list

      
#testing
#print(permutations(['aabb']))

#shortcuts