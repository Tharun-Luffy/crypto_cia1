from myszkowski import encrypt, decrypt
from custom_hash import fnv1a_hash

def run_example(example_num, plaintext, keyword):
    print(f"--- Example {example_num} ---")
    print(f"Original Plaintext: {plaintext}")
    print(f"Keyword: {keyword}")
    
    # Strip spaces and uppercase for clean comparison later
    clean_pt = "".join(filter(str.isalnum, plaintext)).upper()
    
    # Generate Hash of Original Plaintext
    original_hash = fnv1a_hash(clean_pt)
    print(f"1. Hash of Original (FNV-1a): {original_hash}")
    
    # 1. Encrypt
    ciphertext = encrypt(plaintext, keyword)
    print(f"2. Ciphertext: {ciphertext}")
    
    # Generate Hash of Ciphertext (Simulating transit hash)
    ct_hash = fnv1a_hash(ciphertext)
    print(f"   Hash of Ciphertext: {ct_hash}")
    
    # 2. Decrypt
    decrypted = decrypt(ciphertext, keyword)
    print(f"3. Decrypted Text (Padded): {decrypted}")
    
    # 3. Hash after decryption to verify integrity
    # We hash the portion of the decrypted text that matches the original length
    # to ignore the 'X' padding for the hash check, OR we can just hash the whole 
    # decrypted text and say the padding is part of the final message. 
    # Let's remove padding for the hash check if we know original length, 
    # or just show hash of the padded output. 
    # Actually, we can just hash the decrypted padded text to show it's intact.
    decrypted_hash = fnv1a_hash(decrypted)
    print(f"4. Hash of Decrypted (Padded): {decrypted_hash}")
    
    hash_match = original_hash == fnv1a_hash(decrypted[:len(clean_pt)])
    print(f"Integrity Check over original length matches? {hash_match}")
    print()

if __name__ == '__main__':
    print("MYSZKOWSKI CIPHER & CUSTOM FNV-1a HASH DEMO\n")
    
    # Example 1: Standard Myszkowski features (repeated letters in keyword)
    run_example(1, "WE ARE DISCOVERED FLEE AT ONCE", "TOMATO")
    
    # Example 2: Longer phrase
    run_example(2, "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", "CRYPTOGRAPHY")
