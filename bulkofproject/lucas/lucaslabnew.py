class Numby:


    def __init__(self, series):
        if series < 2 or series > 100:
            raise ValueError("Series must be between 2 and 100")

        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0

        self.calc_series()

    def calc_series(self):
        limit = self._series
        f = [2000, 1000]
        while limit > 0:
            self.set_data(f[0])
            f = [f[1], (f[1]/2)]
            limit -= 1

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

    n = 18
    Numbers = Numby(n)
    #print(f" num for {n} = {Numbers.number}")
    #print(f" series for {n} = {Numbers.list}")


    #for i in range(n):
        #print(f"# {i+1} = {Numbers.get_sequence(i)}")