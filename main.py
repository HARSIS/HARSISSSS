class Player:
    def __init__(self, Phone_Number, Name_SurN, Age, Type, Camouflage):
        self.Phone_Number = Phone_Number
        self.Name_SurN = Name_SurN
        self.Age = Age
        self.Type = Type
        self.Camouflage = Camouflage

    def Get_Phone_Number(self):
        return self.Phone_Number

    def Get_Name_SurN(self):
        return self.Name_SurN

    def Get_Age(self):
        return self.Age

    def Get_Type(self):
        return self.Type

    def Get_Camouflage(self):
        return self.Camouflage

    def Set_Phone_Number(self, a):
        self.Phone_Number = a

    def Set_Name_SurN(self, a):
        self.Name_SurN = a

    def Set_Age(self, a):
        self.Age = a

    def Set_Type(self, a):
        self.Type = a

    def Set_Camouflage(self, a):
        self.Camouflage = a


