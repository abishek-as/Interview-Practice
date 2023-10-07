class Alpha:
    def display_alpha(self):
        print('Welcome, Alpha')
        x = 5
        return x


class Beta(Alpha):
    def display_beta(self):
        print("Welcome beta")

    def __init__(self):
        self.x = super().display_alpha

    def display_gamma(self):
        print('Welcome, Gamma', self.x)


obj = Beta()
obj.display_beta()
obj.display_gamma()
