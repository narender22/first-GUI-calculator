import json
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog


# BLL
class Customer:
    listCus = []

    def __init__(self):
        self.id = 0
        self.name = ""
        self.age = 0
        self.mob = ""

    @staticmethod
    def convToDict(ob):
        return ob.__dict__

    @staticmethod
    def contoObj(d):
        ob = Customer()
        ob.id = d["id"]
        ob.age = d["age"]
        ob.name = d["name"]
        ob.mob = d["mob"]
        return ob

    @staticmethod
    def saveCustomerinFile():
        global file
        try:
            fs = open(file, "w")
            json.dump(Customer.listCus, fs, default=Customer.convToDict)
            fs.close()
        except:
            tkinter.messagebox.showinfo("Alert", "Incorrect file selected")

    @staticmethod
    def loadCustomerfromFile():
        global file
        try:
            fs = open(file, "r")
            Customer.listCus = json.load(fs, object_hook=Customer.contoObj)
            fs.close()
        except:
            tkinter.messagebox.showinfo("Alert", "Incorrect file selected")

    def addCustomer(self):
        Customer.listCus.append(self)
        varID.set("")
        varAge.set("")
        varName.set("")
        varMob.set("")

    def searchCustomer(self, id):
        for i in range(len(Customer.listCus)):
            if id == Customer.listCus[i].id:
                self.name = Customer.listCus[i].name
                self.age = Customer.listCus[i].age
                self.mob = Customer.listCus[i].mob
                return 1
            return 0

    def modifyCustomer(self, id):
        for i in range(len(Customer.listCus)):
            if self.id == Customer.listCus[i].id:
                Customer.listCus[i] = self
                return 1
        return 0

    def deleteCustomer(self, id):
        for i in range(len(Customer.listCus)):
            if id == Customer.listCus[i].id:
                Customer.listCus.pop(i)
                return 1
        return 0

    @staticmethod
    def showAllCustomer():
        top = tkinter.Tk()
        top.title("SHOW-DATA")
        top.minsize(200, 200)

        tkinter.Label(top, text="ID", width=12, bg="skyblue", font=16).grid(row=0, column=0)
        tkinter.Label(top, text="Name", width=12, bg="light green", font=16).grid(row=0, column=1)
        tkinter.Label(top, text="Age", width=12, bg="grey", font=16).grid(row=0, column=2)
        tkinter.Label(top, text="Mobile", width=12, bg="pink", font=16).grid(row=0, column=3)

        for i in range(len(Customer.listCus)):
            for k in range(4):
                if k == 0:
                    lblvalueid = tkinter.Label(top, text=Customer.listCus[i].id, width=12, font=12)
                    lblvalueid.grid(row=i + 1, column=k)
                elif k == 1:
                    lblvaluename = tkinter.Label(top, text=Customer.listCus[i].name, width=12, font=12)
                    lblvaluename.grid(row=i + 1, column=k)
                elif k == 2:
                    lblvalueage = tkinter.Label(top, text=Customer.listCus[i].age, width=12, font=12)
                    lblvalueage.grid(row=i + 1, column=k)
                elif k == 3:
                    lblvaluemob = tkinter.Label(top, text=Customer.listCus[i].mob, width=12, font=12)
                    lblvaluemob.grid(row=i + 1, column=k)
        top.mainloop()


# PL
def btnadd_click():
    cus = Customer()
    cus.id = txtId.get()
    cus.name = txtName.get()
    cus.age = txtAge.get()
    cus.mob = txtMob.get()
    cus.addCustomer()
    mes = len(Customer.listCus), "Customer Added Successfully"
    tkinter.messagebox.showinfo("Added", mes)


def btndelete_click():
    id = txtId.get()
    cus = Customer()
    flag = cus.deleteCustomer(id)
    if flag == 1:
        tkinter.messagebox.showinfo("Success", "Customer deleted successfully")
    else:
        tkinter.messagebox.showinfo("Failed", "Customer with given ID not found")


def btnsearch_click():
    id = txtId.get()
    cus = Customer()
    flag = cus.searchCustomer(id)
    if flag == 1:
        varName.set(cus.name)
        varAge.set(cus.age)
        varMob.set(cus.mob)
    else:
        tkinter.messagebox.showinfo("failed", "Customer with given ID not found")


def btnmodify_click():
    cus = Customer()
    cus.id = txtId.get()
    cus.name = txtName.get()
    cus.age = txtAge.get()
    cus.mob = txtMob.get()
    flag = cus.modifyCustomer(cus.id)
    if flag == 1:
        tkinter.messagebox.showinfo("Success", "Customer modified successfully")
    else:
        tkinter.messagebox.showinfo("Faiaed", "Customer with given ID not found")


