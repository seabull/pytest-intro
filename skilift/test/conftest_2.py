import skilift

import pytest

@pytest.fixture
def line5():
    line = skilift.Line(5)
    return line

@pytest.fixture
def line_n(request):
    size = request.node.get_closest_marker('line_size').args[0]
    return skilift.Line(size)

@pytest.fixture
def quad_lift10():
    quad = skilift.Lift(10, skilift.Quad)
    return quad

@pytest.fixture
def BenchN(request):
    size_ = request.node.get_closest_marker('bench_size').args[0]
    class BSize(skilift._Bench):
        size = size_
    return BSize
