class DectoHex:
    def __init__(self,n):
        self.n = n.strip()
        self.Dec = n.strip()
        self.list_Dec = list(self.Dec)

    #hàm nhận diện số thập phân
    def discern_DectoHex(self):

        lst_numbers = '0123456789'
        result = None
        count = 0
        for i in self.list_Dec:
            if i in lst_numbers:
                if i == ' ':
                    pass
                count += 1
        if count == len(self.list_Dec):
            result = True
        else:
            result = False
        return result

    #hàm chuyển đổi
    def Convert_Hexa(self):
        self.n = int(self.n)
        lst = []
        while self.n :
            a = int(self.n%16)
            if a == 10:
                a = 'A'
            elif a==11:
                a = 'B'
            elif a==12:
                a = 'C'
            elif a==13:
                a = 'D'
            elif a==14:
                a = 'E'
            elif a==15:
                a = 'F'
            lst.append(a)
            self.n = int(self.n/16)
        string = ""
        for i in lst[::-1]:
            string += str(i)

        if sum(list(map(int,self.Dec))) == 0:
            string ='0'
        return string

    def show(self): 
        if DectoHex.discern_DectoHex(self):
            txt = str(DectoHex.Convert_Hexa(self))
        else:
            txt = False
        return txt
