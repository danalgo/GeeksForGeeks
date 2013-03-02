
def min_palindrome(arr):
    l=start = 0
    r = end = len(arr) - 1
    first = True
 
    while ( l < len(arr)):
        if (l is r or (l is r-1 and arr[l] is arr[r])):
            print end
            r = len(arr) - 1
            first = True
            l = end + 1
            end = r
        elif arr[l] is arr[r]:
            if first:
                end = r
                first = False
                start = l
            l=l+1
            r=r-1
        else:
            if not first:
                r=r-1
            end = r
            first = True
            l=start

if __name__=='__main__':
    arr = ['a','b','a','b','c','b']
    arr = ['a','b']
    arr = ['a','a','b','a']
    arr = ['a','a','c','a','b','a']
    min_palindrome(arr)
