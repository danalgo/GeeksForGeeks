
def perm(s, p):
    if len(s) is 0:
        print p
    for i in range(0, len(s)):
        perm(s.replace(s[i],''),p+s[i])

if __name__ == '__main__':
    perm('', '')
