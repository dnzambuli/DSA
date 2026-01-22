def lengthOfLongestSubstring(s: str) -> int:

    # Initialization:

    # last_idx: A dictionary that keeps track of the last index where each character occurred.
    # max_len: An integer to store the maximum length of the substring found.
    # start: A pointer to indicate the start of the current substring being examined.


    last_idx = {}
    max_len = 0

    start = 0

    for i in range(0, len(s)):
        # If the character has appeared before and is inside the current examined substring (i.e., if its last index is greater than or equal to start), then we move start to the index right after the last occurrence of that character.
        if s[i] in last_idx:
            start = max(start, last_idx[s[i]] + 1)
            print("current start point",start)
        # Calculate the length of the current substring and update if it's greater than the previously recorded maximum length.
        max_len = max(max_len, i - start + 1)
        print("current len of longest substring: ",max_len)
        # Update the last_idx with the current index of the character.
        last_idx[s[i]] = i 
        print(f"where letter last ocurred: {last_idx}\n\n")
    return max_len

         

print(lengthOfLongestSubstring("!@#$%^&*!"))