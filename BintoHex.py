from BintoDec import*
from DectoHex import*


class BintoHex:

    def __init__(self,n):
        self.Bin = n.strip()
    #hàm nhận diện
    def discern_BintoHex(self):
        result = None
        a = BintoDec(self.Bin)
        if a.show() == False :
            result = False
        else:
            result = True
        return result
    #hàm chuyển đổi
    def Convert_BintoHex(self):
        a = BintoDec(self.Bin)
        if BintoHex.discern_BintoHex(self) :
            b = DectoHex(str(a.show()))
            Hex = b.Convert_Hexa()
        return Hex

    def show(self):
        
        if BintoHex.discern_BintoHex(self):
            txt = str(BintoHex.Convert_BintoHex(self))
        else:
            txt = False
        return txt