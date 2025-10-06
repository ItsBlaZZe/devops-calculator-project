from typing import Callable
from .core import add, sub, mul, div

OPS: dict[str, Callable[[float, float], float]] = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
}

def _read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main() -> None:
    print("Calculator CLI – type 'quit' to exit.")
    while True:
        op = input("Choose op: add, sub, mul, div (or quit): ").strip().lower()
        if op == "quit":
            print("Bye!")
            break
        if op not in OPS:
            print("Unknown op. Try again.")
            continue
        a = _read_float("First number: ")
        b = _read_float("Second number: ")
        try:
            result = OPS[op](a, b)
            print(f"Result: {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
