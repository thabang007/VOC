<<<<<<< HEAD
def print_twice(input: str):
    str = input
    print(str*2)
def print_reversed (input: str):
    text = input[::-1]
    print(text)
=======
def print_header():
    print("Thanks, now I'll print your string reversed, and twice")
>>>>>>> 42b98fc (print header function)
if __name__ == "__main__":
    s = input()
    print_header()
    print_reversed(s)
    print_twice(s)