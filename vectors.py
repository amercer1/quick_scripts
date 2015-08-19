from functools import reduce

def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

def vector_sum_alternate(vectors):
    return reduce(vector_add, vectors)

def scalar_multiply(c ,v):
    return [c * x for x in v]

def main():
    print(vector_add([1, 2], [2, 1])) # [3,3]
    print(vector_subtract([2, 2], [1, 1])) # [1,1]
    print(vector_sum([[0,0,0], [1,1,1], [2,2,2]])) #[3, 3, 3,]
    print(vector_sum_alternate([[0,0,0], [1,1,1], [2,2,2]])) #[3, 3, 3,]
    print(scalar_multiply(10, [1, 2, 3, 4, 5])) # [10, 20, 30, 40, 50]

if __name__ == "__main__":
    main()
