from helpers import distance, distance_sq, ints, manhattan, neighs, neighs_bounded, columns, digits, chunks, chunks_with_overlap


def test_distance():
    a = [2, 3]
    b = [5, 7]

    d = distance(a, b)
    expected = 5

    assert(expected == d)


def test_distance_flipped():
    b = [2, 3]
    a = [5, 7]

    d = distance(a, b)
    expected = 5

    assert(expected == d)


def test_distance_negatives():
    a = [-2, -3]
    b = [-5, -7]

    d = distance(a, b)
    expected = 5

    assert(expected == d)


def test_distance_3d():
    b = [2, -3, 9]
    a = [1, -5, 7]

    d = distance(a, b)
    expected = 3

    assert(expected == d)


def test_distance_sq_2d():
    a = [2, 3]
    b = [5, 7]

    d = distance_sq(a, b)
    expected = 25

    assert(expected == d)


def test_distance_sq_2d_flipped():
    b = [2, 3]
    a = [5, 7]

    d = distance_sq(a, b)
    expected = 25

    assert(expected == d)


def test_distance_sq_2d_negatives():
    a = [-2, -3]
    b = [-5, -7]

    d = distance_sq(a, b)
    expected = 25

    assert(expected == d)


def test_distance_sq_3d():
    b = [2, -3, 9]
    a = [1, -5, 7]

    d = distance_sq(a, b)
    expected = 9

    assert(expected == d)


def test_ints():
    s = 'What they-43 were 8 saying was <albeit 7> (9) mi85ninte and -2'

    nums = ints(s)
    expected = [-43, 8, 7, 9, 85, -2]

    assert(expected == nums)


def test_manhattan():
    a = [5, -4]
    b = [2, 3]

    d = manhattan(a, b)
    expected = 10

    assert(expected == d)


def test_manhattan_flipped():
    b = [5, -4]
    a = [2, 3]

    d = manhattan(a, b)
    expected = 10

    assert(expected == d)


def test_manhattan_same():
    a = [5, -4]
    b = [5, -4]

    d = manhattan(a, b)
    expected = 0

    assert(expected == d)


def test_manhattan_3d():
    a = [5, -4, 7]
    b = [2, 3, 11]

    d = manhattan(a, b)
    expected = 14

    assert(expected == d)


def test_neighs():
    y = 4
    x = 2

    neighbours = neighs(y, x)
    
    assert(4 == len(neighbours))
    assert([3, 2] in neighbours)
    assert([5, 2] in neighbours)
    assert([4, 1] in neighbours)
    assert([4, 3] in neighbours)


def test_neighs_negative():
    y = -4
    x = -2

    neighbours = neighs(y, x)
    
    assert(4 == len(neighbours))
    assert([-3, -2] in neighbours)
    assert([-5, -2] in neighbours)
    assert([-4, -1] in neighbours)
    assert([-4, -3] in neighbours)


def test_neighs_bounded_in_bounds():
    y = 5
    x = 6
    rmin = 0
    rmax = 10
    cmin = 0
    cmax = 10

    neighbours = neighs_bounded(y, x, rmin, rmax, cmin, cmax)
    
    assert(4 == len(neighbours))
    assert([4, 6] in neighbours)
    assert([6, 6] in neighbours)
    assert([5, 5] in neighbours)
    assert([5, 7] in neighbours)


def test_neighs_bounded_edge():
    y = 5
    x = 6
    rmin = 5
    rmax = 10
    cmin = 0
    cmax = 10

    neighbours = neighs_bounded(y, x, rmin, rmax, cmin, cmax)
    
    assert(3 == len(neighbours))    
    assert([6, 6] in neighbours)
    assert([5, 5] in neighbours)
    assert([5, 7] in neighbours)


def test_neighs_bounded_corner():
    y = 5
    x = 6
    rmin = 5
    rmax = 10
    cmin = 0
    cmax = 6

    neighbours = neighs_bounded(y, x, rmin, rmax, cmin, cmax)
    
    assert(2 == len(neighbours))    
    assert([6, 6] in neighbours)
    assert([5, 5] in neighbours)  


def test_columns():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    cols = columns(matrix)

    assert([1, 4, 7] == cols[0])
    assert([2, 5, 8] == cols[1])
    assert([3, 6, 9] == cols[2])

    non_square_matrix = [[1, 2], [3, 4], [5, 6]]

    non_square_cols = columns(non_square_matrix)

    assert([1, 3, 5] == non_square_cols[0])
    assert([2, 4, 6] == non_square_cols[1])


def test_digits():
    s = '8936982'

    result = digits(s)

    assert([8,9,3,6,9,8,2] == result)


def test_chunks():
    l = [1, 2, 7, 10, 12, 2]

    twochunks = list(chunks(l, 2))
    threechunks = list(chunks(l, 3))

    assert([[1, 2], [7, 10], [12, 2]] == twochunks)
    assert([[1, 2, 7], [10, 12, 2]] == threechunks)


def test_chunks_with_overlap():
    l = [1, 2, 7, 10, 12, 2]

    twochunks = list(chunks_with_overlap(l, 2))
    threechunks = list(chunks_with_overlap(l, 3))

    assert([[1, 2], [2, 7], [7, 10], [10, 12], [12, 2]] == twochunks)
    assert([[1, 2, 7], [2, 7, 10], [7, 10, 12], [10, 12, 2]] == threechunks)