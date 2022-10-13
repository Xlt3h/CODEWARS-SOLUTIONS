'''
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.

Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]
'''

eyes = [':', ';']

nose = ['-','~']

smile = [')','D']

def count_smileys(arr):
    #count number of smiles
    count = 0
    for i in arr:
        if len(i) == 2:
            print(i[0])
            if i[0] in eyes and i[1] in smile:
                count += 1
        elif len(i) == 3:
            if i[0] in eyes and i[1] in nose and i[2] in smile:
                count += 1
    return count
#test
print(count_smileys([':)', ';(', ';}', ':-D']))

#shortcut
'''
from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))

def count_smileys(arr):
    count = 0
    if not arr:
      return 0
    smileys = [":)", ";)", ":~)", ";~)", ":-)", ";-)", ":D", ";D", ":~D", ";~D", ":-D", ";-D"]
    for i in arr:
      if i in smileys:
        count += 1
    return count


valid = ":) :D :-) :-D :~) :~D ;) ;D ;-) ;-D ;~) ;~D".split()

def count_smileys(arr):
    return sum(face in valid for face in arr)
'''