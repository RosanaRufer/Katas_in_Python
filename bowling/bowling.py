STRIKE = 'X'
SPARE = '/'


def score_for(all_rolls: str):
    """
    Given valid a set of bowling frames
    It returns the total accumulated score
    :param all_rolls: string
    :return: int
    """
    frames = all_rolls.split('|')
    total_score = 0

    for index, frame in enumerate(frames):

        current_frame_score = score_for_frame(frame)

        next_frame = get_next_frame(frames, index)
        if (STRIKE in frame) and next_frame:
            current_frame_score = current_frame_score + score_for_frame(next_frame)
        if (SPARE in frame) and next_frame:
            current_frame_score = current_frame_score + score_for_first_roll(next_frame)

        total_score = total_score + current_frame_score

    return total_score


def get_next_frame(frames: [str], current_index: int):
    """ If next frame exists, returns next frame, else returns False """
    frame = False
    try:
        frame = frames[current_index + 1]
    except IndexError:
        pass

    return frame


def score_for_first_roll(frame: str):
    """ Returns the points of the first roll in a frame """
    first_roll = frame[0]
    if first_roll in [STRIKE, SPARE]:
        return 10
    else:
        return int(first_roll)


def score_for_frame(frame: str):
    """ Returns the points obtained in a frame """
    if SPARE in frame or STRIKE in frame:
        return 10
    else:
        numbers = [int(n) for n in list(frame)]
        return sum(numbers)
