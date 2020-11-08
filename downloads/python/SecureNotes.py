# Importing modules

from tkinter import *  # Window Management
import os  # Creating and accesing folders

# On StackOverflow
try:
    # Python 3
    from tkinter import messagebox
except:
    # Python 2
    import tkMessageBox as messagebox

homescreen = Tk()  # Make the main window


def ChangeHomeRes():
    ChangeResMenu = Tk()

    # ------Change resolution functions

    def changResTo1366x768():
        homescreen.geometry("1366x768")
        ChangeResMenu.destroy()

    def changResTo1920x1080():
        homescreen.geometry("1920x1080")
        ChangeResMenu.destroy()

    def changResTo2560x1440():
        homescreen.geometry("2560x1440")
        ChangeResMenu.destroy()

    ChangeResMenu.configure(background="white")

    # Buttons to change resolutions

    Button(ChangeResMenu, text="1366x768", command=changResTo1366x768).pack()
    Button(ChangeResMenu, text="1920x1080", command=changResTo1920x1080).pack()
    Button(ChangeResMenu, text="2560x1440", command=changResTo2560x1440).pack()

    ChangeHomeRes.mainloop()


def ExitApp():  # Function for the End session button
    exit()


# Login to user account
def LogIn():
    def LogInCheck():

        # Get the input from the user
        FIleLoginUsername = LoginUsername.get()
        FileLoginPassword = LoginPassword.get()

        # getting all the valid accounts
        profiles = os.listdir()

        # checking if the profile exists and is valid
        if FIleLoginUsername in profiles:  # Checking if the profile name is in the directory

            # changing the directory in OS module to the account folder
            Directory = "D:/Python scripts/SecureNotes/" + FIleLoginUsername + "/"

            # Checking the password---------

            with open(Directory + "Password", "r") as PasswordFile:  # Opening the password folder
                correctPassword = PasswordFile.read()  # reading the contents of the file to get the password

                if correctPassword == FileLoginPassword:  # Checking if the password that was typed in matches the
                    # real password in the file

                    SignedInUsername = FIleLoginUsername
                    # Destroying the windows
                    Login.destroy()
                    homescreen.destroy()

                    def Reload():  # Make a reload functions so when a new file is created, you can reload the file list to see the new file
                        homescreen2 = Tk()  # Make the new window as a signed in person

                        def NewNote():  # Create a new note
                            NewNoteName = Tk()  # New Note Name window creation

                            def NewNoteNext():  # Function when the person press the next button

                                notename = NoteName.get()  # Get the name that the person typed in
                                NewNoteName.destroy()  # Destroy the title window to prevent bugs

                                Note = Tk()  # Make the note window

                                def SaveNote():  # Function to save the note

                                    # Get the text taht is in the note
                                    note = Note2.get("0.0", END)  # Title
                                    title = Title.get("0.0", END)  # Note body

                                    fixedtitle = title.replace("\n",
                                                               "")  # at the end of a title, Tkinter puts a \m so we have to remove it

                                    # Temp test code----
                                    if title in Directory + "Notes":
                                        print("thererrererererer")
                                        messagebox.showwarning("File already there",
                                                               "A file named " + title + " already exists, saving this document will override this document, are you sure you want to proceed?")

                                    else:
                                        print("NO")
                                    # End of stupid temp code

                                    # Create the file
                                    with open(Directory + "Notes/" + fixedtitle,
                                              "w") as SaveFile:  # The note file will be called the name of the title
                                        SaveFile.write(note)  # Writing the note body

                                # Exit code function
                                def Exit():
                                    Note.destroy()  # Simply destroys the window

                                # ------Making the note window
                                Note.configure(background="white")  # Background color
                                Note.title(notename + " - SecureNotes v0.0.1")  # Change title fromm tk

                                Button(Note, text="Save", command=SaveNote).grid(row=0, column=0,
                                                                                 sticky=W)  # Make the buttons for the save
                                Button(Note, text="Exit", command=Exit).grid(row=0, column=0,
                                                                             sticky=E)  # Make the buttons for the exit

                                Title = Text(Note, width=50, height=1, wrap=WORD)  # Define the gadget for the title
                                Title.grid(row=1, column=0, sticky=W)  # Place the title gadget

                                Title.insert(END,
                                             notename)  # Insert the title that was typed in from the title name prompt

                                Note2 = Text(Note, width=50, height=10,
                                             wrap=WORD)  # Define the gadget for the note text
                                Note2.grid(row=2, column=0, sticky=W)  # Place the note gadget

                                Note.mainloop()  # end of the window

                            # -------Set note name GUI
                            NewNoteName.configure(background="white")  # set window color to white
                            NewNoteName.title("New Note")  # Set the title

                            Label(NewNoteName, text="Enter a name for your note:", bg="white").grid(row=0, column=0,
                                                                                                    sticky=W)  # Label at the top

                            NoteName = Entry(NewNoteName, width=50)  # Define the text title entry
                            NoteName.grid(row=1, column=0, sticky=W)  # Place the text entry

                            Button(NewNoteName, text="Next", command=NewNoteNext).grid(row=2, column=0)  # The OK button

                            NewNoteName.mainloop()  # End of the NewNoteName

                        # Making new folders is still in progress
                        def NewFolder():
                            pass

                        # This is the file Manager for when you signed in
                        homescreen2.configure(background="white")  # Configure background to white
                        homescreen2.title("SecureNotes v0.0.1")  # Set title to SecureNotes v0.0.1
                        homescreen2.geometry("1366x768")  # Set window size

                        Label(homescreen2, text="SecureNotes ALPHA", bg="white").grid(row=0,
                                                                                      column=0)  # Write title for the program

                        Button(homescreen2, text="End session", command=ExitApp).grid(row=1, column=1,
                                                                                      sticky=W)  # Make the end session button

                        Label(homescreen2, text="\n", bg="white", fg="white").grid(row=2,
                                                                                   column=0)  # Make a invisible line break Label to add space between the buttons

                        # Adding the actions button
                        Button(homescreen2, text="New Note", command=NewNote).grid(row=3, column=0,
                                                                                   sticky=W)  # Make the New Note button
                        Button(homescreen2, text="New Folder", command=NewFolder).grid(row=3, column=1,
                                                                                       sticky=W)  # Make the New Folder button

                        # Defining the function when you open a file
                        def OpenFile():
                            filetoopen = FileToOpen.get()  # Get what the name of the file that he typed in

                            os.chdir(Directory + "Notes/")  # Canged the directory to the notes folder
                            filesindir = os.listdir()  # Set a variable for all the notes in the notes folder

                            if filetoopen in filesindir:  # Checking if the typed in title of the note is in the

                                with open(Directory + "Notes/" + filetoopen, "r") as file1:  # Opening the file

                                    ImportFile = file1.read()  # Reading the contents of the file (file contains the note)
                                    notename = filetoopen  # Set the name of the note to the name of the note

                                    # -------Make the same gui as before, it is the same so I won't comment it
                                    def SaveNote():
                                        Note3 = Note2.get("0.0", END)
                                        title = Title.get("0.0", END)

                                        fixedtitle2 = title.replace("\n", "")

                                        with open(Directory + "Notes/" + fixedtitle2, "w") as SaveFile:
                                            SaveFile.write(Note3)

                                    def Exit():
                                        Note.destroy()

                                    Note = Tk()

                                    Note.configure(background="white")
                                    Note.title(notename + " - SecureNotes v0.0.1")

                                    Button(Note, text="Save", command=SaveNote).grid(row=0, column=0, sticky=W)
                                    Button(Note, text="Exit", command=Exit).grid(row=0, column=0, sticky=E)

                                    Title = Text(Note, width=50, height=1, wrap=WORD)
                                    Title.grid(row=1, column=0, sticky=W)

                                    Title.delete(0.0, END)
                                    Title.insert(END, notename)

                                    Note2 = Text(Note, width=50, height=10, wrap=WORD)
                                    Note2.grid(row=2, column=0, sticky=W)

                                    # The next 2 lines will add the contents of the file to the Text box
                                    Note2.delete(0.0, END)  # Delets all the items in the Text Box (Just in case)
                                    Note2.insert(END, ImportFile)  # Add the note

                                    Note.mainloop()  # End the window


                            else:

                                # if it cant find the file, it says an error
                                messagebox.showerror("Can't open file", "This file dosent exist!")

                        # Desplaying the notes
                        os.chdir(Directory + "Notes/")  # Set the directory to the notes folder
                        columnCount = 4  # Make variables as a place to set the label
                        filesInDir = os.listdir()  # Put the files as a list in the variable
                        filecount = 0  # I dont know why I did this

                        for i in filesInDir:
                            filetodo = filesInDir[filecount]

                            Label(homescreen2, text=filetodo, bg="white").grid(row=columnCount, column=0, sticky=W)

                            filecount = filecount + 1
                            columnCount = columnCount + 1

                        FileToOpen = Entry(homescreen2, width=50)
                        FileToOpen.grid(row=columnCount, column=0, sticky=E)

                        def Reload2():
                            homescreen2.destroy()
                            Reload()

                        def OpenMail():
                            mail = Tk()

                            def ComposeMail():

                                def SendMail():

                                    mailto = MailTo.get()
                                    mailtitle = MailTitle.get()
                                    mailnote = MailNote.get()
                                    mailbody = MailBody.get(0.0, END)

                                    os.chdir(Directory + "Notes/")

                                    if mailnote in os.listdir():
                                        with open(Directory + "Notes/" + mailnote, "r") as NotesToSend:
                                            notetosend = NotesToSend.read()

                                        MailNoteToSend = notetosend

                                        fixedmailto = mailto.replace("\n", "")
                                        print(fixedmailto)

                                        mailbody2 = "From: " + SignedInUsername + "\nSent Notes:\n---------------\n" + notetosend + "\n---------------\n" + mailbody

                                        os.chdir("D:/Python scripts/SecureNotes/")

                                        if fixedmailto in os.listdir():
                                            with open(
                                                    "D:/Python scripts/SecureNotes/" + fixedmailto + "/Mail/" + mailtitle,
                                                    "w") as MailFile:
                                                MailFile.write(mailbody2)

                                            with open(
                                                    "D:/Python scripts/SecureNotes/" + fixedmailto + "/Notifications/" + mailtitle,
                                                    "w") as Notifyfile:
                                                Notifyfile.write(mailbody2)

                                            composemail.destroy()
                                            mail.destroy()

                                            messagebox.showinfo("Message sent",
                                                                "Your message has been successfully sent to " + fixedmailto + "!")


                                        else:
                                            try:
                                                MailSendError.destroy()
                                            except:
                                                pass
                                            MailSendError = Label(composemail, text="Unknown Person!", bg="Yellow",
                                                                  fg="black")
                                            MailSendError.grid(row=8, column=0)



                                    elif mailtitle == "":
                                        fixedmailto = mailto.replace("\n", "")
                                        print(fixedmailto)

                                        mailbody2 = "From" + SignedInUsername + "\n" + mailbody

                                        os.chdir("D:/Python scripts/SecureNotes/")

                                        if fixedmailto in os.listdir():
                                            with open(
                                                    "D:/Python scripts/SecureNotes/" + fixedmailto + "/Mail/" + mailtitle,
                                                    "w") as MailFile:
                                                MailFile.write(mailbody2)

                                            with open(
                                                    "D:/Python scripts/SecureNotes/" + fixedmailto + "/Notifications/" + mailtitle,
                                                    "w") as Notifyfile:
                                                Notifyfile.write(mailbody2)

                                            composemail.destroy()
                                            mail.destroy()

                                            messagebox.showinfo("Message sent",
                                                                "Your message has been successfully sent to " + fixedmailto + "!")
                                        else:

                                            try:
                                                MailSendError.destroy()
                                            except:
                                                pass
                                            MailSendError = Label(composemail, text="Unknown Person!", bg="Yellow",
                                                                  fg="black")
                                            MailSendError.grid(row=8, column=0)



                                    else:
                                        try:
                                            MailSendError.destroy()
                                        except:
                                            pass
                                        MailSendError = Label(composemail, text="Unknown note document", bg="Yellow",
                                                              fg="black")
                                        MailSendError.grid(row=8, column=0)

                                composemail = Tk()

                                composemail.configure(background="white")
                                composemail.title("Compose Mail - SecureNotes v0.0.1")

                                Label(composemail, text="To:", bg="white").grid(row=0, column=0, sticky=W)
                                MailTo = Entry(composemail, width=50)
                                MailTo.grid(row=1, column=0, sticky=W)

                                Label(composemail, text="Title:", bg="white").grid(row=2, column=0, sticky=W)
                                MailTitle = Entry(composemail, width=50)
                                MailTitle.grid(row=3, column=0, sticky=W)

                                Label(composemail, text="Note to send:", bg="white").grid(row=4, column=0, sticky=W)
                                MailNote = Entry(composemail, width=50)
                                MailNote.grid(row=5, column=0, sticky=W)

                                MailBody = Text(composemail, width=50, height=10, wrap=WORD)
                                MailBody.grid(row=6, column=0, sticky=W)

                                MailBody.delete(0.0, END)
                                MailBody.insert(END, "Your Message here")

                                Button(composemail, text="Send Mail", command=SendMail).grid(row=7, column=0)
                                composemail.mainloop()

                            mail.configure(background="white")
                            mail.title("Mail - SecureNotes v0.0.1")
                            mail.geometry("400x500")

                            def OpenTypedMail():

                                openpostedmail = OpenPostedMail.get()

                                if openpostedmail in os.listdir(Directory + "Mail/"):

                                    with open(Directory + "Mail/" + openpostedmail, "r") as MailFileToGet:
                                        ViewMailBody = MailFileToGet.read()

                                        MailContents = Tk()

                                        MailContents.configure(background="White")
                                        MailContents.title(openpostedmail + " - SecureNotes v0.0.1")

                                        Label(MailContents, text=openpostedmail, bg="White").grid(row=0, column=0)

                                        ViewMailBody2 = Text(MailContents, width=50, height=10, wrap=WORD)
                                        ViewMailBody2.grid(row=1, column=0)

                                        ViewMailBody2.delete(0.0, END)
                                        ViewMailBody2.insert(END, ViewMailBody)

                                        MailContents.mainloop()

                                else:
                                    MailErrorLable = Label(mail, text="Unknown mail subject", bg="Yellow")
                                    MailErrorLable.grid(row=(Position + 2), column=0)

                            Label(mail, text="Mail", bg="white").grid(row=0, column=0)

                            os.chdir(Directory + "Mail/")

                            ItemToPlace = os.listdir()
                            Position = 1

                            for j in os.listdir():

                                os.chdir(Directory + "Mail/")

                                if j in os.listdir():
                                    Label(mail, text=ItemToPlace[Position - 1], bg="yellow").grid(row=Position,
                                                                                                  column=0, sticky=W)
                                else:
                                    Label(mail, text=ItemToPlace[Position - 1], bg="white").grid(row=Position, column=0,
                                                                                                 sticky=W)

                                Position = Position + 1

                            Button(mail, text="Compose Mail", command=ComposeMail).grid(row=Position, column=0)

                            OpenPostedMail = Entry(mail, width=50, bg="White")
                            OpenPostedMail.grid(row=(Position + 1), column=0, sticky=W)

                            Button(mail, text="Open", command=OpenTypedMail).grid(row=(Position + 1), column=1)

                            mail.mainloop()

                        Button(homescreen2, text="Open FIle", command=OpenFile).grid(row=columnCount, column=1,
                                                                                     sticky=W)
                        Button(homescreen2, text="Refresh", command=Reload2).grid(row=1, column=0, sticky=W)

                        Button(homescreen2, text="Open Mail", command=OpenMail).grid(row=1, column=2)

                        homescreen2.mainloop()

                    Reload()

                else:

                    Label(Login, text="Invalid Username/Password!", bg="yellow").grid(row=5, column=1)
                    LoginPassword.delete(0, END)

        else:
            Label(Login, text="Invalid Username/Password!", bg="yellow").grid(row=5, column=1)
            LoginPassword.delete(0, END)

    Login = Tk()

    Login.configure(background="white")
    Login.title("Log in to your SecureNotes account")
    Login.geometry("600x400")

    Label(Login, text="Log in to your SecureNotes account")

    Label(Login, text="Username: ", bg="white").grid(row=1, column=0, sticky=W)
    LoginUsername = Entry(Login, width=50)
    LoginUsername.grid(row=1, column=1, sticky=W)

    Label(Login, text="", bg="white").grid(row=2, column=0)

    Label(Login, text="Password:  ", bg="white").grid(row=3, column=0, sticky=W)
    LoginPassword = Entry(Login, width=50)
    LoginPassword.grid(row=3, column=1, sticky=W)

    Button(Login, text="Log in", command=LogInCheck).grid(row=4, column=0, sticky=W)

    Login.mainloop()


