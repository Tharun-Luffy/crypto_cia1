import hashlib
import math

def get_hash_ranks(passphrase, num_cols):
    """Uses SHA-256 to generate deterministic column ranks."""
    hash_digest = hashlib.sha256(passphrase.encode()).digest()
    # If the message is wider than 32 cols, we wrap the hash
    ranks = [hash_digest[i % len(hash_digest)] for i in range(num_cols)]
    return ranks

def encrypt_hashed_myszkowski(text, passphrase):
    text = text.replace(" ", "").upper()
    num_cols = 8  # We can define a fixed width or derive it
    
    # 1. Generate ranks from hashing the passphrase
    col_ranks = get_hash_ranks(passphrase, num_cols)
    
    # 2. Grid Setup
    num_rows = math.ceil(len(text) / num_cols)
    text = text.ljust(num_rows * num_cols, 'X') # Padding
    grid = [text[i:i + num_cols] for i in range(0, len(text), num_cols)]
    
    # 3. Transposition logic
    unique_ranks = sorted(list(set(col_ranks)))
    ciphertext = ""
    
    for rank in unique_ranks:
        target_cols = [i for i, r in enumerate(col_ranks) if r == rank]
        
        if len(target_cols) == 1:
            # Unique rank: Read down column
            col_idx = target_cols[0]
            for row in grid:
                ciphertext += row[col_idx]
        else:
            # Shared rank: Read across rows (Myszkowski Rule)
            for row in grid:
                for col_idx in target_cols:
                    ciphertext += row[col_idx]
                    
    return ciphertext

# Example
passphrase = "mammal"
message = "ALGORITHMS"

result = encrypt_hashed_myszkowski(message, passphrase)
print(f"Hashed Transposition: {result}")
