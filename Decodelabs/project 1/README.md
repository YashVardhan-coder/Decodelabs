# 🔐 Password Strength Checker (CLI)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Security](https://img.shields.io/badge/Domain-Cyber%20Security-red.svg)]()
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

A lightweight, privacy-focused command-line tool written in Python to evaluate the resilience and complexity of user passwords. Built as part of the **Cyber Security Internship Project**, this tool provides instant, rule-based feedback to help users design robust passwords capable of resisting brute-force and dictionary attacks.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Password Evaluation Criteria](#password-evaluation-criteria)
- [Classification Matrix](#classification-matrix)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation & Setup](#installation--setup)
  - [Usage](#usage)
- [Sample Execution](#sample-execution)
- [Security & Privacy Standards](#security--privacy-standards)
- [Roadmap & Enhancements](#roadmap--enhancements)
- [Author & Acknowledgments](#author--acknowledgments)

---

## 📖 Overview

In modern cybersecurity, weak and compromised credentials remain the primary entry point for unauthorized data breaches. This Password Strength Checker enforces industry-standard security guidelines (aligned with NIST recommendations) by evaluating both **length** and **character entropy** in real-time without storing or transmitting sensitive input.

---

## ✨ Features

- **Length Enforcement**: Mandates a strict minimum baseline of **8 characters**.
- **Multi-Factor Diversity Check**:
  - 🔤 **Uppercase letters** (`A-Z`)
  - 🔡 **Lowercase letters** (`a-z`)
  - 🔢 **Numeric digits** (`0-9`)
  - 🔣 **Special symbols** (via Python's standard `string.punctuation`)
- **4-Tier Scoring Classification**: Categorizes passwords into `Weak`, `Medium`, `Strong`, and `Very Strong`.
- **Interactive CLI Loop**: Allows users to test multiple passwords consecutively without restarting the script.
- **Zero Third-Party Dependencies**: Powered entirely by Python standard libraries (`string`).
- **Privacy-First**: No data is logged, transmitted, or written to disk. All evaluations happen in memory.

---

## 🎯 Password Evaluation Criteria

The tool assesses passwords across two primary dimensions:

1. **Length Factor**: 
   - Passwords shorter than 8 characters fail immediately and receive a **Weak** rating, regardless of character diversity.
   - Passwords with length $\ge 12$ characters with full character coverage qualify for the **Very Strong** tier.
2. **Character Diversity Factor**:
   - Each unique character family (Uppercase, Lowercase, Number, Symbol) adds **1 point** to a maximum diversity score of **4**.

---

## 📊 Classification Matrix

| Category | Minimum Length | Character Diversity Score | Description / Recommendation |
| :--- | :---: | :---: | :--- |
| **Weak** | $< 8$ characters | Any ($0 - 4$) | Fails minimum length threshold. Vulnerable to fast brute-force attacks. |
| **Weak** | $\ge 8$ characters | $< 2$ types | Insufficient character variety (e.g., all lowercase or only numbers). |
| **Medium** | $\ge 8$ characters | $2 - 3$ types | Moderate security. Recommended to add missing character sets. |
| **Strong** | $\ge 8$ characters | All $4$ types | High resilience. Contains uppercase, lowercase, numbers, and symbols. |
| **Very Strong** | $\ge 12$ characters | All $4$ types | Enterprise-grade strength. Highly resistant to offline hash cracking. |

---

## 📂 Project Structure

```text
cyber-security-project1/
│
├── main.py       # Core CLI application and password evaluation logic
└── README.md     # Project documentation and user guide
```

---

## 🚀 Getting Started

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/) installed on your operating system.
- Git (optional, for cloning).

Verify your Python installation:
```bash
python --version
```

### Installation & Setup

1. **Clone the repository**:
   ```bash
   (https://github.com/YashVardhan-coder/Decodelabs.git)
   ```

2. **Verify the environment**:
   No virtual environment or `pip install` required! The script runs out of the box with standard Python.

### Usage

Run the script from your terminal:
```bash
python main.py
```

Follow the on-screen prompts to input passwords and observe real-time strength evaluations.

---

## 🖥️ Sample Execution

```text
$ python main.py
Enter a password to check: pass12
Password Strength: Weak (Password length must be at least 8 characters)

Do you want to check another password? (Yes/No): yes
Enter a password to check: Password123
Password Strength: Medium (Consider adding more character types)

Do you want to check another password? (Yes/No): yes
Enter a password to check: P@ssw0rd2026
Password Strength: Strong (Contains uppercase, lowercase, digits, and symbols)

Do you want to check another password? (Yes/No): yes
Enter a password to check: C0mpl3x#P@ssw0rd!2026
Password Strength: Very Strong (Excellent length and character diversity)

Do you want to check another password? (Yes/No): no
Goodbye!
```

---

## 🛡️ Security & Privacy Standards

- **Zero-Storage Guarantee**: The application does not store, log, or transmit input credentials.
- **Short-Circuit Evaluation**: Employs Python's built-in `any()` generator expressions to optimize search speed and minimize runtime footprint.
- **Brute-Force Mitigation Awareness**: Enforcing length $\ge 12$ with 4 character sets exponentially increases the search space ($94^{12} \approx 4.75 \times 10^{23}$ combinations), rendering standard brute-force cracking practically infeasible.

---

## 🗺️ Roadmap & Enhancements

- [ ] **Masked Password Input**: Integrate `getpass` to hide input typing from shoulder-surfing.
- [ ] **Breach Detection**: Integrate with HaveIBeenPwned k-Anonymity API to flag compromised passwords.
- [ ] **Common Pattern & Wordlist Blacklist**: Detect common patterns like `123456`, `qwerty`, or dictionary words.
- [ ] **Shannon Entropy Scoring**: Provide exact mathematical entropy (bits) calculation.

---

## 👤 Author & Acknowledgments

- **Developer**: Yash Vardhan
- **Domain**: Cyber Security Internship Project
- **Special Thanks**: Mentors and contributors for feedback on security best practices.
