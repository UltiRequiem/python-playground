def return_msg(msg: str = "Hello"):
    def returner() -> str:
        return msg

    return returner


say_cheese = return_msg("cheese")

say_hello = return_msg()

if __name__ == "__main__":
    print(say_hello())
    print(say_cheese())
