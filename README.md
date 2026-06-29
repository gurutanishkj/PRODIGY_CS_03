# PRODIGY_CS_03

## Password Complexity Checker

### Prodigy InfoTech Cyber Security Internship – Task 03

## Description

A Python-based Password Complexity Checker that evaluates the strength of a password based on its length and the presence of uppercase letters, lowercase letters, numbers, and special characters. The application features a graphical user interface (GUI) built using Tkinter and provides real-time feedback to help users create stronger and more secure passwords.

## Features

- Checks password length.
- Detects uppercase letters.
- Detects lowercase letters.
- Detects numeric digits.
- Detects special characters.
- Displays password strength as Weak, Moderate, or Strong.
- Shows a progress bar indicating password strength.
- Provides suggestions to improve weak passwords.
- Includes Show/Hide password functionality.
- Real-time password analysis.

## How It Works

- The user enters a password in the input field.
- The application checks whether the password meets the required security criteria.
- A score is calculated based on the satisfied conditions.
- According to the score, the password is classified as Weak, Moderate, or Strong.
- The progress bar updates automatically.
- If any requirement is missing, suggestions are displayed to help improve the password.

## Code Explanation

- `check_password_strength()` evaluates the password against different security criteria.
- `re.search()` is used to detect uppercase letters, lowercase letters, numbers, and special characters.
- `update_strength()` updates the password strength, progress bar, and feedback in real time.
- `toggle_password()` allows users to show or hide the entered password.
- `ttk.Progressbar()` visually represents the password strength.

## Technologies Used

- Python 3
- Tkinter
- ttk
- Regular Expressions (re)

## How to Run

```bash
python Password_Complexity_Checker.py
```

## Example

### Weak Password

**Input**

```
guru
```

**Output**

```
Password Strength: Weak Password

Suggestions:
- At least 8 characters required
- Add uppercase letter (A-Z)
- Add a number (0-9)
- Add a special character
```

### Moderate Password

**Input**

```
Guru30
```

**Output**

```
Password Strength: Moderate Password

Suggestions:
- Add a special character
```

### Strong Password

**Input**

```
Guru_30
```

**Output**

```
Password Strength: Strong Password

Perfect! All criteria met!
```

## Learning Outcomes

- Password Security Concepts
- Password Complexity Validation
- Regular Expressions in Python
- GUI Development using Tkinter
- Real-time User Feedback
- Python Event Handling

## Internship Details

**Organization:** Prodigy InfoTech

**Domain:** Cyber Security

**Task:** Task 03 – Password Complexity Checker
