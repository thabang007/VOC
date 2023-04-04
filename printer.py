def print_twice(input: str):
    str = input
    print(str*2)
def print_reversed (input: str):
    text = input[::-1]
    print(text)
if __name__ == "__main__":
    s = input()
    print_reversed(s)
    print_twice(s)