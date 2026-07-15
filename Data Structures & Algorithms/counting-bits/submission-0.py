class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        #total = 0
        range_of_number = list(range(n + 1))

        for i in range_of_number:
            total = 0

            #if i == 0:
                #output.append(0)

            while i > 0:
                if i & 1 != 0:
                    total += 1
                i = i >> 1
            output.append(total)
        return output


        