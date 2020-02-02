
def score_for(all_rolls):
    """
    Given a set of bowling frames
    It returns the total score accumulated
    :param all_rolls: string
    :return: int
    """
    frames = all_rolls.split('|')

    if len(frames) > 1:
        return score_for_frame(frames[0]) + score_for_frame(frames[1])
    else:
        return score_for_frame(all_rolls)

def score_for_frame(frame):
    if frame == 'X' or '/' in frame:
        return 10
    else:
        return sum([int(n) for n in list(frame)])
