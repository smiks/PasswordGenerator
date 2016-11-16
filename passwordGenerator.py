class PasswordGenerator:
    """
    Using this class you can set rules used for generating password
    and generate it using generate_password function.
    """

    def __init__(self, length=32, alphabet={"alpha", "num", "special"}):
        """
        Used to set rules used for generating password.
        :param length [int]: length of password
        :param alphabet [set]: what rules should be applied.
                        available rules:
                        - alpha (a-z,A-Z)
                        - num (0-9)
                        - special (special characters: #$%&/()=?-+*.,:;!@{}[]^  )
        """
        self.length = length
        self.alphabet = alphabet

    def generate_password(self):
        """
        Generates password using defined rules.
        :return: generated password
        """
        from random import choice, randint
        self.specials = list("#$%&/()=?-+*.,:;!@{}[]^")
        self.alphas = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.nums = list("0123456789")

        self.password = ""

        divider = 0

        combs = {1: self.alphas, 2: self.nums, 3: self.specials}

        if "alpha" in self.alphabet:
            divider += 1

        if "num" in self.alphabet:
            divider += 1

        if "special" in self.alphabet:
            divider += 1

        for _ in range(self.length):
            pick = randint(1, divider)
            character = choice(combs[pick])

            self.password += character

        return self.password


    def get_password(self):
        return self.password



if __name__ == "__main__":

    pg = PasswordGenerator()
    password = pg.generate_password()
    print(password)