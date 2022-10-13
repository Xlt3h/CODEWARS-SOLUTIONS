'''
Write a function that takes an integer as input, and 
returns the number of bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.
Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''
def count_bits(n):
    bin_ = int(bin(abs(n))[2::])
    counts  = str(bin_).count('1')
    return int(counts)


#shortcut
'''
def countBits(n):
    return bin(n).count("1")
'''