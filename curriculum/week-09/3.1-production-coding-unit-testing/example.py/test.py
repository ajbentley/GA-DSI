import pytest as pytest


import examples
#
# def test_area_calculation():
#     assert examples.rectangle_area(10,2) == 20
#
# def test_area_type_handling():
#     with pytest.raises(TypeError):
#         examples.rectangle_area(5, 'testing')
#
# def test_stopwords():
#     sentence = "the quick brown fox"
#     stopwords = ["the", "a"]
#  assert examples.strip_stopwords(sentence,stopwords) != "the quick brown fox"
#     assert examples.strip_stopwords(sentence,stopwords) == "quick brown fox"

import cardgames


@pytest.fixture()
def setup():
    w = cardgames.War()
    w.handOne.add_card(cardgames.Card())
    return w


def test_equal_hands(setup):

    setup.deal()
    assert len(setup.handOne.cards) == len(setup.handTwo.cards)
