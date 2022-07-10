import pytest


def calc_taxation(tax_pct, price):
    return round((1.0 + tax_pct) * price, 2)


@pytest.mark.parametrize('price,tax_pct,result',
                         [(100, 0.19, 119),
                          (55, 0.16, 63.80),
                          (999.99, 0.07, 1069.99)])
def test_calc_taxation(tax_pct, price, result):
    assert calc_taxation(tax_pct, price) == result
