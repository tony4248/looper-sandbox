import argparse


def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument("--name", default="World", help="Name to greet (default: World)")
    args = parser.parse_args()
    print(greet(args.name))
