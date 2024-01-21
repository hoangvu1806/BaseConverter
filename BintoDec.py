class BintoDec:

    def __init__(self,n):
        self.Bin = n.strip()
        self.list_Bin = list(self.Bin)


    #nhận diện số nhị phân
    def discern_BintoDec(self):

        result = None
        count = 0
        for i in self.list_Bin:
            if i =='0'or i =='1':
                count += 1
        if count == len(self.list_Bin):
            result = True
        else:
            result = False
        return result
        
    #hàm chuyển đổi
    def Convert_Bin(self):

        Dec = 0
        a = len(self.Bin)
        for i in self.list_Bin:
            i = int(i)
            Dec +=  i*(2**(a-1))
            a -= 1
        return Dec
    # hàm hiển thị
    def show(self):
        if BintoDec.discern_BintoDec(self):
            txt = str(BintoDec.Convert_Bin(self))
        else:
            txt = False
        return txt
