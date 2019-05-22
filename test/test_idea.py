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

@st.composite
def doubleIntegersLowerThan(draw):
    int1 = draw(st.integers(1, 100))
    int2 = draw(st.integers(1, int1))
    return {'max': int1, 'min': int2}


@given(HX=doubleIntegersLowerThan(),
       VY=doubleIntegersLowerThan())
def test_Board_clean(HX, VY):
    # assume(positionX < nbrCaseV-1)
    # assume(positionY < nbrCaseH-1)
    dirtyBoard = Board(HX['max'], VY['max'])
    cleanBoard = Board(HX['max'], VY['max'])
    assert(cleanBoard.getBoard() == dirtyBoard.getBoard())
    dirtyBoard.getBoard()[VY['min']-1][HX['min']-1].append("testRat")
    print(HX['max'], HX['min'], VY['max'], VY['min'])
    assert(cleanBoard.getBoard() != dirtyBoard.getBoard())
    # assert(False)
