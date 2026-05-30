from src.math_operations import addition,subtraction

def test_add():
    assert addition(2,3)==5
    assert addition(5,2)==7
    assert addition(-1,1)==0


def test_sub():
    assert subtraction(7,5)==2
    assert subtraction(5,0)==5
    assert subtraction(3,3)==0
    assert subtraction(1,7)==-6





