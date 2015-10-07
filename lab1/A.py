__author__ = 'dantipov'


def flip(char):
    if char == '0':
        return '1'
    return '0'

n = int(input())

s, cur = ['0'] * n, 0

print(''.join(s))
right = int(input())

while right != n:
    s[cur] = '1'
    print(''.join(s))
    if int(input()) < right:
        s[cur] = '0'
    else:
        right += 1
    cur += 1