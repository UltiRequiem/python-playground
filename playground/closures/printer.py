def print_msg(msg: str = "Hello"):
    def printer() -> str:
        print(msg)
        return msg # For the tests :)

    # printer = lambda: print(msg)

    return printer


say_cheese = print_msg("cheese")
say_cheese()

say_hello = print_msg()
say_hello()
