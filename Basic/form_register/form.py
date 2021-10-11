#tkinter ini merupakan sebuah GUI yang digunakan oleh python secara build in yang artinya tidak perlu menginstall tambahan yang lain atau bisa kita katakan jika tkinter ini sudah menjadi satu kesatuan dengan bahasa pemrograman python, jika kita menginstall python, maka kita juga menginstall Tkinter ini juga
from tkinter import * 
import tkinter.font


root = Tk()
root.geometry("370x650") # Mengatur ukuran


changefont = tkinter.font.Font(size=20) # Memberi ukuran font pada Judul
judl = Label(root,text = "REGISTER",font =changefont) # Memberi label pada judul
judl.place(x =130,y = 10) # Mengatur penempatan Label judul

labelfr = LabelFrame(root,text = "Hasil",padx=20,pady=40) # Mengatur padding pada 'Hasil'
labelfr.place(x = 60,y = 400) # Mengatur penempatan Hasil

# Memberi penamaan dan label pada form 
nama = Label(root,text = "Nama :")
email = Label(root,text = "Email : ")
noTelp = Label(root,text = "No Telp : ")
password = Label(root,text = "Password : ")
password2 = Label(root,text = "Masukkan Password Lagi : ")
kebangsaan = Label(root,text = "Kebangsaan : ")
jeniskelamin = Label(root,text = "Jenis Kelamin : ")

# Memberi kolom pada form
e1 = Entry(root,width=40) # Penempatan kolom & lebar untuk label nama
e2 = Entry(root,width=40) # Penempatan kolom & lebar untuk label email
e3 = Entry(root,width=40) # Penempatan kolom & lebar untuk label noTelp
e4 = Entry(root,width=40,show="*") # Penempatan kolom & lebar untuk label password #show "*" berfungsi ketika kita menginputkan password akan otomatis berformat "*"
e5 = Entry(root,width=40,show="*") # Penempatan kolom & lebar untuk label password2 #show "*" berfungsi ketika kita menginputkan password akan otomatis berformat "*"
e6 = Entry(root,width=40) # Penempatan kolom & lebar untuk label kebangsaan
#dikarenakan e7 / (jeniskelamin = Label(root,text = "Jenis Kelamin : ")) bukan kolom, melainkan radio button maka tidak masuk kegolongan kolom


# Mengatur tata letak label pada form
nama.place(x = 20, y =50)
email.place(x = 20, y =90)
noTelp.place(x = 20, y =130)
password.place(x = 20, y =170)
password2.place(x = 20, y =210)
kebangsaan.place(x = 20, y =250)
jeniskelamin.place(x = 20, y =295)


e1.place(x = 20, y = 70) #Penempatan kolom & lebar untuk label nama
e2.place(x = 20, y = 110) #Penempatan kolom & lebar untuk label email
e3.place(x = 20, y = 150) #Penempatan kolom & lebar untuk label noTelp
e4.place(x = 20, y = 190) #Penempatan kolom & lebar untuk label password
e5.place(x = 20, y = 230) #Penempatan kolom & lebar untuk label password2
e6.place(x = 20, y = 270) #Penempatan kolom & lebar untuk label kebangsaan



r = StringVar()
r.set("none")

rb = Radiobutton(root,text = "Male",variable=r,value="male").place(x = 140,y =295 ) # Mengatur Radio Button pada label jeniskelamin
rb2 = Radiobutton(root,text = "Female",variable=r,value="female").place(x = 200,y =295 ) # Mengatur Radio Button pada label jeniskelamin


# Mengelompokkan Hasil setelah button 'Register' diclick  
def login():
    class orang:
        def __init__(self,nama,email,noTelp,password,password2,kebangsaan,jeniskelamin):
            self.nama = nama
            self.email = email
            self.noTelp = noTelp
            self.password = password
            self.password2 = password2
            self.kebangsaan = kebangsaan
            self.jeniskelamin = jeniskelamin
        def hasil(self):
            Label(labelfr,text="Nama = "+self.nama+"\nEmail = "+self.email+"\nNo Telp ="+self.noTelp+"\nPassword = "+self.password+"\nMasukkan Password Lagi ="+self.password2+"\nKebangsaan ="+self.kebangsaan+"\nJenis Kelamin ="+self.jeniskelamin).grid()
    ditampilkan = orang(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(), r.get())
    ditampilkan.hasil()



btn = Button(root,text = "Register",command=login).place(x = 150,y = 350) # Penamaan dan Penempatan Button 'Register'

root.mainloop()