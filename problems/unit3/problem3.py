# The deli staff is in desperate need of caffeine to keep them going through their shift and has decided to divide the coffee supply equally among themselves. Each batch of coffee is stored in containers of different sizes and must remain whole when distributed among n staff. Write a recursive function can_split_coffee() that accepts a list of integers coffee representing the volume of each batch of coffee and returns True if the coffee can be split evenly by volume among n staff and False otherwise.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def can_split_coffee(coffee, n):

    if sum(coffee) % n != 0:
        return False
    if len(coffee) == 0:
        return True
    
    return can_split_coffee(coffee[1:], n)

# Example Usage:

print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))
# Example Output:

# True
# False