import pytest

import skilift


def test_line_take():
    line = skilift.Line(5)
    assert line.num_people == 5
    assert 5 == line.take(7)
    assert 0 == line.num_people


def test_lift_one_bench():
    line = skilift.Line(5)
    quad = skilift.Lift(10, skilift.Quad)
    result = quad.one_bench(line)
    assert result == {'loaded': 4, 'num_benches': 1, 'unloaded': 0}


@pytest.mark.parametrize('l, e', [
    ([], TypeError),
    (None, TypeError),
    ('10', TypeError),
])
def test_line_bad(l, e):
    line = skilift.Line(l)
    with pytest.raises(e):
        line.take(1)


@pytest.mark.parametrize('l, tk, exp', [
    (0, 5, 0),
    (5, 2, 3),
    (10,0, 10),
])
def test_line_sizes(l, tk, exp):
    line = skilift.Line(l)
    line.take(tk)
    assert exp == line.num_people



# @pytest.mark.parametrize('x,y,z', [
#     (1, 2, 3), #first
#     (-1, -2, -3),  # neg
#     (0, 0, ),  # zero
# ])
# def test_add(x, y, z):
#     assert adder(x, y) == z


# @pytest.fixture
# def large_num():
#     return 1e20
#
#
# def test_large(large_num):
#     assert adder(large_num, 1) == large_num

@pytest.fixture(params = [-1, 0 , 100])
def 