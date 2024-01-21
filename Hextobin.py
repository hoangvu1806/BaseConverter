from DectoBin import*
from HextoDec import*



class HextoBin:

    def __init__(self,n):
        self.Bin = n.strip()
    #hàm nhận diện
    def discern_HextoBin(self):
        result = None
        a = HextoDec(self.Bin)
        if a.show() == False :
            result = False
        else:
            result = True
        return result
    # Hàm chuyển đổi
    def Convert_HextoBin(self):
        a = HextoDec(self.Bin)
        if HextoBin.discern_HextoBin(self) :
            b = DectoBin(str(a.show()))
            Hex = b.Convert_Bin()
        return Hex

    def show(self):
        
        if HextoBin.discern_HextoBin(self):
            txt = str(HextoBin.Convert_HextoBin(self))
        else:
            txt = False
        return txt