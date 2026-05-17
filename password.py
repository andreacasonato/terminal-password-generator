#!/usr/bin/env python3
"""Password Generator: generate secure passwords with configurable options."""

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Generate secure random passwords."
    )

    parser.add_argument(
        "--length",
        type=int,
        help="Password length (minimum 10)"
    )
    parser.add_argument(
        "--count",
        type=int,
        help="How many passwords to generate"
    )

    args = parser.parse_args()

    # Temporary: confirm we received the arguments
    print(f"Length: {args.length}")
    print(f"Count: {args.count}")


if __name__ == "__main__":
    main()