def generate_substrings(s: str, size: int) -> list:
    """
    generate a list of substrings of a given size
    :param s:
    :param size:
    :return list of the strings substrings:
    """
    substrings = []
    str_len = len(s)
    if size <= 0:
        raise ValueError("size must be > 0")

    for i in range(str_len - size + 1):
        substrings.append(s[i:i + size])

    return substrings