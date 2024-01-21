class HextoDec:

    def __init__(self,n):
        self.Hexa = n.strip()
        self.list_Hexa =  list(self.Hexa)

    #hàm nhận diện số thập lục phân
    def discern_HextoDec(self):
        lst1 = '0123456789AaBbCcDdEeFf'
        result = None
        count = 0
        for i in self.list_Hexa:
            if i in lst1:
                if i == ' ':
                    pass
                count += 1
        if count == len(self.list_Hexa):
            result = True
        else:
            result = False
        return result

    #Hàm chuyển đổi
    def Convert_Dec(self):
        Dec = 0
        a = len(self.Hexa)
        for i in self.list_Hexa:
            if (i=='A')or(i =='a'):
                i = 10
            elif (i=='B')or(i =='b'):
                i = 11
            elif (i=='C')or(i =='c'):
                i = 12
            elif (i=='D')or(i =='d'):
                i = 13
            elif (i=='E')or(i =='e'):
                i = 14
            elif (i=='F')or(i =='f'):
                i = 15
            i = int(i)
            Dec += i*(16**(a-1))
            a -= 1
        return Dec

    def show(self):
        if HextoDec.discern_HextoDec(self):
            txt = str(HextoDec.Convert_Dec(self))
        else:
            txt = False
        return txt
