#class function
class rsa:
    def __init__(self, message, key1, key2):
        self._message = message
        self._key1 = key1
        self._key2 = key2

        self.func(message, key1, key2)

    def func(self, message, key1, key2):
        #empty variable
        output = []
        #loop for entire message
        for i in range (0, len(message)):
            char = message[i]
            #replace letters in message w/ encrypted values
            C = chr((ord(char) ^ key1) % key2)
            #append list
            output.append(C)

        #turn output into a string
        output = ''.join(output)
        #return output
        return output

    #callable properties "getters"
    @property
    def message(self):
        return self._message

    @property
    def key1(self):
        return self._key1

    @property
    def key2(self):
        return self._key2

    @property
    def end(self):
        return self.func(message, key1, key2)

#test run
if __name__ == '__main__':
    #testing values
    message = "Hello World!"
    key1 = 29
    key2 = 12450239511112411112513261923421
    #construct class
    encoded = rsa(message, key1, key2)
    print(encoded.message)
    print(encoded.key1)
    print(encoded.key2)
    print(encoded.end)