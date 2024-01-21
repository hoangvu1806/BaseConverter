from tkinter.ttk import*
from tkinter import*
from PIL import Image, ImageTk
#khai báo các thư viện chuyển đổi cơ số tự làm
from DectoHex import*
from DectoBin import*
from BintoHex import*
from BintoDec import*
from HextoDec import*
from Hextobin import*


convert_success = '''Đã chuyển đổi thành công!
Nhấn nút Xóa để tiếp tục.'''
convert_Dec_unsuccess = '''Số bạn vừa nhập không phải 
là số có dạng cơ số thập phân!'''
convert_Bin_unsuccess =  '''Số bạn vừa nhập không phải 
là số có dạng cơ số nhị phân!'''
convert_Hex_unsuccess = '''Số bạn vừa nhập không phải 
là số có dạng cơ số thập lục phân!'''
#Hàm chuyển đổi

def click_button():

    text2.delete(1.0,END)
    if (str(text1.get(1.0,END)).strip() == '') :
        a = text2.insert(END,'')
        return a

    elif combo_box1.current() == combo_box2.current():
        if combo_box1.current() == 0:
            b = DectoBin(str(text1.get(1.0,END)).strip())
            if b.show()==False:
                Notice_box.configure(text = convert_Dec_unsuccess,font= ('Arial', 9,'bold italic'),fg = "#E0013F")
                return
            else:
                Notice_box.configure(text = '')
                a = text2.insert(END,text1.get(1.0,END))
                return         

        elif combo_box1.current() == 1:
            b = BintoDec(str(text1.get(1.0,END)).strip())
            if b.show()==False:
                Notice_box.configure(text = convert_Bin_unsuccess,font= ('Arial', 9,'bold italic'),fg = "#E0013F")
                return 
            else:
                Notice_box.configure(text = '')
                a = text2.insert(END,text1.get(1.0,END))
                return     

        elif combo_box1.current() == 2:
            b = HextoDec(str(text1.get(1.0,END)).strip())
            if b.show() == False:
                Notice_box.configure(text = convert_Hex_unsuccess,font= ('Arial', 11,'bold italic'),fg = "#E0013F")                
                return
            else:
                Notice_box.configure(text = '')
                a = text2.insert(END,text1.get(1.0,END))
                return     
                                                 
        a = text2.insert(END,text1.get(1.0,END))
        Notice_box.configure(text = 'Vui lòng chọn cơ số đầu vào!',fg = "#F93F02",font= ('Arial', 11,' bold italic'))
        return a

    elif combo_box1.current() == 0:
        # Dec to Bin
        if combo_box2.current() == 1:
            b = DectoBin(str(text1.get(1.0,END)).strip())
            if b.show(): 
                Notice_box.configure(text = convert_success,fg = "#0939A6",font= ('Arial', 10,'bold italic'))
                output = text2.insert(END,str(DectoBin(str(text1.get(1.0,END)).strip()).show()))
                return output
            else:
                Notice_box.configure(text = convert_Dec_unsuccess,font= ('Arial', 9,'bold italic'),fg = "#E0013F")
                return 
        
        # Dec to Hex
        elif combo_box2.current() == 2:
            b = DectoHex(str(text1.get(1.0,END)).strip())
            if b.show(): 
                Notice_box.configure(text = convert_success,fg = "#0939A6",font= ('Arial', 10,'bold italic'))
                output = text2.insert(END,str(DectoHex(str(text1.get(1.0,END)).strip()).show()))
                return output
            else:
                Notice_box.configure(text = convert_Dec_unsuccess,font= ('Arial', 9,'bold italic'),fg = "#E0013F")
                return 

    elif  combo_box1.current() == 1:
            #Bin to Dec
        if combo_box2.current() == 0:
            b = BintoDec(str(text1.get(1.0,END)).strip())
            if b.show(): 
                Notice_box.configure(text = convert_success,fg = "#0939A6",font= ('Arial', 10,'bold italic'))
                output = text2.insert(END,str(BintoDec(str(text1.get(1.0,END)).strip()).show()))
                return output
            else:
                Notice_box.configure(text = convert_Bin_unsuccess,font= ('Arial', 9,'bold italic'),fg = "#E0013F")
                return 
        #Bin to Hex
        if combo_box2.current() == 2:
            b = BintoHex(str(text1.get(1.0,END)).strip())
            if b.show(): 
                Notice_box.configure(text = convert_success,fg = "#0939A6",font= ('Arial', 10,'bold italic'))
                output = text2.insert(END,str(BintoHex(str(text1.get(1.0,END)).strip()).show()))
                return output
            else:
                Notice_box.configure(text = convert_Bin_unsuccess,font= ('Arial', 9,'bold italic'),fg = "#E0013F")
                return 

    elif  combo_box1.current() == 2:
        # Hex to Dec
        if combo_box2.current() == 0:
            b = HextoDec(str(text1.get(1.0,END)).strip())
            if b.show(): 
                Notice_box.configure(text = convert_success,fg = "#0939A6",font= ('Arial', 10,'bold italic'))
                output = text2.insert(END,str(HextoDec(str(text1.get(1.0,END)).strip()).show()))
                return output
            else:
                Notice_box.configure(text = convert_Hex_unsuccess,font= ('Arial', 11,'bold italic'),fg = "#E0013F")
                return 
        #Hex to Bin
        if combo_box2.current() == 1:
            b = HextoBin(str(text1.get(1.0,END)).strip())
            if b.show(): 
                Notice_box.configure(text = convert_success,fg = "#0939A6",font= ('Arial', 10,'bold italic'))
                output = text2.insert(END,str(HextoBin(str(text1.get(1.0,END)).strip()).show()))
                return output
            else:
                Notice_box.configure(text = convert_Hex_unsuccess,font= ('Arial', 11,'bold italic'),fg = "#E0013F")
                return
        

