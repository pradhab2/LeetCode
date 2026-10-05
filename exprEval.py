""" Trying to evaluate 3*(x+y)
                  and  3*x+y  """


class Expr:
    pass


class Times(Expr):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return "(" + str(self.l) + "*" + str(self.r) + ")"

    def eval(self, env):
        return self.l.eval(env) * self.r.eval(env)


class Plus(Expr):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return "(" + str(self.l) + "+" + str(self.r) + ")"

    def eval(self, env):
        return self.l.eval(env) + self.r.eval(env)


class Const(Expr):

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def eval(self, env):
        return self.val


class Var(Expr):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def eval(self, env):
        return env[self.name]


# e1 = 3*(x+y)
# e2 = 3*x+y

e1 = Times(Const(3), Plus(Var("x"), Var("y")))
e2 = Plus(Times(Const(3), Var("x")), Var("y"))

print(e1)
print(e2)

env = {"x": 5, "y": 4}

print(e1.eval(env))
print(e2.eval(env))

# O/P:
# (3*(x+y))
# ((3*x)+y)
# 27
# 19
