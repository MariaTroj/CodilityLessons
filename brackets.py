"""
A string S consisting of N characters is considered to be properly nested if any of the following
conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function: def solution(S) that, given a string S consisting of N characters, returns 1 if S
is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function
should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
closing_brackets = [']', '}', ')']
brackets_dict = {']': '[', '}': '{', ')': '('}


def solution(S):
    n = len(S)

    if n == 0:
        return 1

    if n % 2 or S[0] in closing_brackets or S[-1] not in closing_brackets:
        return 0

    temp = []

    for b in S:
        if b in closing_brackets:
            try:
                if temp[-1] == brackets_dict[b]:
                    temp.pop()
                else:
                    return 0
            except:
                return 0
        else:
            temp.append(b)

    return int(len(temp) == 0)