#Hàm xóa dữ liệu
def clear():
    text1.delete(1.0,END)
    text2.delete(1.0,END)
    Notice_box.configure(text ='')

#-----------------------------------------------------Tạo cửa sổ chính-------------------------------------------------------

root = Tk()
root.title("Chuyển đổi cơ số")
root.iconbitmap("icon.ico")
root.geometry("500x350+440+100")
root.resizable(width=False,height=False)
root.configure(background='#24292E')

#chèn ảnh
load = Image.open("background.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0,y=0)

#tạo nơi nhập/xuất số
text1 = Text(root,height=1, width=15,fg = ("#FFFFFF"),bg='#474E56',font = ('Cambria',18))
text1.place(x=30,y=100)
text2 = Text(root,height=1, width=15,fg = ("#FFFFFF"),bg='#474E56',font = ('Cambria',18))
text2.place(x= 270,y= 100)

#tạo list 1
valCombo1 = ('Thập Phân','Nhị Phân','Thập Lục Phân')
varCombo1 = StringVar()
varCombo1.set('< Cơ số đầu vào >')
combo_box1 = Combobox(root,width=14 ,values=valCombo1,font = ('Times New Roman',10,"bold"), textvariable=varCombo1)
combo_box1.place(x = 30,y = 132)

#tạo list 2
valCombo2 = ('Thập Phân','Nhị Phân','Thập Lục Phân')
varCombo2 = StringVar()
varCombo2.set('< Cơ số đầu ra >')
combo_box2 = Combobox(root,width=14 ,values=valCombo2,font = ('Times New Roman',10,"bold") , textvariable=varCombo2)
combo_box2.place(x = 350, y = 132)

#tạo nút convert
butt1 = Button(root,text = "Chuyển",width= 10,height= 1,bg='#00DCFA',command = click_button)
butt1.place(x = 173, y = 160)
#tạo nút clear
butt2 = Button(root,text = "Xóa",width= 10,height= 1,bg='#6C0613',fg = "#FFFFFF",command = clear)
butt2.place(x = 253, y = 160)

#Tạo bản thông báo
Notice_box = Label(text= '',font= ('Arial', 12,'italic'),fg = "#95151B",bg = "#BBBBBB")
Notice_box.place(x = 145, y = 225)


lbl1 = Label(text = "Creating by Hoang Vu",font= (None,10,'italic'),fg = "#FFFFFF",bg = "#24292E")
lbl1.place(x = 200, y = 330)

root.mainloop()

######################################################################################################################
