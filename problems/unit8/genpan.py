# A code formatter needs to enumerate every way to nest a fixed number of bracket pairs so it can showcase valid layouts. Given an integer n representing n pairs of parentheses, return all combinations of well-formed (balanced) parentheses.

def generate_parentheses(n):

    res = []
    def backtrack(count_right, count_left, curr):
        if count_right == n and count_left == n:
            res.append(curr)
            return
        
        if count_left < n:
            backtrack(count_right, count_left+1, curr+'(')
        if count_left > count_right:
            backtrack(count_right+1, count_left, curr+')')
        

    backtrack(0, 0, '')
    return res
# Example Usage

print(generate_parentheses(3))
# Example Output:

# ['((()))', '(()())', '(())()', '()(())', '()()()']