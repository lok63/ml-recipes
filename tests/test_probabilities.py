from ml_recipes import probabilities


def test_bayes():
    # when
    p_c = 0.2
    p_pos_given_c = 0.9
    p_pos_given_given_not_c = 0.5

    posterior = probabilities.bayes(p_c, p_pos_given_c, p_pos_given_given_not_c)

    assert round(posterior, 4) == round(0.3103448275862069, 4)