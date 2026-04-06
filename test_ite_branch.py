from command import *
from expression import *

from interval import executeCommand

def test_case1(executeCommand):
    """
    Expected output:
        ---TEST CASE 1---
        ASSERT PASSED
        ASSERT PASSED
    """
    print('---TEST CASE 1---')
    store = {'x': [-1, 1], 'y': [3, 5]}
    condition = BinaryComparisonOp(Var('x'), Const(0), '>=')
    then_statement = BinaryArithOp(Var('x'), Var('y'), '+')
    else_statement = BinaryArithOp(Var('x'), Var('y'), '-')
    s1 = Ite(condition, Assignment(Var('z'), then_statement), Assignment(Var('z'), else_statement))

    s2 = Assert(BinaryComparisonOp(Var('z'), Const(-6), '>='))
    program = Sequence(s1, s2)
    # ASSERT PASSED
    executeCommand(store, program)

    s2 = Assert(BinaryComparisonOp(Var('z'), Const(6), '<='))
    program = Sequence(s1, s2)
    # ASSERT PASSED
    executeCommand(store, program)


# TODO: FEEL FREE TO ADD MORE TESTS

if __name__ == '__main__':
    test_case1(executeCommand)
