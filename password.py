#!/usr/bin/env python3
"""Password Generator: generate secure passwords with configurable options."""

import argparse
import secrets
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


def build_charset() -> str:
    return (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )


# Generate one secure password of a given length
def generate_password(length: int, charset: str) -> str:
    # Guarantee at least one character from each required group.
    required = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    # Fill the rest of the password with random characters
    # length - 4 because we already have 4 required characters
    rest = [secrets.choice(charset) for _ in range(length - 4)]

    # Combine required + rest, then shuffle so the required
    # characters don't always appear at the start
    # secrets.SystemRandom().shuffle() is the secure version of shuffle
    password_chars = required + rest
    secrets.SystemRandom().shuffle(password_chars)

    # Join the list of characters into a single string
    return "".join(password_chars)


def main():
    parser = argparse.ArgumentParser(
        description="Generate secure random passwords."
    )
    parser.add_argument("--length", type=int, help="Password length (minimum 10)")
    parser.add_argument("--count", type=int, help="How many passwords to generate")
    args = parser.parse_args()

    length = args.length if args.length and args.length >= 10 else ask_length()
    count = args.count if args.count and args.count >= 1 else ask_count()

    charset = build_charset()

    # Generate and print one password to test
    password = generate_password(length, charset)
    print(f"\nGenerated: {password}")


if __name__ == "__main__":
    main()