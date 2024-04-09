#  non-empty digit string is diverse if the number of occurrences of each character in it doesn't exceed the number of distinct characters in it.

# For example:

# string "7" is diverse because 7 appears in it 1 time and the number of distinct characters in it is 1;
# string "77" is not diverse because 7 appears in it 2 times and the number of distinct characters in it is 1;
# string "1010" is diverse because both 0 and 1 appear in it 2 times and the number of distinct characters in it is 2;
# string "6668" is not diverse because 6 appears in it 3 times and the number of distinct characters in it is 2.
# You are given a string s of length n, consisting of only digits 0 to 9. Find how many of its n(n+1)2 substrings are diverse.

# A string a is a substring of a string b if a can be obtained from b by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

# Note that if the same diverse string appears in s multiple times, each occurrence should be counted independently. For example, there are two diverse substrings in "77" both equal to "7", so the answer for the string "77" is 2.

# Input
# The first line contains a single integer t (1≤t≤100) — the number of test cases.

# The first line of each test case contains a single integer n (1≤n≤100) — the length of the string s.

# The second line of each test case contains a string s of length n, consisting of only digits 0 to 9.

def diverseSubstrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if len(set(s[i:j+1])) == len(s[i:j+1]):
                count += 1
    return count

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        print(diverseSubstrings(s))