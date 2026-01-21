def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    if len(set(s)) == 1:
        return 1

    left, right = 0, len(s) -1
    while left < right:
        left += 1
        if s[left] in s[left+1: right]:
            left += 1
        elif s[right] in s[left: right]:
            right -= 1
    return len(s[left: right])

print(lengthOfLongestSubstring("abcabcbb"))