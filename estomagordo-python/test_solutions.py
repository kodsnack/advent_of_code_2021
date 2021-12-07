import day1a
import day1b
import day2a
import day2b
import day3a
import day3b
import day4a
import day4b
import day5a
import day5b
import day6a
import day6b
import day7a
import day7b


def test_1a():
    result = day1a.main()
    assert(1581 == result)


def test_1b():
    result = day1b.main()
    assert(1618 == result)


def test_2a():
    result = day2a.main()
    assert(2039256 == result)


def test_2b():
    result = day2b.main()
    assert(1856459736 == result)


def test_3a():
    result = day3a.main()
    assert(2595824 == result)


def test_3b():
    result = day3b.main()
    assert(2135254 == result)


def test_4a():
    result = day4a.main()
    assert(63552 == result)


def test_4b():
    result = day4b.main()
    assert(9020 == result)


def test_5a():
    result = day5a.main()
    assert(6687 == result)


def test_5b():
    result = day5b.main()
    assert(19851 == result)


def test_6a():
    result = day6a.main()
    assert(395627 == result)


def test_6b():
    result = day6b.main()
    assert(1767323539209 == result)


def test_7a():
    result = day7a.main()
    assert(359648 == result)


def test_7b():
    result = day7b.main()
    assert(100727924 == result)