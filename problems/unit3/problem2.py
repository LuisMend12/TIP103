# Problem 2: Reversing Deli Orders
# The deli counter is busy, and orders have piled up. To serve the last customer first, you need to reverse the order of the deli orders. Given a string orders where each individual order is separated by a single space, write a recursive function reverse_orders() that returns a new string with the orders reversed.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def reverse_orders(orders):

    orders = orders.split()
    
    if len(orders) == 1:
        return orders[0]


    return reverse_orders(" ".join(orders[1:])) + " " + orders[0] 

    # return None
# Example Usage:

print(reverse_orders("Bagel Sandwich Coffee"))
# Example Output:

# Coffee Sandwich Bagel