from bowling.bowling import score_for


def test_no_pins_first_frame():
    """
    Given no pins were knocked down on the first frame
    The score should be zero
    """
    assert score_for(all_rolls="0") == 0
