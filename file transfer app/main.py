from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

# Initialize main window
root = Tk()
root.title("File Transfer")
root.geometry("450x600+500+200")
root.configure(bg="#e0f7fa")  # Soft light cyan background for a fresh look
root.resizable(False, False)

# Send File window
def Send():
    window = Toplevel(root)
    window.title("Send File")
    window.geometry("450x600+500+200")
    window.configure(bg="#e0f7fa")
    window.resizable(False, False)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File",
                                              filetype=(("Text Files", "*.txt"), ("Python Files", "*.py"), ("All Files", "*.*")))

    def sender():
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print("Waiting for connection...")
        conn, addr = s.accept()
        file = open(filename, 'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print("File has been sent")

    image_icon1 = PhotoImage(file="send.png")
    window.iconphoto(False, image_icon1)

    # Centered sender ID display
    Mbackground = PhotoImage(file="id.png")
    Label(window, image=Mbackground, bg="#e0f7fa").place(x=150, y=250)

    host = socket.gethostname()
    Label(window, text=f'ID: {host}', bg="#e0f7fa", fg='#004d40', font=("Arial", 14, "bold")).place(x=180, y=300)

    Button(window, text="Select File", width=15, height=2, font=("Arial", 13), bg="#00796b", fg="white", 
           cursor="hand2", command=select_file, relief=RAISED, borderwidth=2).place(x=170, y=160)

    Button(window, text="SEND", width=10, height=2, font=("Arial", 13), bg="#0288d1", fg="white", 
           cursor="hand2", command=sender, relief=RAISED, borderwidth=2).place(x=290, y=160)

    window.mainloop()

# Receive File window
def Receive():
    main = Toplevel(root)
    main.title("Receive File")
    main.geometry("450x600+500+200")
    main.configure(bg="#e0f7fa")
    main.resizable(False, False)

    def receiver():
        ID = SenderID.get()
        filename1 = incoming_file.get()

        s = socket.socket()
        port = 8080
        s.connect((ID, port))
        file = open(filename1, 'wb')
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        messagebox.showinfo("Success", "File has been received")

    image_icon1 = PhotoImage(file="receive.png")
    main.iconphoto(False, image_icon1)

    Label(main, text="Receive File", font=("Arial", 22, "bold"), bg="#e0f7fa", fg="#004d40").place(x=150, y=30)

    Label(main, text="Input Sender ID", font=("Arial", 15), bg="#e0f7fa", fg="#004d40").place(x=30, y=120)
    SenderID = Entry(main, width=30, font=("Arial", 13), bg="#ffffff", fg="#004d40", borderwidth=2)
    SenderID.place(x=30, y=160)

    Label(main, text="Filename for Incoming File", font=("Arial", 15), bg="#e0f7fa", fg="#004d40").place(x=30, y=220)
    incoming_file = Entry(main, width=30, font=("Arial", 13), bg="#ffffff", fg="#004d40", borderwidth=2)
    incoming_file.place(x=30, y=260)

    imageicon = PhotoImage(file="arrow.png")
    rr = Button(main, text="Receive", compound=LEFT, image=imageicon, width=140, height=40, font=("Arial", 15), bg="#d32f2f", 
                fg="white", cursor="hand2", relief=RAISED, command=receiver, borderwidth=2)
    rr.place(x=150, y=330)

    main.mainloop()

# Main window setup
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

Label(root, text="File Transfer", bg="#e0f7fa", fg="#004d40", font=("Arial", 26, "bold")).place(x=130, y=30)
Frame(root, width=380, height=2, bg="#004d40").place(x=35, y=90)

# Send and Receive buttons
send_image = PhotoImage(file="send.png")
send = Button(root, image=send_image, bd=0, bg="#e0f7fa", activebackground="#e0f7fa", cursor="hand2", command=Send)
send.place(x=70, y=130)

receive_image = PhotoImage(file="receive.png")
receive = Button(root, image=receive_image, bd=0, bg="#e0f7fa", activebackground="#e0f7fa", cursor="hand2", command=Receive)
receive.place(x=290, y=130)

Label(root, text="Send File", font=("Arial", 17, "bold"), bg="#e0f7fa", fg="#004d40").place(x=80, y=250)
Label(root, text="Receive File", font=("Arial", 17, "bold"), bg="#e0f7fa", fg="#004d40").place(x=290, y=250)

# Background image
background = PhotoImage(file="background.png")
Label(root, image=background, bg="#e0f7fa").place(x=-2, y=370)

root.mainloop()



