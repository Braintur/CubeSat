def bar_to_meters(bar):
    pg = 12.511674
    m = bar/pg
    m = m*1000
    return m

print(bar_to_meters(1.009))