from day18a import explode, calc, add


def test_explode():
    s1 = '[[[[[9,8],1],2],3],4]'
    s2 = '[7,[6,[5,[4,[3,2]]]]]'
    s3 = '[[6,[5,[4,[3,2]]]],1]'
    s4 = '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'
    s5 = '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'

    result1 = explode(s1)[1]
    result2 = explode(s2)[1]
    result3 = explode(s3)[1]
    result4 = explode(s4)[1]
    result5 = explode(s5)[1]

    assert('[[[[0,9],2],3],4]' == result1)
    assert('[7,[6,[5,[7,0]]]]' == result2)
    assert('[[6,[5,[7,0]]],3]' == result3)
    assert('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]' == result4)
    assert('[[3,[2,[8,0]]],[9,[5,[7,0]]]]' == result5)


def test_add():
    a = '[[[[4,3],4],4],[7,[[8,4],9]]]'
    b = '[1,1]'

    result = add(a, b)

    assert([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]] == result)


def test_calc():
    s = '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'

    result = calc(s)

    assert('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]' == result)