"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    >>> read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
    >>> read_numbers(5)
    No numbers entered

"""


def read_numbers(n: int) -> str:
    total = 0.0
    count = 0 
    for i in range(n):
        print(f"enter {i+1}th number: ")
        user_input = input()
        try:
            num = float(user_input)
            total += num
            count += 1
        except ValueError:
            continue
    
    if count == 0:
        return "No numbers entered"
    
    avg = total / count
    return f"Avg: {avg: .2f}"


print(read_numbers(5))
print(read_numbers(5))

