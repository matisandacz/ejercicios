def estaContenido(Node* t1, Node* t2):

	if not t2: return True
	if not t1: return False

	if(mismoArbol(t1, t2)):
		return True

	return estaContenido(t1->left, t2) or estaContenido(t1->right, t2)

#				3
#		4				4
#1           2                          #4 1 2


def mismoArbol(Node* t1, Node* t2):
	if not t1 and not t2:
		return True
	if t1 and t2 and t1->val == t2->val and mismoArbol(t1->left, t2->left) and mismoArbol(t1->right, t2->right):
		return True
	return False