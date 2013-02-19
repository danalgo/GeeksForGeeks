"""
Suppose there is a circle. There are n petrol pumps on that circle. You are given two sets of data.

1. The amount of petrol that petrol pump will give.
2. Distance from that petrol pump to the next petrol pump.

Calculate the first point from where a truck will be able to complete the circle (The truck will stop at each petrol pump and it has infinite capacity). Expected time complexity is O(n). Assume for 1 litre petrol, the truck can go 1 unit of distance.
"""

def find_start_point(p, d):
    # Check for if solution exist
    if sum(p) < sum(d):
        print 'Solution do not exist'
        return None 
    startpoint, ssum = 0, 0
    for i in range(0, len(p)):
        ssum+=p[i]-d[i]
        if ssum < 0:
            # Petrol pumps will lie in the forward indexes
            startpoint = i+1
            ssum = 0
    return p[startpoint]

if __name__=='__main__':
    p = [6,7,1,4]
    d = [5,8,3,2]
    print find_start_point(p, d)
