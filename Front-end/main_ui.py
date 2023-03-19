import tkinter as tk            
from tkinter import Message, PhotoImage, Toplevel, font as tkfont
from tkinter import ttk
import time
from datetime import datetime


import read_log_file as log
import detect_face as df
import request_response as req # use jumboplus wifi only
import confirm # use jumboplus wifi only
import btn_pi as btn
import clear_file as cf

class myApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Face project")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth()-4, self.winfo_screenheight()-4))
        # self.state('zoomed')
        self.attributes('-zoomed', True)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Main, ConfirmPage, Result_pin):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Main")


    def show_frame(self, page_name):
        
        '''Show a frame for the given page name'''

        if page_name == "ConfirmPage" :
            print("switched!!")
            self.after(0,self.frames['ConfirmPage'].restore)
            
            
            # case password key pressed.
            self.after(500,self.frames['ConfirmPage'].key_check)

            


        if page_name == "Main" :
            print("switched!!")
            self.after(0,self.frames['Main'].restore)
            self.after(800,self.frames['Main'].detect)
        
        
        if page_name == "Result_pin" :
            self.after(100,self.frames['Result_pin'].fetch)
            self.after(1200,self.frames['Result_pin'].go_to_main)
            print("switched!!")

            
        
        frame = self.frames[page_name]
        frame.tkraise()


# ---------------------------------------------------------------------------------------------------------
    