def SignUp():
    def SignUpCheck():

        FileUsername = Username.get()
        Filepassword = Password.get()
        FIleCOnfirmPassword = ConfirmPassword.get()

        SigmUpWindow.destroy()

        if Filepassword != FIleCOnfirmPassword:

            messagebox.showerror("Invalid password", "Please make sure that your passwrods match!!!")

        else:
            try:
                os.mkdir(FileUsername)
                filename = "D:/Python scripts/SecureNotes/" + FileUsername + "/"
                os.chdir(FileUsername)

                with open(filename + "Password", "w") as userfile:
                    userfile.write(Filepassword)

                os.mkdir("Notes")
                os.mkdir("Notifications")
                os.mkdir("Mail")

                messagebox.showinfo("Account created!",
                                    "Your account has been sucessfully created, please restart the program to sign in to your account.")

            except FileExistsError:

                messagebox.showerror("Account taken", "Sorry, another person has already claimed this account username")

    SigmUpWindow = Tk()

    SigmUpWindow.configure(background="white")
    SigmUpWindow.title("Sign up for a SecureNotes account")
    SigmUpWindow.geometry("600x400")

    Label(SigmUpWindow, text="Sign up for a SecureNotes Account", bg="white").grid(row=0, column=0)

    Label(SigmUpWindow, text="Username: ", bg="white").grid(row=1, column=0, sticky=W)
    Username = Entry(SigmUpWindow, width=50)
    Username.grid(row=1, column=1, sticky=W)

    Label(SigmUpWindow, text="", bg="white").grid(row=2, column=0)

    Label(SigmUpWindow, text="Password:  ", bg="white").grid(row=3, column=0, sticky=W)
    Password = Entry(SigmUpWindow, width=50)
    Password.grid(row=3, column=1, sticky=W)

    Label(SigmUpWindow, text="ConfirmPassword", bg="white").grid(row=4, column=0, sticky=W)
    ConfirmPassword = Entry(SigmUpWindow, width=50)
    ConfirmPassword.grid(row=4, column=1, sticky=W)

    Button(SigmUpWindow, text="Create account", command=SignUpCheck).grid(row=5, column=0, sticky=W)

    SigmUpWindow.mainloop()


homescreen.configure(background="white")
homescreen.title("SecureNotes v0.0.1")
homescreen.geometry("1366x768")

Label(homescreen, text="SecureNotes ALPHA", bg="white").grid(row=0, column=0)

Button(homescreen, text="Change window resoluton", command=ChangeHomeRes).grid(row=1, column=0, sticky=W)
Button(homescreen, text="End session", command=ExitApp).grid(row=1, column=1, sticky=W)

Button(homescreen, text="Log in", command=LogIn).grid(row=2, column=0, sticky=W)
Button(homescreen, text="sign Up", command=SignUp, bg="blue", fg="white").grid(row=2, column=1, sticky=W)

homescreen.mainloop()
