class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generateCombos(n, n, "", result)
        return result  

    def generateCombos(self, n_left, n_right, curr_combo, result):
        if n_left == 0 and n_right == 0:
            result.append(curr_combo)
            return
        elif n_left == 0:
            curr_combo += ")"
            n_right -= 1
            self.generateCombos(n_left, n_right, curr_combo, result)
        elif n_left == n_right:
            curr_combo += "("
            n_left -= 1
            self.generateCombos(n_left, n_right, curr_combo, result)
        else: #n_left > n_right:
            self.generateCombos(n_left, n_right - 1, curr_combo + ")", result)
            self.generateCombos(n_left - 1, n_right, curr_combo + "(", result)