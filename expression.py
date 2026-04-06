class Expression:
    """Base class for all expression types in the language AST."""
    def __init__(self):
        pass


class Const(Expression):
    """A numeric constant expression."""
    def __init__(self, c):
        self.const = c


class Var(Expression):
    """A variable reference expression."""
    def __init__(self, name):
        self.name = name


class UnaryOp(Expression):
    """A unary operation applied to an expression (supported: 'not')."""
    def __init__(self, lhs, op):
        self.lhs = lhs
        self.op = op
        assert op in ['not']


class BinaryArithOp(Expression):
    """A binary arithmetic operation on two expressions (supported: '+', '-', '*')."""
    def __init__(self, lhs, rhs, op):
        self.lhs = lhs
        self.rhs = rhs
        self.op = op
        assert op in ['+', '-', '*']


class BinaryComparisonOp(Expression):
    """A binary comparison between two expressions (supported: '<', '<=', '>', '>=', '==')."""
    def __init__(self, lhs, rhs, op):
        self.lhs = lhs
        self.rhs = rhs
        self.op = op
        assert op in ['<', '<=', '>', '>=', '==']


class BinaryLogicalOp(Expression):
    """A binary logical connective between two expressions (supported: 'and', 'or', 'implies')."""
    def __init__(self, lhs, rhs, op):
        self.lhs = lhs
        self.rhs = rhs
        self.op = op
        assert op in ['and', 'or', 'implies']
