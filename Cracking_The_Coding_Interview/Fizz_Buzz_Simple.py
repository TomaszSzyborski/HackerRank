def fizz_buzz(n):
    for i in range(n):
        string = ""
        if not i % 3 or not i % 5:
            if not i % 3:
                string+="Fizz"
            if not i % 5:
                string+="Buzz"
        else:
            string=str(i)
        print(string)

def fizz_buzz_ternary(n):
    #a if condition else b
    for i in range(n):
        print('Fizz' * (not i % 3) + 'Buzz' * (not i % 5) if not i % 3 or not i % 5 else str(i))

#fizz_buzz(101)
fizz_buzz_ternary(101)