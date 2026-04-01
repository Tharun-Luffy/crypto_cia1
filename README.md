# Crypto Project: Myszkowski Cipher & FNV-1a Hash

This repository contains Python implementations of a custom cipher and a custom hashing function, created entirely from scratch without the use of built-in cryptography libraries (as per assignment constraints).

## 1. Theory behind the Cipher: Myszkowski Transposition

The **Myszkowski cipher** is a classic variant of the columnar transposition cipher, proposed by Émile Victor Portier. 
In a standard columnar transposition, a predefined keyword determines the order in which columns of the padded plaintext grid are read. If the keyword contains repeated letters (like the two 'O's in "TOMATO"), the standard cipher reads the corresponding columns one by one from left to right.

In the **Myszkowski transposition**, repeated letters in the keyword are grouped together. When it is time to read the columns assigned to that repeated letter, the text is read left-to-right, row-by-row across *all* columns sharing that letter's rank. This horizontally weaves the letters, scrambling the text more effectively by breaking up vertical column structures.

## 2. Theory behind the Hash: Custom FNV-1a (64-bit)

For the hashing requirement, this project implements a custom 64-bit **FNV-1a (Fowler-Noll-Vo)** hash function from scratch.
The FNV-1a algorithm is designed for fast, consistent, and well-distributed non-cryptographic hashing. It works by:
1. Initializing a 64-bit hash state with an offset basis (`14695981039346656037`).
2. Processing each byte of the input text by first XOR-ing the bottom byte of the current hash with the input byte.
3. Multiplying the resulting hash state by a specific 64-bit FNV prime (`1099511628211`), keeping the bounds to 64-bits.

This simple and elegant mathematical mechanism provides a rapid avalanche effect, meaning small changes in the message generate vastly different 16-character hexadecimal outputs.

## Instructions to Run the Code

1. Ensure you have Python 3 installed.
2. Open your terminal or command prompt.
3. Run the main testing script:

```bash
python3 test_script.py
```

This script will run through the worked examples natively and demonstrate the full `encrypt -> hash -> decrypt` lifecycle.

## Worked Examples

Below are the successful outputs from executing the `test_script.py`:

### Example 1
**Original Plaintext**: WE ARE DISCOVERED FLEE AT ONCE
**Keyword**: TOMATO

1. **Hash of Original Plaintext (FNV-1a)**: `6ff66d61da73932b`
2. **Ciphertext**: `ROFOXACDTXEDSEEEACXXWEIVRLENEX`
   - **Hash of Ciphertext in Transit**: `eda824cba33bfcf9`
3. **Decrypted Text (Padded with X's)**: `WEAREDISCOVEREDFLEEATONCEXXXXX`
4. **Hash of Decrypted Data (Padded)**: `7379b1ff5cc78519`
*(Integrity check against original length: True)*

### Example 2
**Original Plaintext**: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
**Keyword**: CRYPTOGRAPHY

1. **Hash of Original Plaintext (FNV-1a)**: `26df64d0f8e9fb94`
2. **Ciphertext**: `BSDTNRCMZOVGIUAQRXOEOHKFPTYUJLEWOEHX`
   - **Hash of Ciphertext in Transit**: `c9c5e4411c6f148a`
3. **Decrypted Text (Padded with X's)**: `THEQUICKBROWNFOXJUMPSOVERTHELAZYDOGX`
4. **Hash of Decrypted Data (Padded)**: `f7941b16f596dba4`
*(Integrity check against original length: True)*
