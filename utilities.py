keyword = ["lastName", "firstName", "country", "addressLine1", "addressLine2", "sex", "age"]
counter = 0
const = 170

def base_encription(word):
    word = list(word)
    for i in range(len(word)):
        word[i] = str((ord(word[i]) - const) % 256) + " "

    string = ""
    for elem in word:
        string += elem
    return string

def base_private_number(string):

    value = 0
    power = 1

    for i in range(len(string)):
        value += ord(string[i]) * power
        power *= 2

    return value


class Info:
    def __init__(self): # informatiile necesare completarii oricarui form
        self.infoDict = {}

    def set_value(self, property, value):
        self.infoDict[property] = value

    def get_value(self, property):
        return self.infoDict[property]

    def get_dict(self):
        return self.infoDict

    def print_dict(self):
        for property in self.infoDict:
            print (property + " : " + self.infoDict[property])

class User:
    def __init__(self, id):
        self.id = id
        self.privateValue = 0
        self.password = ""
        self.info = Info()

    def get_encription_value(self, transform = base_private_number):
        return transform(self.password)


    def get_property_value(self, property, mode="clear", transform = base_encription):
        string = self.info.get_value(property)
        if mode == "clear":
            return string
        elif mode == "encripted":
            return transform(string)

    def set_password(self, string): # parola trebuie sa aiba maxim 20 de caractere
        self.password = string

    def get_info_data(self, string): # transmitere de form-data as string de forma string = "despartitor + mesaj"
        string = string.split(string[0])
        string.pop(0)

        for i in range(len(string)):
            self.info.set_value(keyword[i], string[i])
        #self.info.print_dict()

string = " Ana are mere"
u = User(counter)
u.get_info_data(string)
print (u.get_property_value(keyword[0], "encripted"))
u.set_password("zzzzzzzzzzzzzzzzzzzz")
print (u.get_encription_value())