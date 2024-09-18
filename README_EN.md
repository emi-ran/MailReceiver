# Email Checker

You can get information about this project in Turkish and English.

- [Türkçe Dokümantasyon (Varsayılan)](README.md)
- [English Documentation](README_EN.md)

## Description

This Python program checks your email accounts and prints the content of the latest email.

## Features

- Connects to an email account using IMAP.
- Prints the latest sent email.
- Supports asynchronous operations for efficiency.

## Requirements

- Python 3.7+
- `imaplib`, `email`, `asyncio`, `pickle` (Standard Python libraries)

## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/emi-ran/Outlook-Mail-Receiver.git
    ```

2. **Navigate to the Project Directory**

    ```bash
    cd MailReceiver
    ```

3. **Install Dependencies**

    This project does not require any external dependencies.

4. **Create Email Credentials File**

    Create a `mails.txt` file with email credentials in the following format:

    ```plaintext
    email@example.com:password
    anotheremail@example.com:anotherpassword
    ```

5. **Run the Program**

    ```bash
    python main.py
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
