import random

charlist1 = ["Mario", "Luigi", "Itadori Yuuji", "Satoru Gojo", "Nagisaki Nobara", "Naruto Uzumaki", "Sasuke Uchiha"]

charlist2 = ["Mario", "Luigi", "Satoru Gojo"]


class Characters:
    def __init__(self, series):
        if series < 0 or series > 4:
            raise ValueError("Series has to be between 0 and 4")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0

        self.character_series()

    def character_series(self):
        limit = self._series
        f = [(random.sample(charlist1, k =1))]
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit -=1

    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    def get_sequence(self, nth):
        return self._dict[nth]

if __name__ == "__main__":
    a = 1
    chars = Characters(a/a)
    print(f"These are some video game/show characters = {chars.list}")
