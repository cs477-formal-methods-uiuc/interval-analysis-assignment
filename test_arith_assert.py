from command import *
from expression import *

from interval import executeCommand

def test_case1(executeCommand):
    """
    Expected output:
        ---TEST CASE 1---
        ASSERT FAILED
        ASSERT PASSED
        ASSERT FAILED
        ASSERT PASSED
    """
    print('---TEST CASE 1---')
    store = {'x': [-1, 1], 'y': [3, 5]}

    s1 = Assignment(Var('z'), BinaryArithOp(Var('x'), Var('y'), '*'))

    s2 = Assert(BinaryComparisonOp(Var('z'), Const(-5), '>'))
    program = Sequence(s1, s2)
    # ASSERT FAILED
    executeCommand(store, program)

    s2 = Assert(BinaryComparisonOp(Var('z'), Const(-5), '>='))
    program = Sequence(s1, s2)
    # ASSERT PASSED
    executeCommand(store, program)

    s2 = Assert(BinaryComparisonOp(Var('z'), Const(5), '<'))
    program = Sequence(s1, s2)
    # ASSERT FAILED
    executeCommand(store, program)

    s2 = Assert(BinaryComparisonOp(Var('z'), Const(5), '<='))
    program = Sequence(s1, s2)
    # ASSERT PASSED
    executeCommand(store, program)


# TODO: FEEL FREE TO ADD MORE TESTS

if __name__ == '__main__':
    test_case1(executeCommand)
