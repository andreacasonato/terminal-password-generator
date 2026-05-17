#!/usr/bin/env python3
"""Password Generator: generate secure passwords with configurable options."""

import argparse


# Ask the user for a valid password length
def ask_length() -> int:
    while True:
        # input() prints the message and waits for the user to type
        raw = input("Password length (min 10): ")

        # Make sure it's a number
        if not raw.isdigit():
            print("  Please enter a valid number.")
            continue

        length = int(raw)

        # Enforce minimum length
        if length < 10:
            print("  Minimum length is 10 for security reasons.")
            continue

        # If we reach here, the input is valid, exit the loop
        return length


# Ask the user how many passwords they want
def ask_count() -> int:
    while True:
        raw = input("How many passwords? (default 1): ")

        # If the user just hits Enter, default to 1
        if raw.strip() == "":
            return 1

        if not raw.isdigit():
            print("  Please enter a valid number.")
            continue

        count = int(raw)

        if count < 1:
            print("  Please enter at least 1.")
            continue

        return count


def main():
    parser = argparse.ArgumentParser(
        description="Generate secure random passwords."
    )
    parser.add_argument("--length", type=int, help="Password length (minimum 10)")
    parser.add_argument("--count", type=int, help="How many passwords to generate")
    args = parser.parse_args()

    # Use the flag if provided, otherwise ask interactively
    # if args.length is not None, use it
    # without asking. Otherwise call ask_length() to prompt the user.
    length = args.length if args.length and args.length >= 10 else ask_length()
    count = args.count if args.count and args.count >= 1 else ask_count()

    print(f"\nGenerating {count} password(s) of length {length}...")


if __name__ == "__main__":
    main()