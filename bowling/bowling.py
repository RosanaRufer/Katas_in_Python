def score_for(all_rolls):
    """
    Given a set of bowling frames
    It returns the total score accumulated
    :param all_rolls: string
    :return: int
    """
    frames = all_rolls.split('|')
    nframes = len(frames)

    if nframes > 1:
        index = 0
        acc = 0
        while index < 10 and nframes > index:
            sff = score_for_frame(frames[index])
            acc = acc + sff
            if ('X' in frames[index]) and nframes > index:
                acc = acc + score_for_frame(frames[index + 1])
            if ('/' in frames[index]) and nframes > index:
                acc = acc + score_for_first_roll(frames[index + 1])
            index = index + 1
        return acc
    else:
        return score_for_frame(all_rolls)


def score_for_first_roll(frame):
    first_roll = frame[0]
    if first_roll in ['X', '/']:
        return 10
    else:
        return int(first_roll)


def score_for_frame(frame):
    if frame == 'X' or '/' in frame:
        return 10
    else:
        numbers = [int(n) for n in list(frame)]
        return sum(numbers)
