class Alpha:
    def display_alpha(self, x):
        print('Welcome, Alpha', x)


class Beta(Alpha):
    def display_beta(self):
        print("Welcome beta")

    def __init__(self):
        self.display_gamma = super().display_alpha

    def display_gamma(self):
        print('Welcome, Gamma')


obj = Beta()
# obj.display_beta()
obj.display_gamma(8)
