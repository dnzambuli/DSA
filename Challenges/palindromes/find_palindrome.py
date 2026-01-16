def palindrome_with_reverse(s: str) -> bool:
    """
    find a palindrome using string reversal
    :param s:
    :return:
    """
    if s != s[::-1]:
        return False
    return True

def palindrome_with_looping(s: str) -> bool:
    """
    find a palindrome using loops
    :param s:
    :return:
    """
    length = len(s)
    # using radar ada  adda as a check
    # I can only move n/2-truncated times: 2(rada), 1(ada), 2(adda)
    for i in range(length // 2):
        # compare index 0 and -1, 1 and -2 ...
        # if one fails it is not a palindrome
        if s[0] != s[length - i - 1]:
            return False
        # exit the loop first before true to ensure the loop iterated enough times
    return True
