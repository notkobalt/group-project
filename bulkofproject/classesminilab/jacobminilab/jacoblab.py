import random

#list for all characters i want to display, including from shows/video games i like.
charlist1 = ["Mario from Super Mario", "Luigi from Super Mario", "Itadori Yuuji from Jujutsu Kaisen", "Satoru Gojo from Jujutsu Kaisen", "Nagisaki Nobara from Jujutsu Kaisen", "Fushigoro Megumi from Jujutsi Kaisen", "Hori Kyouko from Horimiya", "Miyamura Izumi from Horimiya", "Naruto Uzumaki from Naruto", "Sasuke Uchiha from Naruto"]


#defining class Characters and the init for the blueprint (self and series being used)
class Characters:
    def __init__(self, series):

        #setting minimum/maximum values for when a number is inputted that doesn't fit the criteria of the amount of characters listed
        if series < 0 or series > 10:
            raise ValueError('Series has to be between 0 and 10')
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0

        self.character_series()

    #defining my character series and setting the self series; essentially the limit.
    def character_series(self):
        limit = self._series
        f = [(random.sample(charlist1, k=self._series))]
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit -= self.series

    #fibonacci data; instance variables for the class. (list, dict, etc..)
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    #getters retrieving values of the properties; setting attributes for my class, Characters.
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
    #print(f"Here is a character from a show/video game! = {chars.list}")
