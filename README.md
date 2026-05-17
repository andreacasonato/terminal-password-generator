# Password Generator

Generates secure random passwords with configurable length and quantity. Every password always contains uppercase, lowercase, digits, and symbols — no exceptions.

## Usage

```bash
python3 password.py
```

Or skip the prompts with flags:

```bash
python3 password.py --length 16 --count 5
```

## Example

```
Password length (min 10): 16
How many passwords? (default 1): 3

  1. kR7mNpQ2xLvBj49s
  2. Tz4wYcD8nFsXm1qp
  3. Qj9bVeR5pKwNt2yz
```

## Security rules

- Minimum length is 10 characters
- Every password always includes lowercase, uppercase, digits, and symbols
- Uses Python's `secrets` module — cryptographically secure, not `random`