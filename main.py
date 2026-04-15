# 26
class ReverseString:
    def __init__(self, s):
        self.s = s
    def solve(self):
        return self.s[::-1]

print(ReverseString(input()).solve())

# 27
class Palindrome:
    def __init__(self, s):
        self.s = s
    def solve(self):
        return self.s == self.s[::-1]

print(Palindrome(input()).solve())

# 28
class CountA:
    def __init__(self, s):
        self.s = s
    def solve(self):
        return self.s.count('a')

print(CountA(input()).solve())

# 29
class ReplaceAB:
    def __init__(self, s):
        self.s = s
    def solve(self):
        return self.s.replace('a', 'b')

print(ReplaceAB(input()).solve())

# 30
class ReverseWords:
    def __init__(self, s):
        self.s = s
    def solve(self):
        return " ".join(self.s.split()[::-1])

print(ReverseWords(input()).solve())
