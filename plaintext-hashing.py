import math

def myszkowski_hash_logic(plaintext):
    # 1. Clean the text (Uppercase, no spaces)
    clean_text = "".join(filter(str.isalnum, plaintext)).upper()
    if not clean_text:
        return ""

    # 2. Use the message as its own keyword
    keyword = clean_text
    num_cols = len(keyword)
    
    # 3. Generate Ranks (Alphabetical order of the message letters)
    # This is the "Myszkowski" part: repeated letters get the same rank.
    sorted_chars = sorted(list(set(keyword)))
    rank_map = {char: i for i, char in enumerate(sorted_chars)}
    col_ranks = [rank_map[char] for char in keyword]
    
    # 4. Create the Grid (Message is written across)
    # In this self-hashing version, we look at the message as a single-row grid
    # or a square grid. Let's use a square-root width for a standard "hash" feel.
    width = int(math.sqrt(num_cols)) or 1
    rows = math.ceil(num_cols / width)
    padded_text = clean_text.ljust(rows * width, 'X')
    
    grid = [padded_text[i:i + width] for i in range(0, len(padded_text), width)]
    
    # We need to recalculate ranks for the new width
    key_for_width = clean_text[:width]
    sorted_sub = sorted(list(set(key_for_width)))
    sub_rank_map = {char: i for i, char in enumerate(sorted_sub)}
    sub_ranks = [sub_rank_map[char] for char in key_for_width]
    
    # 5. Transpose
    unique_ranks = sorted(list(set(sub_ranks)))
    result = ""
    for rank in unique_ranks:
        target_cols = [i for i, r in enumerate(sub_ranks) if r == rank]
        if len(target_cols) == 1:
            for row in grid:
                result += row[target_cols[0]]
        else:
            for row in grid:
                for col_idx in target_cols:
                    result += row[col_idx]
    
    return result

# Example
text = "ALGORITHMS"
hashed_output = myszkowski_hash_logic(text)

print(f"Plaintext: {text}")
print(f"Myszkowski-style Hash: {hashed_output}")