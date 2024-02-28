def isABB(Node* node):
	if not node:
		return True


	isLeft = isABB(node->left)
	isRight = isABB(node->right) 
	isMaxLeft = node->val >= find_max(node->left)
	isMinRight = node->val <= find_min(node->right)
	return isLeft and isRight and isMaxLeft and isMinRight




def find_max(node* node):
	if esHoja(node):
		return node->val
	else:
		return max(node->val, max(find_max(node->left), find_max(node->right)))




