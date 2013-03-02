"""
Fin the number of contigous arrays with two or one different element
"""
import copy

COUNT=0

def conti(x, s, index, di):
    global COUNT
    temp_x = copy.deepcopy(x)
    if len(di) is 1 or len(di) is 2:
        print ''.join(x),
        COUNT+=1
    if len(di) >2 :
        return
    for i in range(index, len(s)):
        present = False
        temp_x.append(s[i])
        if di.has_key(s[i]):
            present = True
        else:
            di[s[i]] = 1
        #print temp_x, s[i+1:]
        conti(temp_x, s, i+1, di)
        if not present:
            del(di[s[i]])
        del(temp_x[0])

def conti_n(s):
    a = [0]
    for i in range(1,len(s)):
        if s[i-1] is s[i]:
            a.append(0)
        else:
            a.append(1)

    curr, prev = 1, 1
    for i in range(1,len(a)):
        if (a[i] is 0) or (a[i-1] is 0 and a[i] is 1):
            curr+=prev+1
            prev=prev+1
        elif a[i-1] is 1 and a[i] is 1:
            curr+=2
            prev=2
    print 'Iterative', curr
    
            
        
        
        

conti([],'aab',0,{})
print COUNT
conti_n('aab')
