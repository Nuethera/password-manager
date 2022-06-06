import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
class Passgen:

    def __init__(self):
        self.nr_letters = 8
        self.nr_symbols = 4
        self.nr_numbers = 4

    def makepass(self):
        hard_p_l = []
        for i in range(0, self.nr_letters):
            hard_p_l.append(random.choice(letters))
        for i in range(0, self.nr_symbols):
             hard_p_l.append(random.choice(symbols))
        for i in range(0, self.nr_numbers):
            hard_p_l.append(random.choice(numbers))
        random.shuffle(hard_p_l)
        hard_p = "".join(hard_p_l)
        return hard_p
