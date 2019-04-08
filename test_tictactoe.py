import pytest
import tictactoe as t

def test_create_board():
    assert t.create_board() == [['_' for _ in range(3)] for _ in range(3)]

pytest.main()
