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
    Given 3 pins on first roll and 7 pins on second roll
    The score should be 10
    """
    assert score_for(all_rolls="3/") == 10


def test_no_spare_or_strike_and_second_frame():
    """
    Given a first frame with no strike or spare
    The score should be the sum of all rolls
    """
    assert score_for(all_rolls="31|4") == 8


def test_strike_first_frame_and_normal_second_frame():
    """
    Given a strike on first roll and a normal second frame
    The score should be 10 + second frame + second frame
    """
    assert score_for(all_rolls="X|41") == 20


def test_spare_first_frame_and_normal_second_frame():
    """
    Given a spare on first roll and a normal second frame
    The score should be 10 + third roll + second frame
    """
    assert score_for(all_rolls="3/|41") == 19


def test_two_strikes():
    """
    Given two strikes
    The score should be (10 + 10) + 10
    """
    assert score_for(all_rolls="X|X") == 30


def test_finished_game_no_bonus_balls():
    """
    Given ten frames with no spares or strikes
    The score should be the total of all pins knocked down
    """
    assert score_for(
        all_rolls='01|01|01|01|01|01|01|01|01|01|'
    ) == 10


def test_finished_game_final_spare():
    """
    Given ten frames
    Where 9 are scoring 1 pin
    And the 10th gets a spare
    The score should be 9 + (10 + 10) + 10
    """
    assert score_for(
        all_rolls='01|01|01|01|01|01|01|01|01|1/|X'
    ) == 39
