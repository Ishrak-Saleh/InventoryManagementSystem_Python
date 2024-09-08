from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# from PIL import Image, ImageTk
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PythonProject2024",
    database="mydata"
)

print(mydb)

class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("PharmaVault")
        self.root.geometry("1366x768+0+0")
        #ADD_MED_VARIABLE_______________
        self.addMed_var = StringVar()
        self.refMed_var = StringVar()
        #MAIN_VARIABLE_______________
        self.ref_var = StringVar()
        self.company_var = StringVar()
        self.medType_var = StringVar()
        self.medName_var = StringVar()
        self.lotNumber_var = StringVar()
        self.issued_var = StringVar()
        self.expires_var = StringVar()
        self.uses_var = StringVar()
        self.sideEffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.quantity_var = StringVar()





        lblTitle = Label(self.root, text="PharmaVault", bg="#475054", fg="#FEFEF9", font=("Lexend", 20, "bold"), padx=0, pady=2)
        lblTitle.pack(side=TOP, fill=X)


        ##__________________________________DATA_FRAME__________________________________
        DataFrame = Frame(self.root, bd=5, bg="#475054", relief=RAISED, padx=20)
        DataFrame.place(x=0, y=50, width=1366, height=320)

        DataFrameLeft = LabelFrame(DataFrame, bd=5, bg="#475054",relief=RAISED, padx=20, text="Info: ", fg="#FEFEF9",font=("Lexend", 12, "bold"))
        DataFrameLeft.place(x=610, y=5, width=708, height=290)

        DataFrameRight = LabelFrame(DataFrame, bd=5, bg="#475054",relief=RAISED, padx=20, text="Department: ",fg="#FEFEF9",font=("Lexend", 12, "bold"))
        DataFrameRight.place(x=0, y=5, width=542, height=290)




        ##__________________________________BUTTON_FRAME__________________________________
        BtnFrame = Frame(self.root, bg="#475054", padx=20)
        BtnFrame.place(x=0, y=370, width=1366, height=43)
        ##__________________________________BUTTON_MAIN__________________________________
        btnAddData = Button(BtnFrame, command= self.add_Data,text="ADD", font=("Satoshi", 10, "bold"),
                            width=13, bg="#5EC9CC", fg="black")
        btnAddData.grid(row=0, column=0)
        btnUpdateData = Button(BtnFrame, command=self.Update, text="UPDATE", font=("Satoshi", 10, "bold"),
                               width=13,bg="#5EC9CC", fg="black")
        btnUpdateData.grid(row=0, column=1)
        btnDelData = Button(BtnFrame, command = self.Delete,text="DELETE", font=("Satoshi", 10, "bold"),
                            width=13, bg="#FD4E62", fg="black")
        btnDelData.grid(row=0, column=2)
        btnResetData = Button(BtnFrame, command= self.Reset,text="RESET", font=("Satoshi", 10, "bold"),
                              width=13, bg="#5EC9CC", fg="black")
        btnResetData.grid(row=0, column=3)





        ##__________________________________SEARCH_BY__________________________________
        lblSearch = Label(BtnFrame, text="SEARCH", font=("Lexend", 10, "bold"),
                          width=8, bg="#475054",fg="#FEFEF9")
        lblSearch.grid(row=0, column=5, sticky="e")
        #____VARIABLE____
        self.search_Var = StringVar()
        search_combo = ttk.Combobox(BtnFrame,textvariable=self.search_Var,
                                    width=18, font=("Satoshi", 10, "bold"), state="readonly")
        search_combo["values"] = ("REFERENCE", "MEDI_NAME")
        search_combo.grid(row=0, column=6, padx = 6)
        search_combo.current(0)
        self.searchTXT_var = StringVar()
        txtSearch = Entry(BtnFrame, textvariable=self.searchTXT_var,
                          width=20, font=("Satoshi", 10, "bold"), bg = "#fefef9", fg = "black")
        txtSearch.grid(row=0, column=7)
        btnSearch = Button(BtnFrame, command=self.search_Data,text="SEARCH",
                           font=("Satoshi", 10, "bold"), width=13, bg="#5EC9CC", fg="black")
        btnSearch.grid(row=0, column=8, padx = 15)
        btnShow = Button(BtnFrame, command = self.fetch_data,text="SHOW ALL",
                         font=("Satoshi", 10, "bold"), width=13, bg="#5EC9CC", fg="black")
        btnShow.grid(row=0, column=9)

        ##__________________________________LABELS_&_ENTRY__________________________________
        # ____LEFT____
        # Reference_Number(Combo)____________________
        lbl_RefNum = Label(DataFrameLeft, text="Reference Number:", font=("Satoshi", 12, "bold"), padx=2, pady=6,bg="#475054",fg="#FEFEF9")
        lbl_RefNum.grid(row=0, column=0, sticky="w")

        conn = mysql.connector.connect(host="localhost", username="root", password="PythonProject2024", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select REF from pharma")
        row = my_cursor.fetchall()
        comRefNum = ttk.Combobox(DataFrameLeft, textvariable=self.ref_var,width=18, font=("Satoshi", 10, "bold"), state="readonly")
        comRefNum["values"] = row
        comRefNum.grid(row=0, column=1)
        if row:
            comRefNum.current(0)
        else:
            print("No reference numbers found.")

        # Company_Name____________________
        lbl_CompanyName = Label(DataFrameLeft, text="Company Name:", font=("Satoshi", 12, "bold"), padx=2, pady=6,bg="#475054",fg="#FEFEF9")
        lbl_CompanyName.grid(row=1, column=0, sticky="w")
        txt_CompanyName = Entry(DataFrameLeft, textvariable= self.company_var,width=20, font=("Satoshi", 10, "bold"),bg = "#fefef9", fg = "black")
        txt_CompanyName.grid(row=1, column=1)
        # Medicine_Type(Combo)____________________
        lbl_MedicineType = Label(DataFrameLeft, font=("Satoshi", 12, "bold"), text="Medicine Type:", bg="#475054",fg="#FEFEF9", padx=2,pady=6)
        lbl_MedicineType.grid(row=2, column=0, sticky='W')
        comMedicineType = ttk.Combobox(DataFrameLeft, textvariable= self.medType_var,state="readonly", font=("Satoshi", 10, "bold"), width=18,cursor="hand2")
        comMedicineType['value'] = ("TABLET", "LIQUID", "CAPSULES", "TOPICAL MEDICINES", "DROPS", "INHALERS", "INJECTION")
        comMedicineType.current(0)
        comMedicineType.grid(row=2, column=1)

        # Medicine_Name(Combo)____________________
        lbl_MedicineName = Label(DataFrameLeft, font=("Satoshi", 12, "bold"), text="Medicine Name:", bg="#475054",fg="#FEFEF9", padx=2,pady=6)
        lbl_MedicineName.grid(row=3, column=0, sticky='W')

        conn = mysql.connector.connect(host="localhost", username="root", password="PythonProject2024", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select MEDI_NAME from pharma")
        med = my_cursor.fetchall()

        comMedicineName = ttk.Combobox(DataFrameLeft, textvariable=self.medName_var,state="readonly", font=("Satoshi", 10, "bold"), width=18, cursor="hand2")
        comMedicineName['value'] = med
        comMedicineName.grid(row=3, column=1)

        if med:
            comMedicineName.current(0)
        else:
            print("No medicine names found.")

        # Lot_Number____________________
        lbl_LotNumber = Label(DataFrameLeft, text="Lot Number:", font=("Satoshi", 12, "bold"), padx=2, pady=6,bg="#475054",fg="#FEFEF9")
        lbl_LotNumber.grid(row=4, column=0, sticky="w")
        txt_LotNumber = Entry(DataFrameLeft,textvariable=self.lotNumber_var, width=20, font=("Satoshi", 10, "bold"), bg = "#fefef9", fg = "black")
        txt_LotNumber.grid(row=4, column=1)
        # Issue_Date____________________
        lbl_IssueDate = Label(DataFrameLeft, text="Issue Date:", font=("Satoshi", 12, "bold"), padx=2, pady=6,bg="#475054",fg="#FEFEF9")
        lbl_IssueDate.grid(row=5, column=0, sticky="w")
        txt_IssueDate = Entry(DataFrameLeft, textvariable=self.issued_var,width=20, font=("Satoshi", 10, "bold"), bg = "#fefef9", fg = "black")
        txt_IssueDate.grid(row=5, column=1)
        # Expiration_Date____________________
        lbl_ExprDate = Label(DataFrameLeft, text="Expiration Date:", font=("Satoshi", 12, "bold"), padx=2, pady=6,bg="#475054",fg="#FEFEF9")
        lbl_ExprDate.grid(row=6, column=0, sticky="w")
        txt_ExprDate = Entry(DataFrameLeft, textvariable=self.expires_var,width=20,font=("Satoshi", 10, "bold"), bg = "#fefef9", fg="black")
        txt_ExprDate.grid(row=6, column=1)
        # Uses____________________
        lbl_Uses = Label(DataFrameLeft, text="         Uses:", font=("Satoshi", 12, "bold"), padx=2, pady=6, bg="#475054",fg="#FEFEF9")
        lbl_Uses.grid(row=0, column=3, sticky="w")
        txt_Uses = Entry(DataFrameLeft, textvariable=self.uses_var,width=20, font=("Satoshi", 10, "bold"),bg = "#fefef9", fg ="black")
        txt_Uses.grid(row=0, column=4)
        # Side_Effect____________________
        lbl_SideEffect = Label(DataFrameLeft, text="         Side Effect:", font=("Satoshi", 12, "bold"), padx=2,pady=6, bg="#475054",fg="#FEFEF9")
        lbl_SideEffect.grid(row=1, column=3, sticky="w")
        txt_SideEffect = Entry(DataFrameLeft, textvariable=self.sideEffect_var,width=20, font=("Satoshi", 10, "bold"), bg = "#fefef9", fg = "black")
        txt_SideEffect.grid(row=1, column=4)
        # Warning____________________
        lbl_Warning = Label(DataFrameLeft, text="         Prescriber:", font=("Satoshi", 12, "bold"), padx=2, pady=6,bg="#475054",fg="#FEFEF9")
        lbl_Warning.grid(row=2, column=3, sticky="w")
        txt_Warning = Entry(DataFrameLeft, textvariable=self.warning_var,width=20, font=("Satoshi", 10, "bold"), bg = "#fefef9", fg = "black")
        txt_Warning.grid(row=2, column=4)
        # Dosage____________________
        lbl_Dosage = Label(DataFrameLeft, text="         Dosage:", font=("Satoshi", 12, "bold"), padx=2, pady=6,bg="#475054",fg="#FEFEF9")
        lbl_Dosage.grid(row=3, column=3, sticky="w")
        txt_Dosage = Entry(DataFrameLeft, textvariable=self.dosage_var,width=20, font=("Satoshi", 10, "bold"), bg = "#fefef9", fg = "black")
        txt_Dosage.grid(row=3, column=4)
        # Pricing____________________
        lbl_Pricing = Label(DataFrameLeft, text="         Pricing:", font=("Satoshi", 12, "bold"), padx=2, pady=6,bg="#475054",fg="#FEFEF9")
        lbl_Pricing.grid(row=4, column=3, sticky="w")
        txt_Pricing = Entry(DataFrameLeft, textvariable=self.price_var, width=20, font=("Satoshi", 10, "bold"), bg = "#fefef9", fg = "black")
        txt_Pricing.grid(row=4, column=4)
        # Quantity____________________
        lbl_Quantity = Label(DataFrameLeft, text="         Quantity:", font=("Satoshi", 12, "bold"), padx=2, pady=6,bg="#475054",fg="#FEFEF9")
        lbl_Quantity.grid(row=5, column=3, sticky="w")
        txt_Quantity = Entry(DataFrameLeft, textvariable=self.quantity_var,width=20, font=("Satoshi", 10, "bold"), bg = "#fefef9", fg = "black")
        txt_Quantity.grid(row=5, column=4)


        # ____RIGHT____
        # Reference_Number____________________
        lbl_RefNum = Label(DataFrameRight, text="Reference Number:", font=("Satoshi", 12, "bold"), padx=2, pady=6, bg="#475054",fg="#FEFEF9")
        lbl_RefNum.grid(row=0, column=0, sticky="w")
        txt_RefNum = Entry(DataFrameRight,textvariable= self.refMed_var,width=20, font=("Satoshi", 10, "bold"), bg = "#fefef9", fg = "black")
        txt_RefNum.grid(row=0, column=1)

        # Medicine_Name____________________
        lbl_MedicineName = Label(DataFrameRight, text="Medicine Name:", font=("Satoshi", 12, "bold"), padx=2, pady=6,bg="#475054",fg="#FEFEF9")
        lbl_MedicineName.grid(row=1, column=0, sticky="w")
        txt_MedicineName = Entry(DataFrameRight, textvariable= self.addMed_var,width=20, font=("Satoshi", 10, "bold"), bg = "#fefef9", fg = "black")
        txt_MedicineName.grid(row=1, column=1)

        # Side_Frame____________________
        sideFrame = Frame(DataFrameRight, bg="#FEFEF9", bd=5, relief=RAISED)
        sideFrame.place(x=8, y=90, width=330, height=158)

        sc_x = ttk.Scrollbar(sideFrame, orient=HORIZONTAL)
        sc_y = ttk.Scrollbar(sideFrame, orient=VERTICAL)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y.pack(side=RIGHT, fill=Y)

        #INITIALIZING_TREEVIEW
        self.medicine_table = ttk.Treeview(sideFrame, column=("REF", "MEDICINE"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("REF", text="REF"),
        self.medicine_table.heading("MEDICINE", text="MEDICINE")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("REF", width=100)
        self.medicine_table.column("MEDICINE", width=100)

        self.medicine_table.bind("<ButtonRelease-1>", self.MedGet_cursor)




        ##__________________________________DEPARTMENT_BUTTONS__________________________________
        downFrame = Frame(DataFrameRight, bd=5, relief = RAISED, bg="#FEFEF9")
        downFrame.place(x = 370, y = 90, width = 125, height = 147)

        btnAddMed = Button(downFrame,command=self.AddMed, text="ADD", font=("Satoshi", 10, "bold"),
                           width=13, bg="#5EC9CC", fg="black", pady = 4)
        btnAddMed.grid(row=0, column=0)
        btnUpdateMed = Button(downFrame, command=self.UpdateMed, text="UPDATE", font=("Satoshi", 10, "bold"),
                              width=13, bg="#5EC9CC", fg="black", pady=4)
        btnUpdateMed.grid(row=1, column=0)
        btnDelMed = Button(downFrame, command=self.DeleteMed, text="DELETE", font=("Satoshi", 10, "bold"),
                           width=13, bg="#FD4E62", fg="black",pady=4)
        btnDelMed.grid(row=2, column=0)
        btnClearMed = Button(downFrame,command = self.ClearMed, text="CLEAR", font=("Satoshi", 10, "bold"),
                             width=13, bg="#FD4E62", fg="black",pady=4)
        btnClearMed.grid(row=3, column=0)



        ##__________________________________DETAILS__________________________________
        detailsFrame = Frame(self.root, bd=5, relief=RAISED, bg="#FEFEF9")
        detailsFrame.place(x=0, y=400, width=1366, height=310)

        #____TABLE____
        tableFrame = Frame(self.root, bd=5, relief=RAISED, bg="#FEFEF9")
        tableFrame.place(x=0, y=400, width=1366, height=310)

        scroll_x = ttk.Scrollbar(tableFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableFrame, orient=VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.pharmacy_table = ttk.Treeview(tableFrame, column = ("REF","COMPANY", "MEDI_TYPE", "MEDI_NAME", "LOT_NUMBER"
                                                                 , "ISSUED", "EXPIRES", "USES", "SIDE_EFFECT", "WARNING"
                                                                 , "DOSAGE", "PRICE", "QUANTITY"), xscrollcommand=scroll_x.set
                                                                 , yscrollcommand= scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
        self.pharmacy_table["show"] = "headings"
        self.pharmacy_table.heading("REF", text="ReferenceNumber")
        self.pharmacy_table.heading("COMPANY", text="CompanyName")
        self.pharmacy_table.heading("MEDI_TYPE", text="MedicineType")
        self.pharmacy_table.heading("MEDI_NAME", text="MedicineName")
        self.pharmacy_table.heading("LOT_NUMBER", text="LotNumber")
        self.pharmacy_table.heading("ISSUED", text="IssueDate")
        self.pharmacy_table.heading("EXPIRES", text="ExpirationDate")
        self.pharmacy_table.heading("USES", text="Uses")
        self.pharmacy_table.heading("SIDE_EFFECT", text="SideEffect")
        self.pharmacy_table.heading("WARNING", text="Warning")
        self.pharmacy_table.heading("DOSAGE", text="Dosage")
        self.pharmacy_table.heading("PRICE", text="Price")
        self.pharmacy_table.heading("QUANTITY", text="Quantity")
        self.pharmacy_table.pack(fill=BOTH, expand=1)

        self.pharmacy_table.column("REF", width=120)
        self.pharmacy_table.column("COMPANY", width=100)
        self.pharmacy_table.column("MEDI_TYPE", width=100)
        self.pharmacy_table.column("MEDI_NAME", width=100)
        self.pharmacy_table.column("LOT_NUMBER", width=100)
        self.pharmacy_table.column("ISSUED", width=100)
        self.pharmacy_table.column("EXPIRES", width=100)
        self.pharmacy_table.column("USES", width=100)
        self.pharmacy_table.column("SIDE_EFFECT", width=100)
        self.pharmacy_table.column("WARNING", width=100)
        self.pharmacy_table.column("DOSAGE", width=100)
        self.pharmacy_table.column("PRICE", width=100)
        self.pharmacy_table.column("QUANTITY", width=100)

        self.fetch_DataMed()
        self.fetch_data()

        self.pharmacy_table.bind("<ButtonRelease-1>", self.Get_Cursor)






    ##__________________________________MEDICINE_TABLE__________________________________
    def AddMed(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root",
                                           password="PythonProject2024", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into pharma(REF, MEDI_NAME) values(%s, %s)", (
                self.refMed_var.get(),
                self.addMed_var.get()
            ))
            conn.commit()  # Commit the transaction
            messagebox.showinfo("Success", "Medicine Added")
            self.fetch_DataMed()
            self.fetch_data()
            self.MedGet_cursor()
        except Exception as e:
            messagebox.showerror("Error", f"An error occured: {e}")
        finally:
            conn.close()

    def fetch_DataMed(self):
        with mysql.connector.connect(host="localhost", username="root",
                                     password="PythonProject2024",database="mydata") as conn:
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM pharma")
            rows = my_cursor.fetchall()

            if rows:
                self.medicine_table.delete(*self.medicine_table.get_children())
                for row in rows:
                    self.medicine_table.insert("", END,
                                               values=tuple(str(item) for item in row))
            conn.commit()

    ##__________________________________MEDICINE_GET_CURSOR__________________________________
    def MedGet_cursor(self, ev=""):
        try:
            selected_row_index = self.medicine_table.focus()
            if selected_row_index is not None:
                selected_row_data = self.medicine_table.item(selected_row_index)
                row_values = selected_row_data["values"]
                self.refMed_var.set(row_values[0])
                self.addMed_var.set(row_values[1])
        except Exception as e:
            print(f"Error retrieving selected row: {e}")

    def UpdateMed(self):
        if self.refMed_var.get() == "" or self.addMed_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root",
                                           password="PythonProject2024", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE pharma SET MEDI_NAME = %s WHERE REF = %s", (
                self.addMed_var.get(),
                self.refMed_var.get(),
            ))
            conn.commit()
            self.fetch_DataMed()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Medicine Updated")

    def DeleteMed(self):
        conn = mysql.connector.connect(host="localhost", username="root",
                                       password="PythonProject2024", database="mydata")
        my_cursor = conn.cursor()

        sql = "delete from pharma where REF = %s"
        val = (self.refMed_var.get(),)
        my_cursor.execute(sql, val)

        conn.commit()
        self.fetch_DataMed()
        self.fetch_data()
        conn.close()

    def ClearMed(self):
        self.refMed_var.set("")
        self.addMed_var.set("")

    ##__________________________________MAIN_TABLE__________________________________
    def add_Data(self):
        try:
            if not self.ref_var.get() or not self.lotNumber_var.get():
                raise ValueError("Reference number and Lot Number are required fields.")
            conn = mysql.connector.connect(host="localhost", username="root",
                                           password="PythonProject2024", database="mydata")
            my_cursor = conn.cursor()
            check_query = "SELECT COUNT(*) FROM pharmacy WHERE REF = %s"
            my_cursor.execute(check_query, (self.ref_var.get(),))
            result = my_cursor.fetchone()
            if result[0] > 0:
                messagebox.showwarning("Warning", "This REF already exists. Consider updating the existing record.")
            else:
                insert_query = """INSERT INTO pharmacy VALUES (%s, %s, %s, %s, %s, 
                                  %s, %s, %s, %s, %s, %s, %s, %s)"""
                insert_data = (self.ref_var.get(),
                               self.company_var.get(), self.medType_var.get(), self.medName_var.get(),
                               self.lotNumber_var.get(), self.issued_var.get(), self.expires_var.get(),
                               self.uses_var.get(), self.sideEffect_var.get(), self.warning_var.get(),
                               self.dosage_var.get(), self.price_var.get(), self.quantity_var.get())
                my_cursor.execute(insert_query, insert_data)
                conn.commit()
                self.fetch_DataMed()
                self.fetch_data()
                self.Get_Cursor()
                self.MedGet_cursor()
                messagebox.showinfo("Success", "Data Inserted")
        except (ValueError, mysql.connector.Error) as err:
            messagebox.showerror("Error", f"An error occurred: {err}")
        finally:
            conn.close()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root",
                                       password="PythonProject2024", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharmacy")
        rows = my_cursor.fetchall()
        self.pharmacy_table.delete(*self.pharmacy_table.get_children())
        for row in rows:
            safe_row = [str(item) for item in row]
            self.pharmacy_table.insert("", END, values=safe_row)

        conn.commit()
        conn.close()

    def Get_Cursor(self, ev = ""):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row = content["values"]
        self.ref_var.set(row[0])
        self.company_var.set(row[1])
        self.medType_var.set(row[2])
        self.medName_var.set(row[3])
        self.lotNumber_var.set(row[4])
        self.issued_var.set(row[5])
        self.expires_var.set(row[6])
        self.uses_var.set(row[7])
        self.sideEffect_var.set(row[8])
        self.warning_var.set(row[9])
        self.dosage_var.set(row[10])
        self.price_var.set(row[11])
        self.quantity_var.set(row[12])

    def Update(self):
        try:
            if not self.ref_var.get():
                raise ValueError("Reference number is a required field.")

            conn = mysql.connector.connect(host="localhost", username="root",
                                           password="PythonProject2024", database="mydata")
            my_cursor = conn.cursor()

            update_query = """UPDATE pharmacy 
                              SET COMPANY=%s, MEDI_TYPE=%s, MEDI_NAME=%s, 
                                  LOT_NUMBER=%s, ISSUED=%s, EXPIRES=%s, USES=%s, 
                                  SIDE_EFFECT=%s, WARNING=%s, DOSAGE=%s, PRICE=%s, 
                                  QUANTITY=%s 
                              WHERE REF=%s"""
            update_data = (self.company_var.get(), self.medType_var.get(), self.medName_var.get(),
                           self.lotNumber_var.get(), self.issued_var.get(), self.expires_var.get(),
                           self.uses_var.get(), self.sideEffect_var.get(), self.warning_var.get(),
                           self.dosage_var.get(), self.price_var.get(), self.quantity_var.get(),
                           self.ref_var.get())
            my_cursor.execute(update_query, update_data)
            conn.commit()
            conn.close()
            messagebox.showinfo("UPDATE", "Record has been updated successfully")

        except (ValueError, mysql.connector.Error) as err:
            messagebox.showerror("Error", f"An error occurred: {err}")

    def Delete(self):
        conn = mysql.connector.connect(host="localhost", username="root",
                                       password="PythonProject2024", database="mydata")
        my_cursor = conn.cursor()
        sql = "delete from pharmacy where REF = %s"
        val = (self.ref_var.get(),)
        my_cursor.execute(sql, val)
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("UPDATE", "Record has been deleted successfully")


    def Reset(self):
        #self.ref_var.set("")
        self.company_var.set("")
        #self.medType_var.set("")
        #self.medName_var.set("")
        self.lotNumber_var.set("")
        self.issued_var.set("")
        self.expires_var.set("")
        self.uses_var.set("")
        self.sideEffect_var.set("")
        self.warning_var.set("")
        self.dosage_var.set(r"")
        self.price_var.set(r"")
        self.quantity_var.set(r"")

    def search_Data(self):
        conn = mysql.connector.connect(host="localhost", username="root",
                                       password="PythonProject2024", database="mydata")
        my_cursor = conn.cursor()
        search_term = self.searchTXT_var.get()
        if not search_term:
            print("Please enter a search term.")
            return
        try:
            search_query = f"SELECT * FROM pharmacy WHERE (REF LIKE %s OR MEDI_NAME LIKE %s)"
            my_cursor.execute(search_query, ("%" + search_term + "%", "%" + search_term + "%"))
            rows = my_cursor.fetchall()

            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for row in rows:
                self.pharmacy_table.insert("", END, values=row)
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    ##root.attributes('-fullscreen',True)
    root.state('zoomed')
    root.mainloop()