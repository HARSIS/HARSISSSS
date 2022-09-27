class Player:
    def __init__(self, Phone_Number, Name, Surn, Age, Type, Camouflage):
        self.Phone_Number = Phone_Number #телефон
        self.Name = Name #имя
        self.Surn = Surn #фамилия
        self.Age = Age #возрост
        self.Type = Type #тип
        self.Camouflage = Camouflage #позывной

    def Get_Phone_Number(self):
        return self.Phone_Number

    def Get_Name(self):
        return self.Name
    
    def Get_Surn(self):
        return self.Surn

    def Get_Age(self):
        return self.Age

    def Get_Type(self):
        return self.Type

    def Get_Camouflage(self):
        return self.Camouflage

    def Set_Phone_Number(self, a):
        self.Phone_Number = a

    def Set_Name(self, a):
        self.Name = a
        
    def Set_Surn(self, a):
        self.Surn = a

    def Set_Age(self, a):
        self.Age = a

    def Set_Type(self, a):
        self.Type = a

    def Set_Camouflage(self, a):
        self.Camouflage = a


