import copy

from expression import *
from command import *

# **** FEEL FREE TO ADD MORE HELPER FUNCTIONS ****
# **** It is not recommended to modify functions without the TODO. ****

def evaluateConst(store, c):
    """Returns the interval [c, c] for a numeric constant."""
    return [c.const, c.const]


def evaluateVar(store, var):
    """Looks up the interval stored for a variable."""
    return store[var.name]


def evaluateUnaryOp(store, lhs, op):
    """Evaluates a unary operation on an interval (supported: 'not')."""
    l = evaluateExpr(store, lhs)
    if op == 'not':
        if l == [0, 1]:
            return l
        if l == [0, 0]:
            return [1, 1]
        if l == [1, 1]:
            return [0, 0]
        else:
            raise Exception('ERROR')


def evaluateBinaryArithOp(store, lhs, rhs, op):
    """Evaluates a binary arithmetic operation on two intervals. See expression.py for supported ops."""
    # TODO
    raise NotImplementedError("evaluateBinaryArithOp not implemented")


def evaluateBinaryComparisonOp(store, lhs, rhs, op):
    """Evaluates a binary comparison between two intervals. See expression.py for supported ops."""
    # TODO
    raise NotImplementedError("evaluateBinaryComparisonOp not implemented")


def evaluateBinaryLogicalOp(store, lhs, rhs, op):
    """Evaluates a binary logical connective on two intervals. See expression.py for supported ops."""
    # TODO
    raise NotImplementedError("evaluateBinaryLogicalOp not implemented")


def evaluateExpr(store, expr):
    """Dispatches expression evaluation to the appropriate handler based on expression type."""
    if isinstance(expr, Const):
        return evaluateConst(store, expr)

    elif isinstance(expr, Var):
        return evaluateVar(store, expr)

    elif isinstance(expr, BinaryArithOp):
        return evaluateBinaryArithOp(store, expr.lhs, expr.rhs, expr.op)

    elif isinstance(expr, BinaryComparisonOp):
        return evaluateBinaryComparisonOp(store, expr.lhs, expr.rhs, expr.op)

    elif isinstance(expr, BinaryLogicalOp):
        return evaluateBinaryLogicalOp(store, expr.lhs, expr.rhs, expr.op)

    elif isinstance(expr, UnaryOp):
        return evaluateUnaryOp(store, expr.lhs, expr.op)
    else:
        print('ERROR')
        return None


def executeSkip(store):
    """Returns the store unchanged."""
    return store


def executeAssignment(store, command):
    """Evaluates the RHS expression and updates the store with the result."""
    # TODO
    raise NotImplementedError("executeAssignment not implemented")


def executeSequence(store, command):
    """Executes two statements in order, threading the store through."""
    # TODO
    raise NotImplementedError("executeSequence not implemented")

def executeIte(store, command):
    """Executes an if-then-else statement. See command.py for the command class definition."""
    # TODO
    raise NotImplementedError("executeIte not implemented")

def executeAssert(store, command):
    """Evaluates the assertion expression and prints whether it passed or failed."""
    interval = evaluateExpr(store, command.expr)

    if interval == [1, 1]:
        print('ASSERT PASSED')
    else:
        print('ASSERT FAILED')
    return store


def executeCommand(store, command):
    """Dispatches command execution to the appropriate handler based on command type."""
    if isinstance(command, Skip):
        return executeSkip(store, command)
    elif isinstance(command, Assignment):
        return executeAssignment(store, command)
    elif isinstance(command, Sequence):
        return executeSequence(store, command)
    elif isinstance(command, Assert):
        return executeAssert(store, command)
    elif isinstance(command, Ite):
        return executeIte(store, command)
    else:
        print('ERROR')
        return None
