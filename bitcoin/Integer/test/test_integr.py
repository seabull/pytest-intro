import pytest
from integr import parse

@pytest.mark.ylj
@pytest.mark.basic
@pytest.mark.num
def test_basic():
    #import pdb;pdb.set_trace()
    result = parse("1,3,5,9")
    assert [1,3,5,9] == result, "expect [1,3,5,9]"


@pytest.mark.exception_check
def test_exc():
    with pytest.raises(ValueError):
        parse('1,a,3,5,6')


@pytest.mark.xfail(raises=ValueError)
def test_exc2():
    parse('1,a,3,5,6')

@pytest.mark.wrong
def test_bad1():
    with pytest.raises(ValueError):
        parse('1-3,12-15')


@pytest.mark.wrong
@pytest.mark.xfail(raises=ValueError)
def test_bad2():
    parse('1-3,12-15')


if __name__ == '__main__':
    pytest.main()
