class DectoBin:
    def __init__(self,n):
        self.n = n.strip()
        self.Dec = n.strip()
        self.list_Dec = list(self.Dec)

    #nhận diện số thập phân
    def discern_DectoBin(self):

        lst_numbers = '0123456789'
        result = None
        count = 0
        for i in self.list_Dec:
            if i in lst_numbers:
                count += 1
                
        if count  == len(self.list_Dec):
            result = True
        else:
            result = False
        return result

    #hàm chuyển đổi
    def Convert_Bin(self):
        self.n = int(self.n)
        lst = []
        while self.n :
            a = int(self.n%2)
            lst.append(a)
            self.n = int(self.n/2)
        string = ""
        for i in lst[::-1]:
            string += str(i)
        if sum(list(map(int,self.Dec))) == 0:
            string ='0'
        return string
        
    def show(self):
        if DectoBin.discern_DectoBin(self):
            txt = str(DectoBin.Convert_Bin(self))
        else:
            txt = False
        return txt

