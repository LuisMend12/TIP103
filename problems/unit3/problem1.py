# You're working at a deli, and need to count the layers of a sandwich to make sure you made the order correctly. Each layer is represented by a nested list. Given a list of lists sandwich where each list [] represents a sandwich layer, write a recursive function count_layers() that returns the total number of sandwich layers.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

# def count_layers(sandwich):
#     pass
# Example Usage:

# Example Output:

# 4
# 5


def count_layers(sandwich):
    
    if not sandwich:
        return 0

    if len(sandwich) == 1:
        return 1
    

    return 1 + count_layers(sandwich[1])


        

        



sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))