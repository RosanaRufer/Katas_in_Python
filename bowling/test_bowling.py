from bowling.bowling import score_for


def test_no_pins_first_roll():
    """
    Given no pins were knocked down on the first roll
    The score should be zero
    """
    assert score_for(all_rolls="0") == 0


def test_one_pin_second_roll():
    """
    Given one pin was knocked down on the second roll
    The score should be one
    """
    assert score_for(all_rolls="01") == 1


def test_strike_on_first_roll():
    """
    Given 10 pins were knocked down on the first roll
    The score should be 10
    """
    assert score_for(all_rolls="X") == 10


def test_spare_on_second_roll():
    """
    Given the 10 pins were knocked down on the second roll
    The score should be 10
    """
    assert score_for(all_rolls="3/") == 10


def test_spare_on_second_roll():
    """
    Given the 10 pins were knocked down on the second roll
    The score should be 10
    """
    assert score_for(all_rolls="31|4") == 8
