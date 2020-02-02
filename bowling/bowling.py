
def score_for(all_rolls):
    """
    Given a set of bowling frames
    It returns the total score accumulated
    :param all_rolls: string
    :return: int
    """
    return int(all_rolls) if all_rolls != 'X' else 10
