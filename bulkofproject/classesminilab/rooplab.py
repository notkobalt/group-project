class numlist:
    def __init__(self, series):
        if series < 3 or series > 100:
            raise ValueError("Series must be between 3 and 100")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.calc_series()

    def calc_series(self):
        limit = self._series
        f = [0, 1]
        while limit > 0:
            self.set_data(f[0])
            f = [f[1], f[0] + f[1]]
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
    '''Value for testing'''
    n = 21
    '''Constructor of Class object'''
    numlist = numlist(n)

    #print(f" number for {n} = {numlist.number}")
    #print(f" series for {n} = {numlist.list}")

    #for i in range(n):
        #print(f" sequence {i + 1} = {numlist.get_sequence(i)}")
