
def score_for(all_rolls):
    """
    Given a set of bowling frames
    It returns the total score accumulated
    :param all_rolls: string
    :return: int
    """
    frames = all_rolls.split('|')

    if len(frames) > 1:
        index = 0
        acc = 0
        while index < 10 and len(frames) > index:
            acc = acc + score_for_frame(frames[index])
            index = index + 1
        return acc
    else:
        return score_for_frame(all_rolls)

def score_for_frame(frame):
    if frame == 'X' or '/' in frame:
        return 10
    else:
        return sum([int(n) for n in list(frame)])
