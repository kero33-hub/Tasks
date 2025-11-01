# Minimax Algorithm Example

def minimax(depth, node_index, is_max, scores, max_depth):
  
    if depth == max_depth:
        return scores[node_index]


    if is_max:
        left = minimax(depth + 1, node_index * 2, False, scores, max_depth)
        right = minimax(depth + 1, node_index * 2 + 1, False, scores, max_depth)
        return max(left, right)
    else:
        left = minimax(depth + 1, node_index * 2, True, scores, max_depth)
        right = minimax(depth + 1, node_index * 2 + 1, True, scores, max_depth)
        return min(left, right)



scores = [3, 5, 6, 9, 1, 2, 0, -1]
max_depth = 3  

optimal_value = minimax(0, 0, True, scores, max_depth)

print("Leaf nodes:", scores)
print(" Optimal value for MAX player is:", optimal_value)
