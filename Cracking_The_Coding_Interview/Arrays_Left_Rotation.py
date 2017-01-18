def array_left_rotation(a, n, k):
    tmp_array = [0 for i in range(n)]
    for index, element in enumerate(a):
        number = a[index]
        tmp_array[index - k] = number
    return tmp_array

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
