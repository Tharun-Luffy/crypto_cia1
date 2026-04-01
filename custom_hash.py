def fnv1a_hash(text):
    """
    FNV-1a Hash (64-bit)
    An implementation of the Fowler-Noll-Vo hash function from scratch.
    It fulfills the requirement of implementing a custom hashing function 
    without using built-in libraries like hashlib.
    """
    # 64-bit FNV prime and offset basis
    FNV_prime = 1099511628211
    offset_basis = 14695981039346656037
    
    hash_value = offset_basis
    
    # Convert string to bytes
    text_bytes = str(text).encode('utf-8')
    
    for byte in text_bytes:
        # XOR the bottom with the current byte
        hash_value = hash_value ^ byte
        # Multiply by the FNV magic prime
        hash_value = (hash_value * FNV_prime) & 0xFFFFFFFFFFFFFFFF  # 64-bit integer constraint
        
    # Return a 16-character zero-padded hexadecimal string representing the 64-bit hash
    return hex(hash_value)[2:].zfill(16)

if __name__ == '__main__':
    # Simple test
    print(fnv1a_hash("Hello, World!"))
    print(fnv1a_hash("Hello, World."))
