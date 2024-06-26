import pytest
from rock_paper_scissors import GameLogic


@pytest.fixture
def game_logic():
    return GameLogic()


def test_valid_answer(game_logic):
    assert game_logic.valid_answer("rock") == True
    assert game_logic.valid_answer("paper") == True
    assert game_logic.valid_answer("scissors") == True
    assert game_logic.valid_answer("invalid_answer") == False


def test_winning_answer(game_logic):
    assert game_logic.winning_answer("rock", "scissors") == True
    assert game_logic.winning_answer("rock", "paper") == False
    assert game_logic.winning_answer("paper", "rock") == True
    assert game_logic.equal_answer("paper", "scissors") == False
    assert game_logic.winning_answer("scissors", "paper") == True
    assert game_logic.winning_answer("scissors", "rock") == False


def test_equal_answer(game_logic):
    assert game_logic.equal_answer("rock", "rock") == True
    assert game_logic.equal_answer("paper", "paper") == True
    assert game_logic.equal_answer("scissors", "scissors") == True
    assert game_logic.equal_answer("rock", "paper") == False
    assert game_logic.equal_answer("rock", "scissors") == False
    assert game_logic.equal_answer("paper", "scissors") == False
