from RatsAndMazes.idea import Board
from hypothesis import given, strategies as st
from hypothesis import example, assume, settings, HealthCheck
import copy

#  pytest -v -l --hypothesis-show-statistics
@given(nbrCaseH=st.integers(1, 100), nbrCaseV=st.integers(1, 100))
def test_Board_Property(nbrCaseH, nbrCaseV):
    board = Board(nbrCaseH, nbrCaseV)
    assert(isinstance(board.getBoard(), type([])))
    assert(len(board.getBoard()) == nbrCaseV)
    for x in range(nbrCaseV):
        assert(len(board.getBoard()[x]) == nbrCaseH)


# @settings(max_examples=200,
#           suppress_health_check=(HealthCheck.filter_too_much,))

rectangle_lists = st.integers(min_value=0, max_value=10).flatmap(lambda n: st.lists(st.lists(st.integers(), min_size=n, max_size=n)))
find(rectangle_lists, lambda x: True)
@given(nbrCaseH=st.integers(1, 100),
       nbrCaseV=st.integers(1, 100),
       positionX=st.integers(1).filter(st.integers(1, 100)),
       positionY=st.integers(1, 99))
def test_Board_clean(nbrCaseH, nbrCaseV, positionX, positionY):
    # assume(positionX < nbrCaseV-1)
    # assume(positionY < nbrCaseH-1)
    dirtyBoard = Board(nbrCaseH, nbrCaseV)
    cleanBoard = Board(nbrCaseH, nbrCaseV)
    dirtyBoard.getBoard()[positionY-1][positionX-1].append("testRat")
    print(nbrCaseH, nbrCaseV, positionX, positionY)
    assert(cleanBoard != dirtyBoard)
    # assert(False)
