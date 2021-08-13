def print_msg(msg: str = "Hello"):
    def printer() -> str:
        print(msg)
        return msg # For the tests :)

    # printer = lambda: print(msg)

    return printer


say_cheese = print_msg("cheese")

say_hello = print_msg()

if __name__ == "__main__":
    say_hello()
    say_cheese()
