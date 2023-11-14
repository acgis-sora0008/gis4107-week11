import geometry as ge

def test_point():
    expected = 45.2059, 75.5417
    point = ge.Point(45.2059,75.5417)
    actual = point.point
    assert expected == actual

def test_line():
    expected = 2
    from_point = ge.Point(2,3)
    to_point = ge.Point(2,1)
    actual = ge.Line.length
    assert expected == actual