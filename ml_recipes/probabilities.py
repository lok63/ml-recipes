
def complement(p:float) -> float:
    """
    :param p:
    :return: 1 - p
    """
    return 1-p


def joint(p_A: float, p_B : float) -> float:
    return p_A * p_B


def total_probability(p_disease: float, p_pos_given_disease: float, p_pos_given_no_disease: float) -> float:
    """
    :param p_disease: P(c)
    :param p_pos_given_disease:  P(c | pos)
    :param p_pos_given_no_disease: P(-c | pos)
    :return: P(pos)
    """
    p_not_disease = complement(p_disease)

    total = (p_disease * p_pos_given_disease) + (p_not_disease * p_pos_given_no_disease)

    return total


def bayes(p_c: float, p_pos_given_c : float, p_pos_given_not_c : float) -> float:
    """
    :param p_c: P(c)
    :param p_pos_given_c:  P(Pos|c)
    :param p_pos_given_not_c: P(Pos| -c)
    :return: Posterior : P(c|Pos)
    """

    p_pos = total_probability(p_c, p_pos_given_c, p_pos_given_not_c)
    posterior = p_pos_given_c * p_c / p_pos
    return posterior


if __name__ == '__main__':
    # Find posterior probability
    p_c = 0.2
    p_pos_given_c = 0.9
    p_pos_given_given_not_c = 0.5

