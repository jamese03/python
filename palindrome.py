def longestPalindrome(string: str):
    longest = ""
    for i in range(len(string)):
        pal1 = findPalindrome(list(string), i, i + 1)
        pal2 = findPalindrome(list(string), i, i)
        tempLongest = ""
        if len(pal1) > len(pal2):
            tempLongest = pal1
        else:
            tempLongest = pal2
        if len(tempLongest) > len(longest):
            longest = tempLongest

    return print("".join(longest))



def findPalindrome(l: list, left: int, right: int):
    while left >= 0 and right < len(l) and l[left] == l[right]:
        left = left - 1
        right = right + 1

    return l[left+1:right]



longestPalindrome("84949495849585855555444555499999999999444444245")
