import math

def get_keyword_ranks(keyword):
    """
    Generate ranks for each letter in the keyword based on alphabetical order.
    Identical letters get the same rank.
    """
    keyword = keyword.upper()
    sorted_unique_chars = sorted(list(set(keyword)))
    rank_map = {char: i for i, char in enumerate(sorted_unique_chars)}
    return [rank_map[char] for char in keyword]

def encrypt(plaintext, keyword):
    """
    Encrypts the plaintext using the Myszkowski transposition cipher.
    """
    plaintext = "".join(filter(str.isalnum, plaintext)).upper()
    keyword = "".join(filter(str.isalpha, keyword)).upper()
    
    if not plaintext or not keyword:
        return ""

    num_cols = len(keyword)
    col_ranks = get_keyword_ranks(keyword)
    
    # Pad plaintext with 'X' to complete the grid
    num_rows = math.ceil(len(plaintext) / num_cols)
    padded_len = num_rows * num_cols
    plaintext = plaintext.ljust(padded_len, 'X')
    
    grid = [plaintext[i:i + num_cols] for i in range(0, len(plaintext), num_cols)]
    
    unique_ranks = sorted(list(set(col_ranks)))
    ciphertext = ""
    
    for rank in unique_ranks:
        target_cols = [i for i, r in enumerate(col_ranks) if r == rank]
        
        if len(target_cols) == 1:
            # Standard columnar read
            col_idx = target_cols[0]
            for row in grid:
                ciphertext += row[col_idx]
        else:
            # Myszkowski read: read across the row for the target columns
            for row in grid:
                for col_idx in target_cols:
                    ciphertext += row[col_idx]
                    
    return ciphertext

def decrypt(ciphertext, keyword):
    """
    Decrypts the ciphertext using the Myszkowski transposition cipher.
    Returns the padded plaintext.
    """
    ciphertext = "".join(filter(str.isalnum, ciphertext)).upper()
    keyword = "".join(filter(str.isalpha, keyword)).upper()
    
    if not ciphertext or not keyword:
        return ""

    num_cols = len(keyword)
    col_ranks = get_keyword_ranks(keyword)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    
    unique_ranks = sorted(list(set(col_ranks)))
    
    # Create an empty grid
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    # Fill the grid
    idx = 0
    for rank in unique_ranks:
        target_cols = [i for i, r in enumerate(col_ranks) if r == rank]
        
        if len(target_cols) == 1:
            col_idx = target_cols[0]
            for r in range(num_rows):
                if idx < len(ciphertext):
                    grid[r][col_idx] = ciphertext[idx]
                    idx += 1
        else:
            for r in range(num_rows):
                for col_idx in target_cols:
                    if idx < len(ciphertext):
                        grid[r][col_idx] = ciphertext[idx]
                        idx += 1
                        
    # Reconstruct plaintext
    plaintext = ""
    for row in grid:
        plaintext += "".join(row)
        
    return plaintext

if __name__ == '__main__':
    # Quick Test
    kw = "TOMATO"
    pt = "WEAREDISCOVEREDFLEEATONCE"
    ct = encrypt(pt, kw)
    dec = decrypt(ct, kw)
    print("Keyword:", kw)
    print("Plain:", pt)
    print("Cipher:", ct)
    print("Decrypted:", dec)
