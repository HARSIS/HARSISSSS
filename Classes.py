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

class Team:
    def __init__(self, Name, Camouflage, Sight, Leader):
        self.Name = Name
        self.Camouflage = Camouflage
        self.Sight = Sight
        self.Leader = Leader

    def Get_Name(self):
        return self.Name

    def Set_Name(self, a):
        self.Name = a

    def Get_Camouflage(self):
        return self.Camouflage

    def Set_Camouflage(self, a):
        self.Camouflage = a

    def Get_Sight(self):
        return self.Sight

    def Set_Sight(self, a):
        self.Sight = a

    def Get_Leader(self):
        return self.Leader

    def Set_Leader(self, a):
        self.Leader = a


class Game:
    def __init__(self, Name, Discription, Zone, Date, Type):
        self.Name = Name
        self.Discription = Discription
        self.Zone = Zone
        self.Date = Date
        self.Type = Type

    def Get_Name(self):
        return self.Name

    def Set_Name(self, a):
        self.Name = a

    def Get_Discription(self):
        return self.Discription

    def Set_Discription(self, a):
        self.Discription = a

    def Get_Zone(self):
        return self.Zone

    def Set_Zone(self, a):
        self.Zone = a

    def Get_Date(self):
        return self.Date

    def Set_Date(self, a):
        self.Date = a

    def Get_Type(self):
        return self.Type

    def Set_Type(self, a):
        self.Type = a


