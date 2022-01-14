import tkinter as tk
from tkinter import *
import mysql.connector
from datetime import datetime
from tkinter import messagebox  
import DetectNumberPlate as dnp
import cv2
from PIL import Image, ImageTk
from tkinter_custom_button import TkinterCustomButton
from pymata4 import pymata4
import time
global k

# arduino bord tanımladık
board = pymata4.Pymata4()

def misafirKaydet():
    if len(str(username.get()))!=0 and len(str(tel.get()))!=0:
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        # veritabanı baglantisi
        mydb=mysql.connector.connect(host="localhost",user="root",password="1453.Muhammed",database="plakalar")
        mycursor=mydb.cursor()
        sorgu="INSERT INTO misafir (ad_soyad, tel, plaka, giris_saat) VALUES (%s, %s, %s, %s)"
        misafirinfos=(str(username.get()), str(tel.get()), plaka, formatted_date)
        mycursor.execute(sorgu, misafirinfos)
        mydb.commit()
        messagebox.showinfo("information",str(mycursor.rowcount)+" adet kayıt eklendi")
        guest_window.destroy()
    else:
        messagebox.showinfo("information","BOŞ ALAN BIRAKMAYINIZ!")

    
def misafirGiris():
    master2.destroy()
    global guest_window
    guest_window=tk.Tk()
    guest_window.title("Misafir Girişi")
    canvas=tk.Canvas(guest_window, height=500, width=800, bg="#2f4f4f")
    canvas.pack()
    image1 = Image.open("bgimage.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=0, y=0)
    tk.Label(guest_window ,text="Misafir Girişi", fg='white', bg="#1f201b", font=("Arial",25)).place(relx=0.41,rely=0.12)
    tk.Label(guest_window, text="Ad-Soyad: ", fg='white', bg="#1f201b", font=("Times",15,"italic")).place(relx=0.3, rely=0.3)
    tk.Label(guest_window, text="Tel: ", fg='white', bg="#1f201b", font=("Times",15,"italic")).place(relx=0.3, rely=0.4)
    global username
    global tel
    username=tk.Entry(guest_window)
    username.place(x=335, y=150, width=200, height=30)
    tel=tk.Entry(guest_window)
    tel.place(x=335, y=200, width=200, height=30)
    TkinterCustomButton(bg_color=None, fg_color="#A93226", hover_color="#CD6155", text_font=None, text="Kaydet", text_color="white", corner_radius=0, width=200, height=55, hover=True, command=misafirKaydet).place(x=332, y=250)

def ssDB():
    if len(str(ad_soyad.get()))!=0 and len(str(tel_no.get()))!=0  and len(str(arac_markasi.get()))!=0 and len(str(arac_modeli.get()))!=0:
        mydb=mysql.connector.connect(host="localhost",user="root",password="1453.Muhammed",database="plakalar")
        mycursor=mydb.cursor()
        sorgu="INSERT INTO kullanicilar (plaka, ad_soyad, tel, blok_no, daire_no, araba_marka, araba_model) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        ssinfos=(plaka, str(ad_soyad.get()), str(tel_no.get()), str(blok_no.get()), int(daire_no.get()), str(arac_markasi.get()), str(arac_modeli.get()))
        mycursor.execute(sorgu, ssinfos)
        mydb.commit()
        messagebox.showinfo("information",str(mycursor.rowcount)+" adet kayıt eklendi")
        user_window.destroy()
    else:
        messagebox.showinfo("information","BOŞ ALAN BIRAKMAYINIZ!")

def ssKaydet():
    master2.destroy()
    global user_window
    user_window=tk.Tk()
    user_window.title("Site Sakini Kayıt Penceresi")
    canvas=tk.Canvas(user_window, height=500, width=800, bg="#2f4f4f")
    canvas.pack()
    
    image1 = Image.open("bgimage.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=0, y=0)
    
    tk.Label(user_window ,text="Site Sakini Kaydı", fg='white', bg="#1f201b", font=("Arial",20)).place(relx=0.35,rely=0.1)
    tk.Label(user_window ,text="Ad-Soyad:", fg='white', bg="#1f201b", font=("Times",15,"italic")).place(relx=0.2,rely=0.27)
    tk.Label(user_window ,text="Tel No:", fg='white', bg="#1f201b", font=("Times",15,"italic")).place(relx=0.2,rely=0.39)
    tk.Label(user_window ,text="Blok No:", fg='white', bg="#1f201b", font=("Times",15,"italic")).place(relx=0.2,rely=0.52)
    tk.Label(user_window ,text="Daire No:", fg='white', bg="#1f201b", font=("Times",15,"italic")).place(relx=0.2,rely=0.64)
    tk.Label(user_window ,text="Araç Markası:", fg='white', bg="#1f201b", font=("Times",15,"italic")).place(relx=0.53,rely=0.27)
    tk.Label(user_window ,text="Araç Modeli:", fg='white', bg="#1f201b", font=("Times",15,"italic")).place(relx=0.53,rely=0.39)
    
    global ad_soyad
    global tel_no
    global blok_no
    global daire_no
    global arac_markasi
    global arac_modeli
    
    ad_soyad=tk.Entry(user_window)
    tel_no=tk.Entry(user_window)
    bloklar=["1.Blok","2.Blok","3.Blok","4.Blok","5.Blok"]
    daireler=[1,2,3,4,5,6,7,8,9,10,11,12]
    blok_no=StringVar()
    blok_no.set(bloklar[0])
    daire_no=IntVar()
    daire_no.set(daireler[0])
    blok_menu=OptionMenu(user_window, blok_no, *bloklar)
    blok_menu.place(x=255, y=262, width=150, height=25)
    daire_menu=OptionMenu(user_window, daire_no, *daireler)
    daire_menu.place(x=255, y=324, width=150, height=25)
    arac_markasi=tk.Entry(user_window)
    arac_modeli=tk.Entry(user_window)
    ad_soyad.place(x=255, y=135, width=150, height=25)
    tel_no.place(x=255, y=195, width=150, height=25)
    arac_markasi.place(x=557, y=136, width=150, height=25)
    arac_modeli.place(x=557, y=200, width=150, height=25)
    saveBtn=TkinterCustomButton(bg_color=None, fg_color="#A93226", hover_color="#CD6155", text_font=None, text="Kaydet", text_color="white", corner_radius=0, width=200, height=55, hover=True, command=ssDB)
    saveBtn.place(x=480, y=270)
    user_window.mainloop()
    
def menu():
    print("menuye girdi")
    
    global master2
    master2=tk.Tk()
    master2.title("Bilinmeyen Plaka")
    tk.Canvas(master2, height=500, width=800, bg="#2f4f4f").pack()
    ust_frame=tk.Frame(bg="black").place(x=0,y=0, height=150, width=800)
    alt_frame=tk.Frame(bg="blue").place(x=0, y=150, height=350, width=800)
    image1 = Image.open("bgimage.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=0, y=0)
    play_image = ImageTk.PhotoImage(Image.open("guestimg.png").resize((150, 150)))
    skip_image = ImageTk.PhotoImage(Image.open("hostimg.png").resize((150, 150)))
    tk.Label(ust_frame, text=plaka, fg="white", bg="#1f201b",font=("Arial", 30)).place(relx=0.42,rely=0.2)
    TkinterCustomButton(alt_frame,text="Misafir", image=play_image, corner_radius=12, command=misafirGiris).place(x=200, y=250, height=150, width=150)
    TkinterCustomButton(alt_frame,text="Site Sakini",image=skip_image,corner_radius=12, command=ssKaydet).place(x=450, y=250, height=150, width=150)    
    master2.mainloop()

def kapiAc():
    # pinleri tanimladik
    pins=[8,10,9,11]
    # step motor tanimladik
    board.set_pin_mode_stepper(400, pins)
    # 90 derece acip kapattik kapiyi
    board.stepper_write(21, -520)
    time.sleep(10)
    board.stepper_write(21, 520)
    
def arayuz(plaka):
    # okunan plaka kontrolu
    mydb=mysql.connector.connect(host="localhost",user="root",password="1453.Muhammed",database="plakalar")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT plaka FROM kullanicilar")
    myresult=mycursor.fetchall()
    print(plaka)
    ctrl=0
    for i in myresult:
        for k in i:
            if plaka==k:
                # eger bu plaka kayitli ise kapi acilacak
                print("Eşit: "+plaka)
                kapiAc()
                time.sleep(5)
                ctrl+=1
                break
    if ctrl==0:
        # esit degilse menu acilacak araba bekleyecek
        print("Eşit Değil: "+plaka)
        mydb2=mysql.connector.connect(host="localhost",user="root",password="1453.Muhammed",database="plakalar")
        mycursor2=mydb2.cursor()
        mycursor2.execute("SELECT plaka,cikis_saat FROM misafir")
        sonuclarim=mycursor2.fetchall()
        if not sonuclarim:
            menu()
        else:
            ctrl_sayi=1
            for t in sonuclarim:
                if t[0]==plaka and t[1]==None:
                    now2 = datetime.now()
                    formatted_date2 = now2.strftime('%Y-%m-%d %H:%M:%S')
                    upd="UPDATE misafir SET cikis_saat=%s WHERE plaka=%s"
                    val=(formatted_date2,plaka)
                    mycursor2.execute(upd, val)
                    mydb2.commit()
                elif ctrl_sayi==len(sonuclarim):
                    menu()
                ctrl_sayi+=1
##########################################
# kameradan videoyu aldik
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)

while True: 
    try:
       success, img = cap.read()
       # plakayi tespit ettik
       plaka = dnp.detectPlate(img)
       # Eğer istenmeyen bir karakter varsa onları siliyoruz
       plaka = plaka.replace("[", "")
       plaka = plaka.replace("]", "")
       if plaka[2] != " " and plaka[0] == "0":
          plaka = plaka[1:]
          
       print("Plaka: " + plaka, "tip: ",type(plaka))
       arayuz(plaka)
    except:
       pass
           
#########################################