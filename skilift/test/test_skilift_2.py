import skilift


import pytest

@pytest.mark.bench_size(6)
def test_bench6(BenchN, line5):
    lift = skilift.Lift(10, BenchN)
    res = lift.one_bench(line5)
    assert res == {'loaded': 5, 'num_benches': 1, 'unloaded': 0}


@pytest.mark.line_size(6)
def test_line6(line_n):
    res = line_n.take(7)
    assert res == 6
    assert line_n.num_people == 0


def test_line_take(line5):
    res = line5.take(7)
    assert res == 5
    assert line5.num_people == 0

def test_lift_one_bench(line5, quad_lift10):
    res = quad_lift10.one_bench(line5)
    assert res == {'loaded': 4, 'num_benches': 1, 'unloaded': 0}

@pytest.mark.parametrize('count, err',
                         [([], TypeError),
                          (None, TypeError),
                          ('10', TypeError)])
def test_line_bad(count, err):
    line = skilift.Line(count)
    with pytest.raises(err):
        res = line.take(1)


@pytest.mark.parametrize('line, take_size, remaining',
                         [(0,5,0), (5,2,3), (10, 0, 10)])
def test_line_sizes(line, take_size, remaining):
    line = skilift.Line(line)
    res = line.take(take_size)
    assert line.num_people == remaining

def test_half_take(monkeypatch):
    def half_take(self, amount):
        amount = int(amount/2)
        if amount > self.num_people:
            amount = self.num_people
        self.num_people -= amount
        return amount
    monkeypatch.setattr(skilift.Line, 'take', half_take)
    line = skilift.Line(10)
    res = line.take(5)
    assert res == 2
    assert line.num_people == 8
