class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score = []

        for i in operations:
            if i not in ("C","D","+"):
                score.append(int(i))
            elif i == "+":
                previous_two = score[-2:]
                sum_of_previous = sum(previous_two)
                score.append(sum_of_previous)
            elif i == "D":
                double_score = score[-1]
                score.append(2 * double_score)
            else:
                remove_score = score[-1]
                score.remove(remove_score)

        return sum(score)



        