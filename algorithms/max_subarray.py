
def max_subarray(a):
    # Check if all negative
    if max(a) < 0:
        return min(a)
    max_tillnow = max_overall =0
    for i in range(0, len(a)):
        if max_tillnow + a[i] < 0:
            max_tillnow = 0
        else:
            max_tillnow+=a[i] 
        if max_tillnow > max_overall:
            max_overall = max_tillnow

    return max_overall
         

a = [-1,4,5,-3,8]
print a
print max_subarray(a)
        
