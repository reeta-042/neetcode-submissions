class Solution:
    def scoreOfString(self, s: str) -> int:
        pairs = []
        list_of_pairs = []
        letters = list(s)
        n = len(letters) - 1
        for i in range(n):
            pairs.append((letters[i] , letters[i +1]))
            list_of_pairs.append(abs(ord(pairs[-1][0]) - ord(pairs[-1][1])))
        return sum(list_of_pairs)