class Main(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Face image", font=controller.title_font)
        label.grid(row=0,column=0,columnspan=3,pady=5)


# part img
        self.parent = parent
        img = PhotoImage(file='pic/bg.png')
        self.label = ttk.Label(self)
        self.label['image'] = img
        img.image = img
        self.label.grid(row=1,column=0,columnspan=3)

    # result
        self.result = tk.Label(self, text= "< Prediction result >")
        self.result.config(font = ("Courier", 18))
        self.result.grid(row=2,column=0,columnspan=3)

        name = "Unknown"
        self.Name = tk.Label(self, text = name )
        self.Name.config(font = ("Courier", 15))
        self.Name.grid(row=3,column=0,columnspan=3)
        
        predict = "Unknown"
        self.Predict = tk.Label(self, text = predict )
        self.Predict.config(font = ("Courier", 15))
        self.Predict.grid(row=4,column=0,columnspan=3)

    # part perdiction
        self.result = tk.Label(self, text= "<- Prediction ranking ->")
        self.result.config(font = ("Courier", 18))
        self.result.grid(row=5,column=0,columnspan=3)

    # col 1 
        rname1 = "Unknown"
        self.RName1 = tk.Label(self, text = rname1 )
        self.RName1.config(font = ("Courier", 15))
        self.RName1.grid(row=6,column=0,)
        
        rp1 = "Unknown"
        self.RP1 = tk.Label(self, text = rp1 )
        self.RP1.config(font = ("Courier", 15))
        self.RP1.grid(row=7,column=0)
    # col 2
        rname2 = "Unknown"
        self.RName2 = tk.Label(self, text = rname2 )
        self.RName2.config(font = ("Courier", 15))
        self.RName2.grid(row=6,column=1)
        
        rp2 = "Unknown"
        self.RP2 = tk.Label(self, text = rp2 )
        self.RP2.config(font = ("Courier", 15))
        self.RP2.grid(row=7,column=1)
    # col 3
        rname3 = "Unknown"
        self.RName3 = tk.Label(self, text = rname3 )
        self.RName3.config(font = ("Courier", 15))
        self.RName3.grid(row=6,column=2)
        
        rp3 = "Unknown"
        self.RP3 = tk.Label(self, text = rp3 )
        self.RP3.config(font = ("Courier", 15))
        self.RP3.grid(row=7,column=2)
        
        
        
        
# part time stamp
        self.result_t = tk.Label(self, text= "< Last time prediction >")
        self.result_t.config(font = ("Courier", 18))
        self.result_t.grid(row=8,column=0,columnspan=3)
        
        date = "Unknown"
        self.Date = tk.Label(self, text = date )
        self.Date.config(font = ("Courier", 15))
        
        time_s = "Unknown"
        self.Time_d = tk.Label(self, text = time_s )
        self.Time_d.config(font = ("Courier", 15))
        
        self.Date.grid(row=9,column=0,columnspan=3)
        self.Time_d.grid(row=10,column=0,columnspan=3)
        
# part status program
        self.con1 = tk.Label(self, text= "Status : waiting for face detect...... ")
        self.con1.config(font = ("Courier", 17))
        self.con1.grid(row=11,column=0,columnspan=3)

# part print word confrim
        self.con = tk.Label(self, text= "Please comfirm prediction result in 2 minutes. ")
        self.con.config(font = ("Courier", 17))
        self.con.grid(row=12,column=0,columnspan=3)
# for debug
        # button1 = tk.Button(self, text="Go to confirm page",command=lambda: controller.show_frame("ConfirmPage"))
        # button1.pack(pady=10)

# for fill picture in frame 
    
        for x in range(3):
            tk.Grid.columnconfigure(self, x, weight=1)

        for y in range(13):
            tk.Grid.rowconfigure(self, y, weight=1)
        
        
    def restore(self):
        img = PhotoImage(file='pic/bg.png')
        self.label['image'] = img
        img.image = img
        
        self.con1['text'] = "Status : waiting for face detect...... "
        
        self.RName1['text'] = "Unknown"
        self.RName2['text'] = "Unknown"
        self.RName3['text'] = "Unknown"
        
        self.RP1['text'] = "Unknown"
        self.RP2['text'] = "Unknown"
        self.RP3['text'] = "Unknown"
        
        self.Name['text'] = "Unknown"
        self.Predict['text'] = "Unknown"
        # self.Date['text'] = "Unknow"
        # self.Time_d['text'] = "Unknow"
    

    def detect(self):
        
        fileName =  df.find_face()
        start = time.perf_counter() #-----------------------
        self.con1['text'] = "Status : Waiting for send image......"
        start_send = time.time()
        flag2 = req.sendImg("pic/"+fileName[2]) # use jumboplus wifi only
        end_send = time.time()
        print("Sending Time:",end_send-start_send)
        path = "pic/"+ fileName[2]
        self.fetch_data(path)
        end = time.perf_counter() #-----------------------
        ptime = int((end - start) * 10**3) 
        log.write_time(ptime,fileName[2])
        cf.clean(fileName)
        self.con1['text'] = "Status : waiting for button confirm......"
        self.after(500,self.wait_btn)


    def fetch_data(self,path):
        img = PhotoImage(file=path)
        self.label['image'] = img
        img.image = img

        lastest = log.refesh_result()

        label_Name = lastest['Name']
        label_Percent = lastest['Percent']
        label_Date_Time = lastest['Time']

        arr_name = log.getName(label_Name)
        arr_percent = log.getResultPrecent(label_Percent)
        date = log.getDate(label_Date_Time)
        time_s = log.getTime(label_Date_Time)

        result_name,result_percent = log.most_3_people(lastest)

        rname1 = result_name[0]
        rname2 = result_name[1]
        rname3 = result_name[2]
        rp1 = result_percent[0]
        rp2 = result_percent[1]
        rp3 = result_percent[2]

        self.RName1['text'] = rname1
        self.RName2['text'] = rname2
        self.RName3['text'] = rname3
        
        self.RP1['text'] = str(rp1) + " %"
        self.RP2['text'] = str(rp2) + " %"
        self.RP3['text'] = str(rp3) + " %"
        
        p_result = label_Percent.index(max(label_Percent))

        global name
        global prediction
        name, prediction = log.find_most_acc(arr_name, arr_percent, p_result)
        label_result = prediction,"%"
            
        self.Name['text'] = name
        self.Date['text'] = date
        self.Time_d['text'] = str(time_s) + " น."
        
        if prediction == 0:
            self.Predict['text'] = "Unknown"
        else :
            self.Predict['text'] = label_result
        
        self.update()
        
    def wait_btn(self):
        global name
        global prediction
        if prediction >= 80 :
            flag_wait = btn.btn()
            if flag_wait == 0 :
                print("True")
                confirm.YES(name) # use jumboplus wifi only
                self.after(100,lambda: self.controller.show_frame("Main"))
            elif flag_wait == 1 :
                print("False")
                self.after(0,lambda: self.controller.show_frame("ConfirmPage"))
            elif flag_wait == 2 : # case idle 2 min.
                print("2 minutes.")
                self.after(0, confirm.Nothing()) # use jumboplus wifi only
                self.after(1000,lambda: self.controller.show_frame("Main"))
            else :
                print("Debug case.")
        else :
            print("Unknown")
            self.after(3000,lambda: self.controller.show_frame("ConfirmPage"))
            
# ------------------------------------------------------------------------------------------------------------------------

class ConfirmPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Confirm", font=controller.title_font)
        label.grid(row=0,column=0,columnspan=6,pady=15)
        
        self.des = tk.Label(self, text =  "Please comfirm code of")
        self.des.config(font = ("Courier", 15))
        self.des.grid(row=1,column=0,columnspan=6,pady=5)
        
        # --------------------------------------------------------
        name_f = ""
        predict_f = ""
        
        self.Name_f = tk.Label(self, text =  name_f)
        self.Name_f.config(font = ("Courier", 15))
        self.Name_f.grid(row=2,column=0,columnspan=6)
        
        self.Predict_f = tk.Label(self, text =  predict_f)
        self.Predict_f.config(font = ("Courier", 15))
        self.Predict_f.grid(row=3,column=0,columnspan=6)
        # --------------------------------------------------------
# part password code 6 digits

        img1 = PhotoImage(file='pic/lock.png')
        self.label1 = ttk.Label(self)
        self.label1['image'] = img1
        img1.image = img1
        self.label1.grid(row=4,column=0,padx=10,pady=300)
        
        img2 = PhotoImage(file='pic/lock.png')
        self.label2 = ttk.Label(self)
        self.label2['image'] = img2
        img2.image = img2
        self.label2.grid(row=4,column=1,padx=10,pady=300)
   
        img3 = PhotoImage(file='pic/lock.png')
        self.label3 = ttk.Label(self)
        self.label3['image'] = img3
        img3.image = img3
        self.label3.grid(row=4,column=2,padx=10,pady=300)
        
        img4 = PhotoImage(file='pic/lock.png')
        self.label4 = ttk.Label(self)
        self.label4['image'] = img4
        img4.image = img4
        self.label4.grid(row=4,column=3,padx=10,pady=300)
       
        img5 = PhotoImage(file='pic/lock.png')
        self.label5 = ttk.Label(self)
        self.label5['image'] = img5
        img5.image = img5
        self.label5.grid(row=4,column=4,padx=10,pady=300)
        
        img6 = PhotoImage(file='pic/lock.png')
        self.label6 = ttk.Label(self)
        self.label6['image'] = img6
        img6.image = img6
        self.label6.grid(row=4,column=5,padx=10,pady=300)
        
        self.con1 = tk.Label(self, text= "reset password press '*'. ")
        self.con1.config(font = ("Courier", 13))
        self.con1.grid(row=5,column=0,columnspan=6,pady=20)
        
        self.con2 = tk.Label(self, text= "cancel press '#' ")
        self.con2.config(font = ("Courier", 13))
        self.con2.grid(row=6,column=0,columnspan=6,pady=20)
        
# for debug
        # button1 = tk.Button(self, text="Go to confirm page",command=lambda: controller.show_frame("Main"))
        # button1.grid(row=2,column=0,columnspan=6,pady=10)
        

# for fill picture in frame 
    
        for x in range(6):
            tk.Grid.columnconfigure(self, x, weight=1)

        for y in range(4):
            tk.Grid.rowconfigure(self, y, weight=1)
            
    
    def restore(self):
        img = PhotoImage(file="pic/lock.png")
        self.label1['image'] = img
        img.image = img
        
        self.label2['image'] = img
        img.image = img
        
        self.label3['image'] = img
        img.image = img
        
        self.label4['image'] = img
        img.image = img
        
        self.label5['image'] = img
        img.image = img
        
        self.label6['image'] = img
        img.image = img
        
        logFile = log.refesh_result()
        
        result_name_f,result_percent_f = log.most_3_people(logFile)
        
        predict = result_percent_f[0],"%"
        
        print("log confirm : ",result_name_f[0])
        print("log confirm : ",predict)
        
        self.Predict_f['text'] = predict
        self.Name_f['text'] = result_name_f[0]
        
     
     
    def key_check(self):
        img = PhotoImage(file="pic/unlock.png")
        code = ""
        start = datetime.now()
        flag_goto = False
        while len(code) < 6 :
            digit = btn.matrix_keypad(start)
            print(digit)
            
            if str(digit) == 'time_out' or digit == "#": # case idle 1.30 min.
                print("time out!!")
                self.after(500,confirm.Nothing())    # use jumboplus wifi only
                flag_goto = True
                break
            else :
                if str(digit) == "*" :
                    code = ""
                    self.after(0,self.restore)
                    self.update()
                    continue
                else :
                    code = code + str(digit)
                    
                if len(code) == 6 :
                    send = int(code)
                    confirm.NO(send) # use jumboplus wifi only
                    #self.after(0,self.msg_complete)
                else :
                    print("code :",code)
                    print("len code :",len(code))
                    ff = len(code)
                    
                    if ff == 1 :
                        self.label1['image'] = img
                        img.image = img
                    elif ff == 2 :  
                        self.label2['image'] = img
                        img.image = img
                    elif ff == 3 :
                        self.label3['image'] = img
                        img.image = img
                    elif ff == 4 : 
                        self.label4['image'] = img
                        img.image = img
                    elif ff == 5 :
                        self.label5['image'] = img
                        img.image = img
                    elif ff == 6 :
                        self.label6['image'] = img
                        img.image = img
                    else : print("Debug !!")
                    
            self.update()
                
            time.sleep(0.2)
            
        if flag_goto:
            self.after(500,lambda: self.controller.show_frame("Main"))
        else :
            self.after(500,lambda: self.controller.show_frame("Result_pin"))
    
    
    def msg_complete(self):
        top = Toplevel()
        top.title('complete')
        Message(top, text="Code send complete.",padx=80,pady=40).pack()
        top.after(2000, top.destroy)
        
        
        
class Result_pin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # label = tk.Label(self, text="Confirm", font=controller.title_font)
        # label.grid(row=0,column=0,pady=15)
        img = PhotoImage(file='pic/check.png')
        self.label1 = ttk.Label(self)
        self.label1['image'] = img
        img.image = img
        self.label1.grid(row=0,column=0,padx=10)
        
        self.des = tk.Label(self, text =  "PIN status")
        self.des.config(font = ("Courier", 30))
        self.des.grid(row=1,column=0,pady=5)
        # for fill picture in frame 
    
        for x in range(1):
            tk.Grid.columnconfigure(self, x, weight=1)

        for y in range(2):
            tk.Grid.rowconfigure(self, y, weight=1)
            
    
    def fetch(self):
        status = log.refresh_pin_status()
        if status :
            img = PhotoImage(file="pic/check.png")
            self.label1['image'] = img
            img.image = img
            self.des['text'] = "Your PIN is correct."
        else :
            img = PhotoImage(file="pic/uncheck.png")
            self.label1['image'] = img
            img.image = img
            self.des['text'] = "Your PIN is incorrect."
        self.update()
    
    def go_to_main(self):
        self.after(2000,lambda: self.controller.show_frame("Main"))
        

         


if __name__ == "__main__":
    app = myApp()
    app.mainloop()