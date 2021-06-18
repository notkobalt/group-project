import requests

class Calc:
    def __init__(self, series):

        if series < 0 or series > 50:
            raise ValueError("Series must be between 0 and 50.")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.calc_series()

    def calc_series(self):
        limit = self._series
        f = [1, 2]
        while limit > 0:
            self.set_data(f[0])
            f = [f[1], ((f[1]*2))]
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
        return self._list[self._dictID -1]

    def get_sequence(self, nth):
        return self._dict[nth]

if __name__ == "__main__":
    n= 10

    calculation = Calc(n)

    #print(f"Numbers for {n} = {calculation.number}")
    #print(f"series for {n} = {calculation.list}")

    #for i in range(n):
        #print(f"sequence {i + 1} = {calculation.get_sequence(i)}")

