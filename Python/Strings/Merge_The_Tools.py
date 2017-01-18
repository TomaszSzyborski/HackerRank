from collections import OrderedDict

def merge_the_tools(string, k):
    #print(*[iter(string)] * k)
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

#Test Input
string = "AABCAAADA"
k = 3
#Test Output
output = "AB\nCA\nAD"

print("Actual result:")
merge_the_tools(string, k)
print("Expected result:")
print(output)