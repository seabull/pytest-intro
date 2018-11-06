import pytest
import skilift


@pytest.fixture
def line_N(request):
    line_size = request.node.get_closest_marker('line_size').args[0]
    return skilift.Line(line_size)


@pytest.fixture
def test_mp(monkeypatch):
    def take_half(self, amount):
        half_amt = int(amount/2)
        if half_amt > self.num_people:
            half_amt = self.num_people
        self.num_people -= half_amt
        return half_amt
    monkeypatch.setattr(skilift.Line, 'take', take_half)
    line = skilift.Line(10)
    assert line.take(5) == 2
    assert 8 == line.num_people


