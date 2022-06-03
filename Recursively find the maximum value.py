data = list(range(30))

import random
random.shuffle(data)

def getmax(left, right):
    
    if left == right:
        return data[left]
    mid = left + int((right-left)>>1)
    print(left, end='\t')
    print(right, end='\t')
    print(mid)
    
    left_max = getmax(left, mid)
    right_max = getmax(mid + 1, right)
    return max(left_max, right_max)

print( 'getmax =', getmax(0, len(data)-1) )

'''
0	29	14
0	14	7
0	7	3
0	3	1
0	1	0
2	3	2
4	7	5
4	5	4
6	7	6
8	14	11
8	11	9
8	9	8
10	11	10
12	14	13
12	13	12
15	29	22
15	22	18
15	18	16
15	16	15
17	18	17
19	22	20
19	20	19
21	22	21
23	29	26
23	26	24
23	24	23
25	26	25
27	29	28
27	28	27
getmax = 29
'''
