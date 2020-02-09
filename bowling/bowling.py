STRIKE = 'X'
SPARE = '/'


def score_for(all_rolls):
    """
    Given a set of bowling frames
    It returns the total score accumulated
    :param all_rolls: string
    :return: int
    """
    frames = all_rolls.split('|')
    last_index = len(frames) - 1
    total_score = 0

    for index, frame in enumerate(frames):
        current_frame_score = score_for_frame(frame)

        next_index = index + 1

        if (STRIKE in frame) and next_index <= last_index:
            current_frame_score = current_frame_score + score_for_frame(frames[next_index])
        if (SPARE in frame) and next_index <= last_index:
            current_frame_score = current_frame_score + score_for_first_roll(frames[next_index])

        total_score = total_score + current_frame_score

    return total_score


def score_for_first_roll(frame):
    first_roll = frame[0]
    if first_roll in [STRIKE, SPARE]:
        return 10
    else:
        return int(first_roll)


def score_for_frame(frame):
    if SPARE in frame or STRIKE in frame:
        return 10
    else:
        numbers = [int(n) for n in list(frame)]
        return sum(numbers)