def showcustomerbyindex(i):
    varID.set(Customer.listCus[i].id)
    varName.set(Customer.listCus[i].name)
    varAge.set(Customer.listCus[i].age)
    varMob.set(Customer.listCus[i].mob)


index = 0
file = ""


def btnfirst_click():
    global index
    index = 0
    showcustomerbyindex(index)


def btnprev_click():
    global index
    if index > 0:
        index = index - 1
    showcustomerbyindex(index)


def btnnext_click():
    global index
    if index < len(Customer.listCus) - 1:
        index = index + 1
    showcustomerbyindex(index)


def btnlast_click():
    global index
    index = len(Customer.listCus) - 1
    showcustomerbyindex(index)


def btnload_click():
    Customer.loadCustomerfromFile()
    tkinter.messagebox.showinfo("Success", "Customer Loaded Successfully")


def btnsave_click():
    Customer.saveCustomerinFile()
    tkinter.messagebox.showinfo("Success", "Customer Saved Successfully")


def btnshowall_click():
    Customer.showAllCustomer()


def btnselectfile_click():
    global file
    root.filename = filedialog.askopenfilename(initialdir="C://", title="Select a file",
                                               filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    file = root.filename


root = tkinter.Tk()
root.title("CMS")
# start creating labels
lblId = tkinter.Label(root, text="ID", width=12, height=2, font=16)
lblId.grid(row=0, column=0, columnspan=2)

lblName = tkinter.Label(root, text="Name", width=12, height=2, font=16)
lblName.grid(row=1, column=0, columnspan=2)

lblAge = tkinter.Label(root, text="Age", width=12, height=2, font=16)
lblAge.grid(row=2, column=0, columnspan=2)

lblMob = tkinter.Label(root, text="Mobile No.", width=12, height=2, font=16)
lblMob.grid(row=3, column=0, columnspan=2)

varID = tkinter.IntVar()
txtId = tkinter.Entry(root, text="ID", width=12, textvariable=varID, font=16)
txtId.grid(row=0, column=2, columnspan=2)

varName = tkinter.StringVar()
txtName = tkinter.Entry(root, text="Name", width=12, textvariable=varName, font=16)
txtName.grid(row=1, column=2, columnspan=2)

varAge = tkinter.IntVar()
txtAge = tkinter.Entry(root, text="Age", width=12, textvariable=varAge, font=16)
txtAge.grid(row=2, column=2, columnspan=2)

varMob = tkinter.StringVar()
txtMob = tkinter.Entry(root, text="Mobile No.", textvariable=varMob, font=16)
txtMob.grid(row=3, column=2, columnspan=2)
# start creating buttons
btnAdd = tkinter.Button(root, text="Add", width=10, height=2, font=16, command=btnadd_click)
btnAdd.grid(row=4, column=0)

btnSearch = tkinter.Button(root, text="Search", width=10, height=2, font=16, command=btnsearch_click)
btnSearch.grid(row=4, column=1)

btnDelete = tkinter.Button(root, text="Delete", width=10, height=2, font=16, command=btndelete_click)
btnDelete.grid(row=4, column=2)

btnModify = tkinter.Button(root, text="Modify", width=10, height=2, font=16, command=btnmodify_click)
btnModify.grid(row=4, column=3)

btnFirst = tkinter.Button(root, text="First", width=10, height=2, font=16, command=btnfirst_click)
btnFirst.grid(row=5, column=0)

btnPrev = tkinter.Button(root, text="Previous", width=10, height=2, font=16, command=btnprev_click)
btnPrev.grid(row=5, column=1)

btnNext = tkinter.Button(root, text="Next", width=10, height=2, font=16, command=btnnext_click)
btnNext.grid(row=5, column=2)

btnLast = tkinter.Button(root, text="Last", width=10, height=2, font=16, command=btnlast_click)
btnLast.grid(row=5, column=3)

btnLoad = tkinter.Button(root, text="Load", width=15, height=2, font=16, command=btnload_click)
btnLoad.grid(row=6, column=0, columnspan=2)

btnSave = tkinter.Button(root, text="Save", width=15, height=2, font=16, command=btnsave_click)
btnSave.grid(row=6, column=2, columnspan=2)

btnSelectFile = tkinter.Button(root, text="Select File", width=15, height=2, font=16, command=btnselectfile_click)
btnSelectFile.grid(row=7, column=0, columnspan=2)

btnShowall = tkinter.Button(root, text="Show all", width=15, height=2, font=16, command=btnshowall_click)
btnShowall.grid(row=7, column=2, columnspan=2)
root.mainloop()
