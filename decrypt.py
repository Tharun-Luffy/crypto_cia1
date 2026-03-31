import hashlib
import math

def get_hash_ranks(passphrase, num_cols):
    """Generates deterministic column ranks using SHA-256."""
    hash_digest = hashlib.sha256(passphrase.encode()).digest()
    # Use bytes from the hash to create ranks
    ranks = [hash_digest[i % len(hash_digest)] for i in range(num_cols)]
    return ranks

def encrypt_hashed_myszkowski(text, passphrase, num_cols=6):
    """Encrypts text using the Myszkowski transposition rules with a hashed key."""
    text = text.replace(" ", "").upper()
    col_ranks = get_hash_ranks(passphrase, num_cols)
    
    num_rows = math.ceil(len(text) / num_cols)
    text = text.ljust(num_rows * num_cols, 'X') # Padding with X
    grid = [text[i:i + num_cols] for i in range(0, len(text), num_cols)]
    
    unique_ranks = sorted(list(set(col_ranks)))
    ciphertext = ""
    
    for rank in unique_ranks:
        target_cols = [i for i, r in enumerate(col_ranks) if r == rank]
        if len(target_cols) == 1:
            col_idx = target_cols[0]
            for row in grid:
                ciphertext += row[col_idx]
        else:
            for row in grid:
                for col_idx in target_cols:
                    ciphertext += row[col_idx]
    return ciphertext

def decrypt_hashed_myszkowski(ciphertext, passphrase, num_cols=8):
    """Reverses the hashed Myszkowski transposition."""
    col_ranks = get_hash_ranks(passphrase, num_cols)
    num_rows = len(ciphertext) // num_cols
    
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    unique_ranks = sorted(list(set(col_ranks)))
    current_pos = 0
    
    for rank in unique_ranks:
        target_cols = [i for i, r in enumerate(col_ranks) if r == rank]
        if len(target_cols) == 1:
            col_idx = target_cols[0]
            for row_idx in range(num_rows):
                grid[row_idx][col_idx] = ciphertext[current_pos]
                current_pos += 1
        else:
            for row_idx in range(num_rows):
                for col_idx in target_cols:
                    grid[row_idx][col_idx] = ciphertext[current_pos]
                    current_pos += 1
                    
    plaintext = "".join(["".join(row) for row in grid])
    return plaintext.rstrip('X')

# --- Execution Block ---
if __name__ == "__main__":
    passphrase = "mammal"
    original_msg = "ALGORITHMSTHARUN"

    # Now both functions are defined and will work!
    encrypted = encrypt_hashed_myszkowski(original_msg, passphrase)
    decrypted = decrypt_hashed_myszkowski(encrypted, passphrase)

    print(f"Original:   {original_msg}")
    print(f"Ciphertext: {encrypted}")
    print(f"Decrypted:  {decrypted}")