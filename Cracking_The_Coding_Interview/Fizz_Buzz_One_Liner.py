def fizz_buzz(n):
    return "\n".join(["FizzBuzz"[i*i%3*4:8--i**4%5] or str(i) for i in range(1,n)])

def fizz_buzz_alternative(n):
    return "\n".join(['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n)])


print(fizz_buzz(101))
print(fizz_buzz_alternative(101))