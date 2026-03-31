Myszkowski Cipher Experiments

This repository contains two different Python implementations of the Myszkowski Cipher, a classic encryption method that moves letters around (transposition) based on a keyword.
1. Hashed Key Cipher (myszkowski.py)

In this version, we use a Password to lock and unlock a message.
How it works:

    The Hashed Password: Instead of using your password directly, the code uses a "Digital Blender" (SHA-256 Hash) to turn your password into a long list of random-looking numbers.

    The Grid: Your message is written into a table (like an Excel sheet).

    The Scramble: The code looks at the random numbers from your password to decide which columns of the table to pick up first.

    The Twist: If two columns have the same "priority number," the code reads them horizontally instead of vertically. This makes the code much harder to break than a standard cipher.

Use Case: Sending a secret message to a friend where you both know the password.


2. Self-Hashing Plaintext (plaintext-hashing.py)

In this version, we don't use a password. Instead, the message scrambles itself.
How it works:

    Message as the Key: The code looks at the letters inside your message (like "ALGORITHMS") and uses their alphabetical order to decide the shuffling pattern.

    The Square Grid: It automatically calculates the best square-shaped table to fit your message.

    The Fingerprint: Because the message decides its own shuffle, if you change even one letter of the original text, the entire scrambled result will look completely different.

Use Case: Creating a "Digital Fingerprint" or a unique ID for a piece of text to see if it has been changed or tampered with.
