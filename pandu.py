from numpy.random import randn
from pandas import Series, date_range

ts = Series(randn(1000, 0), index=date_range('1/1/2000', periods=1000))
ts = ts.cumsum()

