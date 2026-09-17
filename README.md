# Secure Password Tool

A Python-based command-line tool for generating secure passwords and checking password strength.

## Features

- Generate random passwords using Python's `secrets` module
- Choose password length between 8 and 50 characters
- Choose uppercase letters
- Choose lowercase letters
- Choose numbers
- Choose special characters
- Check password strength
- Provides suggestions for improving weak passwords
- Does not store generated passwords

## Technologies Used

- Python
- secrets
- string

## Password Strength Criteria

The password is evaluated based on five criteria:

1. At least 8 characters
2. Contains uppercase letters
3. Contains lowercase letters
4. Contains numbers
5. Contains special characters

### Strength Levels

| Score | Strength |
|------:|----------|
| 0–2 | WEAK |
| 3–4 | MEDIUM |
| 5 | VERY STRONG |

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/PathapalliSowmya/Secure-Password-Tool.git