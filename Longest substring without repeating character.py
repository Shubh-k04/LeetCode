def lengthOfLongestSubstring(s):
    maximum = [1]
    string = []
    max = 0
    for i in range(len(s)):
        if s[i] not in string:
            max+=1
            maximum.append(max)
        else:
            max = maximum[len(maximum)-1]-1