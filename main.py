#!/usr/bin/python3 


def main():
    name = input("Please enter your name: " )
    print(f"Hello from Python {name}" )
    return name


def sayGoodBye(name):
    print(f"Goodbye {name}")


if __name__ ==  "__main__":
    name = main()
    sayGoodBye(name)
