class word:
    def __init__(self, s):
        self.s = str(s)

    def reverse(self):
        return self.s[::-1]

Code = word('code')
print(Code.reverse())