def is_reflexive(relation_set, set_elements):
    for element in set_elements:
        if (element, element) not in relation_set:
            return False
    return True

def is_symmetric(relation_set):
    for pair in relation_set:
        if (pair[1], pair[0]) not in relation_set:
            return False
    return True

def is_transitive(relation_set):
    for a, b in relation_set:
        for c, d in relation_set:
            if b == c and (a, d) not in relation_set:
                return False
    return True

def check_equivalence(relation_set, set_elements):
    reflexive = is_reflexive(relation_set, set_elements)
    symmetric = is_symmetric(relation_set)
    transitive = is_transitive(relation_set)

    if reflexive and symmetric and transitive:
        print("R is an equivalence relation")
    else:
        print("R is" + (" not" if not reflexive else "") + " reflexive")
        print("R is" + (" not" if not symmetric else "") + " symmetric")
        print("R is" + (" not" if not transitive else "") + " transitive")
        print("R does" + ("" if reflexive and symmetric and transitive else " not") + " have equivalence relation")

input_string = { (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }
elements = {0, 1, 2, 3}

check_equivalence(input_string, elements)
