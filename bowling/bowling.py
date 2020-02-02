
def score_for(all_rolls):
    """
    Given a set of bowling frames
    It returns the total score accumulated
    :param all_rolls: string
    :return: int
    """
    if all_rolls == 'X' or '/' in all_rolls:
        return 10
    else:
        return int(all_rolls)
