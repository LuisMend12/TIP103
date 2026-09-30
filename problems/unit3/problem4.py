# A regular at the deli has requested a new order made by merging two different sandwiches on the menu together. Given the heads of two linked lists sandwich_a and sandwich_b where each node in the lists contains a sandwich layer, write a recursive function merge_orders() that merges the two sandwiches together in the pattern:

# a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...

# Return the head of the merged sandwich.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b):

    if sandwich_a == None:
        return sandwich_b
    
    if sandwich_b == None:
        return sandwich_a
    
    # HINT 1: Your base cases above are correct. Keep them.
    #
    # HINT 2: The two assignments below make a loop: a1 -> b1 -> a1 -> ...
    #   Trace it by hand with Bacon and Turkey. After both lines run, what
    #   points to Lettuce? What points to Cheese? If nothing does, the rest
    #   of both lists is lost.
    #
    # HINT 3: Before you overwrite sandwich_a.next, it holds something you
    #   still need (the rest of sandwich_a). How can you keep hold of it --
    #   or can you use it BEFORE it gets overwritten?
    #
    # HINT 4: A recursive call must work on a SMALLER problem. Because of the
    #   loop, sandwich_b.next is sandwich_a and sandwich_a.next is sandwich_b,
    #   so the call below gets the same two nodes again and never reaches a
    #   base case. The next call should not include a1 at all.
    #
    # HINT 5: Finish this sentence, using lists that do NOT contain a1:
    #   "a1.next should be the merge of ___ and ___."
    #   After a1, whose turn is it to go first? That sentence is your
    #   recursive call, and its result is what a1.next should be set to.
    #
    # HINT 6: If the recursive call hands you back the rest of the merged
    #   list, do you need to set sandwich_b.next yourself in this call?
    #   Trust the recursion to handle b1's pointer one level down.
    #
    # HINT 7: Don't return the recursive call's result directly -- that gives
    #   back a node from deep in the list. Which node is the head of the
    #   merged sandwich at THIS level? Return that one.
    #
    # HINT 8 (testing): merging rewires the nodes of sandwich_a in place. What
    #   does sandwich_a look like by the time the second example call runs?
    #   You may need a fresh list to see the expected second output.
    #
    # HINT 9 (complexity): how many calls are made in terms of the lengths of
    #   the two lists, and how deep does the call stack get?

    sandwich_a.next = sandwich_b
    sandwich_b.next = sandwich_a

    return merge_orders(sandwich_b.next, sandwich_a.next)


# Example Usage:

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))
# Example Output:

# Bacon -> Turkey -> Lettuce -> Cheese -> Tomato -> Mayo
# Bacon -> Bread -> Lettuce -> Tomato