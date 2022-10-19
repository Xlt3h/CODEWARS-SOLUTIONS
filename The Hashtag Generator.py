'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
'''
def generate_hashtag(s):    
    if len(s) > 140 or s == '':
        return False
    else:
        hashtag = "#"
        sen  = ' '.join(x.strip() for x in s.split()).split() #removing the spaces and leave spaces for words !!!
        for i in sen:
            hashtag+=i[0].upper()+ i[1::].lower()
        return hashtag

#print(generate_hashtag("    Hello     World  c  "))-
#print(generate_hashtag('CodeWars is nice'))

#shortcut
def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False

def generate_hashtag(s): return '#' +s.strip().title().replace(' ','') if 0<len(s)<=140 else False

