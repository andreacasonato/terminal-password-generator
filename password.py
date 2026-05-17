#!/usr/bin/env python3
"""Password Generator: generate secure passwords with configurable options."""

import argparse
import string


def ask_length() -> int:
    while True:
        raw = input("Password length (min 10): ")
        if not raw.isdigit():
            print("  Please enter a valid number.")
            continue
        length = int(raw)
        if length < 10:
            print("  Minimum length is 10 for security reasons.")
            continue
        return length


def ask_count() -> int:
    while True:
        raw = input("How many passwords? (default 1): ")
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


# Build the character set every password must use
def build_charset() -> str:
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Concatenate all four into one long string of allowed characters
    charset = lowercase + uppercase + digits + symbols

    print(f"\nCharacter set: {len(charset)} characters available")
    print(f"  Lowercase:  {lowercase}")
    print(f"  Uppercase:  {uppercase}")
    print(f"  Digits:     {digits}")
    print(f"  Symbols:    {symbols}")

    return charset


def main():
    parser = argparse.ArgumentParser(
        description="Generate secure random passwords."
    )
    parser.add_argument("--length", type=int, help="Password length (minimum 10)")
    parser.add_argument("--count", type=int, help="How many passwords to generate")
    args = parser.parse_args()

    length = args.length if args.length and args.length >= 10 else ask_length()
    count = args.count if args.count and args.count >= 1 else ask_count()

    # Build the character set
    charset = build_charset()

    print(f"\nGenerating {count} password(s) of length {length}...")


if __name__ == "__main__":
    main()