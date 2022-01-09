import pandas as pd
import pytest

from scripts.transform import _fips_cleaner

@pytest.mark.parametrize(
    "input, expected",
    [
        ('01001', '01001'), # 5-character string in, 5-character string out
        ('1001', '01001'),  # 4-character string in, 5-character string out
        (1001, '01001'),    # int in, 5-character string out
        (1001.0, '01001'),  # float in, 5-character string out
        ('11001', '11001'),   # Similar to before, but with two digit state code
        (11001, '11001'),   # Similar to before, but with two digit state code
        (11001.0, '11001'),   # Similar to before, but with two digit state code
    ]
)
def test_fips_cleaner(input, expected):
    input_series = pd.Series([input]) # setup
    cleaned_series = _fips_cleaner(input_series).iloc[0] # compute
    assert cleaned_series == expected
