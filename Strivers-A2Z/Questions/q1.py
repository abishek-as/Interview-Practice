class Alpha:
    def __init__(self):
        self.__name = "alpha"

    def __str__(self):
        return self.__name
    
    def test(self):
        return "Hi from alpha"


class Beta(Alpha):
    def __init__(self):
        super().__init__()
        self.name = "beta"
    
    def test(self):
        return "Hi from beta"


class Gamma(Beta):
    def __init__(self):
        super().__init__()
        self.name = "gamma"
    
    def test(self):
        return "Hi from gamma"


alpha_obj = Alpha()
beta_obj = Beta()
gamma_obj = Gamma()

# print(alpha_obj, beta_obj, gamma_obj)
print(alpha_obj.test(), beta_obj.test(), gamma_obj.test())

