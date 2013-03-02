import random

def fisher_yates_original(arr):
    art = []
    for index, i in enumerate(arr):
        k = random.randint(0,(len(arr)-index-1))
        arr[k],arr[-1+index] = arr[-1+index], arr[k]
        art.append(arr[k])
    print art

def sort_shuffle(arr):
    arrt = []
    for i in arr:
        arrt.append((i,random.randint(1,100)))

    print [ i[0] for i in sorted(arrt, key=lambda a: a[1]) ]

arr_orig = [4,6,8,9,3,0]
print 'Input: ', arr_orig
print '------------'
for i in range(10):
    arr = arr_orig
    #fisher_yates_original(arr)
    sort_shuffle(arr)
