class equations:
    #perameters
    def __init__(self, limit):
        #define peramaters
        if limit < 0 or limit > 10:
            raise ValueError("series must be between 0 and 10")
        self._limit = limit
        self._list = [list]
        self._dict = {}
        self._dictID = 0

        self.function()

    #functions
    def function(self):
        limit = self._limit
        array = [0,1]
        while limit > 0:
            self.input_data(array[0])
            array = [array[1], array[0] + array[1]]
            limit = limit - 1

    def input_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID = self._dictID + 1

    #getters
    @property
    def series(self):
        self._limit

    @property
    def list(self):
        self._list

    @property
    def position(self):
        return self._list[self._dictID - 1]

    #method access
    def get_method(self, num):
        self._dict[num]

#test
##test num
x = 7

#build class
eqs = equations(x)

#get data from built class
print({eqs.position})
print({eqs.list})