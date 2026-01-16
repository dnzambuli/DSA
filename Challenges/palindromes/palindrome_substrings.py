a = "aabbaa"

a_split = []
a_len = len(a)


def is_palindrome(s):
    length = len(s)

    for i in range(length // 2):

        if s[i] != s[length - i - 1]:
            # Return 0 (not a palindrome)
            return 0

    # If all symmetric characters are equal
    # then it is palindrome
    return 1


def sliding_chunks(s: str, size: int) -> list[str]:
    if size <= 0:
        raise ValueError("size must be positive")

    palindromes = []
    for i in range(len(s) - size + 1):
        if is_palindrome(s[i : i + size]):
            palindromes.append(s[i : i + size])
        else:
            continue

    return palindromes

    # [s[i:i + size] if is_palindrome(s[i:i + size]) else continue for i in range(len(s) - size + 1)]

for i in range(2, a_len + 1):
    a_split.append(sliding_chunks(a, i))

final = []
for i in a_split:
    if len(i) != 0:
        final.append(i)

print(final)
