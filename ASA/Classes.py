class Player:
    def __init__(self, Phone_Number, Name, Surn, Age, Type, Camouflage, Nick):
        self.Phone_Number = Phone_Number  # телефон
        self.Name = Name  # имя
        self.Surn = Surn  # фамилия
        self.Age = Age  # возрост: 12 - 200 лет
        self.Type = Type  # тип игрока: щитовой/sqb/штурмовой/марксман/снайпер/пулемётчик
        self.Camouflage = Camouflage  # камуфляж: MOX/Multicam/EMR/Black/Tan/Olive/другой
        self.Nick = Nick  # позывной

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

    def Get_Nick(self):
        return self.Nick

    def Set_Nick(self, a):
        self.Nick = a


class Team:
    def __init__(self, Name, Camouflage, Sight, Leader):
        self.Name = Name  # название
        self.Camouflage = Camouflage  # камуфляж: MOX/Multicam/EMR/Black/Tan/Olive/другой
        self.Sight = Sight  # сторона: тёмная/светлая/смешанная
        self.Leader = Leader  # командир

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
        self.Name = Name  # название
        self.Discription = Discription  # описание
        self.Zone = Zone  # полигон
        self.Date = Date  # дата
        self.Type = Type  # тип игры: воскреска/большая игра/sqb/ролёвка

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


class Admin:
    def __init__(self, Login, Password, Discription, Banlist_Players, Banlist_Teams):
        self.Login = Login
        self.Password = Password
        self.Discription = Discription
        self.Banlist_Players = Banlist_Players
        self.Banlist_Teams = Banlist_Teams

    def Get_Login(self):
        return self.Login

    def Set_Login(self, a):
        self.Login = a

    def Get_Password(self):
        return self.Password

    def Set_Password(self, a):
        self.Password = a

    def Get_Discription(self):
        return self.Discription

    def Set_Discription(self, a):
        self.Discription = a

    def Get_Banlist_Players(self):
        return self.Banlist_Players

    def Set_Banlist_Players(self, a):
        self.Banlist_Players = a

    def Get_Banlist_Teams(self):
        return self.Banlist_Teams

    def Set_Banlist_Teams(self, a):
        self.Banlist_Teams = a
