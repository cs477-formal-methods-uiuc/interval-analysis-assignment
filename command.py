class Statement:
    """Base class for all statement types in the language AST."""
    def __init__(self):
        pass

class Skip(Statement):
    """A no-op statement that does nothing."""
    def __init__(self):
        pass

class Assignment(Statement):
    """Assigns the value of an expression to a variable (var := expr)."""
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

class Sequence(Statement):
    """Executes two statements in order (s1; s2)."""
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

class Ite(Statement):
    """If-then-else statement: executes s1 if cond holds, otherwise s2."""
    def __init__(self, cond, s1, s2):
        self.cond = cond
        self.s1 = s1
        self.s2 = s2

class Assert(Statement):
    """Asserts that an expression holds; used for property checking."""
    def __init__(self, expr):
        self.expr = expr
