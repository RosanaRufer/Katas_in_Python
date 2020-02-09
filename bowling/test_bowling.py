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
    assert score_for(all_rolls="3/") == 10


def test_no_spare_or_strike_and_second_frame():
    assert score_for(all_rolls="31|4") == 8


def test_strike_first_frame_and_roll_second_frame():
    assert score_for(all_rolls="X|41") == 20


def test_spare_first_frame_and_roll_second_frame():
    assert score_for(all_rolls="3/|41") == 19


def test_two_strikes():
    assert score_for(all_rolls="X|X") == 30


def test_finished_game_no_bonus_balls():
    assert score_for(
        all_rolls='01|01|01|01|01|01|01|01|01|01|'
    ) == 10
