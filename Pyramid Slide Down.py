'''
Lyrics...
Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer, you can mess with pyramids even if you are not in Egypt at the time. For example, let's consider the following problem. Imagine that you have a pyramid built of numbers, like this one here:

   /3/
  \7\ 4 
 2 \4\ 6 
8 5 \9\ 3
Here comes the task...
Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23

Your task is to write a function that takes a pyramid representation as argument and returns its' largest 'slide down'. For example:

* With the input `[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]`
* Your function should return `23`.
By the way...
My tests include some extraordinarily high pyramids so as you can guess, brute-force method is a bad idea unless you have a few centuries to waste. You must come up with something more clever than that.

(c) This task is a lyrical version of the Problem 18 and/or Problem 67 on ProjectEuler.
'''

def longest_slide_down(pyramid):
    #create the longest slide down list
    lsd = [0] * len(pyramid)
    #set the last row of the pyramid to the lsd
    lsd = pyramid[-1]
    #loop through the pyramid backwards
    for i in range(len(pyramid)-2, -1, -1):
        #loop through the current row of the pyramid
        for j in range(len(pyramid[i])):
            #set the current value in the lsd to the max of the two values below it
            lsd[j] = pyramid[i][j] + max(lsd[j], lsd[j+1])
    #return the first value in the lsd
    return lsd[0]

    


#shortcut
'''
def longest_slide_down(p):
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1])  for i in range(len(tmp))] 
    return res.pop()'''