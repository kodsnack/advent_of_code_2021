from day18a import explode, reduction, add, calc, magnitude
from day22b import intersection
from day23b import heuristic, scorepos


def test_explode():
    s1 = '[[[[[9,8],1],2],3],4]'
    s2 = '[7,[6,[5,[4,[3,2]]]]]'
    s3 = '[[6,[5,[4,[3,2]]]],1]'
    s4 = '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'
    s5 = '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
    s6 = '[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]'

    result1 = explode(s1)[1]
    result2 = explode(s2)[1]
    result3 = explode(s3)[1]
    result4 = explode(s4)[1]
    result5 = explode(s5)[1]
    result6 = explode(s6)[1]

    assert('[[[[0,9],2],3],4]' == result1)
    assert('[7,[6,[5,[7,0]]]]' == result2)
    assert('[[6,[5,[7,0]]],3]' == result3)
    assert('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]' == result4)
    assert('[[3,[2,[8,0]]],[9,[5,[7,0]]]]' == result5)
    assert('[[[[4,0],[5,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]' == result6)


def test_add():
    a = '[[[[4,3],4],4],[7,[[8,4],9]]]'
    b = '[1,1]'
    c = '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]'
    d = '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]'

    result1 = add(a, b)
    result2 = add(c, d)

    assert('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]' == result1)
    assert('[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]' == result2)


def test_reduction():
    s = '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'

    result = reduction(s)

    assert('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]' == result)


def test_calc():
    nums1 = ['[1,1]', '[2,2]', '[3,3]', '[4,4]']
    nums2 = ['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]']
    nums3 = ['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]', '[6,6]']
    nums4 = ['[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]', '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]']
    nums5 = ['[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]', '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]', '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]']
    nums6 = ['[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]', '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]', '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]', '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]']
    nums7 = ['[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]', '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]', '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]', '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]', '[7,[5,[[3,8],[1,4]]]]']
    nums8 = ['[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]', '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]', '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]', '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]', '[7,[5,[[3,8],[1,4]]]]', '[[2,[2,2]],[8,[8,1]]]']
    nums8short = ['[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]', '[[2,[2,2]],[8,[8,1]]]']

    result1 = calc(nums1)
    result2 = calc(nums2)
    result3 = calc(nums3)
    result4 = calc(nums4)
    result5 = calc(nums5)
    result6 = calc(nums6)
    result7 = calc(nums7)
    result8 = calc(nums8)
    result9 = calc(nums8short)

    assert('[[[[1,1],[2,2]],[3,3]],[4,4]]' == result1)
    assert('[[[[3,0],[5,3]],[4,4]],[5,5]]' == result2)
    assert('[[[[5,0],[7,4]],[5,5]],[6,6]]' == result3)
    assert('[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]' == result4)
    assert('[[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]' == result5)
    assert('[[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]' == result6)
    assert('[[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]' == result7)
    assert('[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]' == result8)
    assert('[[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]' == result9)


def test_magnitude():
    s1 = '[[1,2],[[3,4],5]]'
    s2 = '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'
    s3 = '[[[[1,1],[2,2]],[3,3]],[4,4]]'
    s4 = '[[[[3,0],[5,3]],[4,4]],[5,5]]'
    s5 = '[[[[5,0],[7,4]],[5,5]],[6,6]]'
    s6 = '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'

    result1 = magnitude(s1)
    result2 = magnitude(s2)
    result3 = magnitude(s3)
    result4 = magnitude(s4)
    result5 = magnitude(s5)
    result6 = magnitude(s6)

    assert(143 == result1)
    assert(1384 == result2)
    assert(445 == result3)
    assert(791 == result4)
    assert(1137 == result5)
    assert(3488 == result6)


def test_intersection():
    empty = (0, 0, 0, 0, 0, 0)
    a = (10, 12, 10, 12, 10, 12)
    b = (11, 13, 11, 13, 11, 13)
    c = (9, 11, 9, 11, 9, 11)
    d = (10, 10, 10, 10, 10, 10)

    ab = intersection(a, b)
    ba = intersection(b, a)
    cd = intersection(c, d)
    bd = intersection(b, d)

    assert(ab == ba)
    assert((11, 12, 11, 12, 11, 12) == ab)
    assert(d == cd)
    assert(empty == bd)


def test_heuristic():
    goala = [(2, 3), (3, 3), (4, 3), (5, 3)]
    goalb = [(2, 5), (3, 5), (4, 5), (5, 5)]
    goalc = [(2, 7), (3, 7), (4, 7), (5, 7)]
    goald = [(2, 9), (3, 9), (4, 9), (5, 9)]

    startexa = [(3, 9), (4, 7), (5, 3), (5, 9)]
    startexb = [(2, 3), (2, 7), (3, 7), (4, 5)]
    startexc = [(2, 5), (3, 5), (4, 9), (5, 7)]
    startexd = [(2, 9), (3, 3), (4, 3), (5, 5)]

    assert(len([x for x in startexa if x in startexb]) == 0)
    assert(len([x for x in startexa if x in startexc]) == 0)
    assert(len([x for x in startexa if x in startexd]) == 0)
    assert(len([x for x in startexb if x in startexc]) == 0)
    assert(len([x for x in startexb if x in startexd]) == 0)
    assert(len([x for x in startexc if x in startexd]) == 0)

    assert(0 == heuristic(goala, goalb, goalc, goald))
    assert(36001 == heuristic(startexa, startexb, startexc, startexd))


# def test_scorepos():
