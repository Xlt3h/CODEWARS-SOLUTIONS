def to_camel_case(text):
    arr_for_dash = [i for i,e in enumerate(text) if e == '-']
    arr_for_under = [i for i,e in enumerate(text) if e == '_']
    v = ''
    arr_for_under = [i for i,e in enumerate(text) if e == '_']

    
    if '_' and '-' in text:
        if '-' in text:
            
            for i in arr_for_dash:
                v =text.replace(text[i],'')
            first_dash = arr_for_dash[0]
            arr_dash = [i for i in arr_for_dash[1:]]
            arr_dash_ = []
            count = 1
            for i in arr_dash:
                i-=count
                arr_dash_.append(i)
                count+=1
            arr_dash = arr_dash_
            arr_for_dash = []
            arr_for_dash.append(first_dash)
            for i in arr_dash:
                arr_for_dash.append(i)
            
            for i in arr_for_dash:
                v = "".join(c.upper() if i in arr_for_dash else c for i,c in enumerate(v))
            
            if '_' in v:
                arr_for_under = [i for i,e in enumerate(v) if e == '_']
                v = v.replace(v[arr_for_under[0]],'')
                
                first_under = arr_for_under[0]
                arr_under = [i for i in arr_for_under[1:]]
                arr_under_ = []
                count = 1
                for i in arr_under:
                    i-=count
                    arr_under_.append(i)
                    count+=1
                arr_under = arr_under_
                arr_for_under = []
                arr_for_under.append(first_under)
                for i in arr_under:
                    arr_for_under.append(i)
           
                for i in arr_for_under:
                    v = "".join(c.upper() if i in arr_for_under else c for i,c in enumerate(v))
                return v
        else:
            pass
    arr_for_dash = [i for i,e in enumerate(text) if e == '-']
    arr_for_under = [i for i,e in enumerate(text) if e == '_']
    if '-' in text:
        
        for i in arr_for_dash:
            v =text.replace(text[i],'')
        first_dash = arr_for_dash[0]
        arr_dash = [i for i in arr_for_dash[1:]]
        arr_dash_ = []
        count = 1
        for i in arr_dash:
            i-=count
            arr_dash_.append(i)
            count+=1
        arr_dash = arr_dash_
        arr_for_dash = []
        arr_for_dash.append(first_dash)
        for i in arr_dash:
            arr_for_dash.append(i)
        
        for i in arr_for_dash:
            v = "".join(c.upper() if i in arr_for_dash else c for i,c in enumerate(v))
        return v
    else:
        pass
    
    if '_' in text:
        for i in arr_for_under:
            v =text.replace(text[i],'')
        first_under = arr_for_under[0]
        arr_under = [i for i in arr_for_under[1:]]
        arr_under_ = []
        count = 1
        for i in arr_under:
            i-=count
            arr_under_.append(i)
            count+=1
        arr_under = arr_under_
        arr_for_under = []
        arr_for_under.append(first_under)
        for i in arr_under:
            arr_for_under.append(i)
       
        for i in arr_for_under:
            v = "".join(c.upper() if i in arr_for_under else c for i,c in enumerate(v))
        return v
    else:
        pass
    return text
#short cut
'''
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s

def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')

def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])
'''
