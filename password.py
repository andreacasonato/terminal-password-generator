"""
Password Generator: generate secure random passwords.

Usage:
    python3 password.py
    python3 password.py --length 16 --count 5
"""

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


def generate_password(length: int, charset: str) -> str:
    required = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]
    rest = [secrets.choice(charset) for _ in range(length - 4)]
    password_chars = required + rest
    secrets.SystemRandom().shuffle(password_chars)
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

    # NEW: generate and print all passwords, numbered
    print()
    for i in range(count):
        password = generate_password(length, charset)
        print(f"  {i + 1}. {password}")
    print()


if __name__ == "__main__":
    main()