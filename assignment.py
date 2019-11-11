from tkinter import *
from tkinter import ttk
import mysql.connector


try:
    con = mysql.connector.connect(host='localhost', user='root', password='banahbiyasta22', database='assignment')
    cur = con.cursor()
except mysql.connector.Error as e:
    print(e)

class Student_info:
    def __init__(self, root):

        self.root = root

        #--------label---------
        self.firstnframe = Label(self.root, text='First Name')
        self.firstnframe.grid(row=1, column=0, padx=15, pady=15)

        self.lnamef = Label(self.root,text='Last Name')
        self.lnamef.grid(row=2, column=0, padx=15, pady=15)

        self.lblAdd = Label(self.root,text="Address")
        self.lblAdd.grid(row=3, column=0, padx=15, pady=15)

        self.lblage = Label(self.root,text='Age')
        self.lblage.grid(row=4, column=0, padx=15, pady=15)

        self.lblid=Label(self.root,text='ID')
        self.lblid.grid(row=0, column=0, padx=15, pady=15)

        self.lblcontact = Label(self.root, text='Contact Number')
        self.lblcontact.grid(row=5, column=0, padx=15, pady=15)

        self.lbldeg = Label(self.root, text='Degree')
        self.lbldeg.grid(row=6, column=0, padx=15, pady=15)
        #---------Entry---------
        self.id = Entry(self.root)
        self.id.grid(row=0, column=1, padx=15, pady=15)

        self.firsten = Entry(self.root)
        self.firsten.grid(row=1, column=1, padx=15, pady=15)

        self.len = Entry(self.root)
        self.len.grid(row=2, column=1, padx=15, pady=15)

        self.Adden = Entry(self.root)
        self.Adden.grid(row=3, column=1, padx=15, pady=15)

        self.ageen = Entry(self.root)
        self.ageen.grid(row=4, column=1, padx=15, pady=15)

        self.contact = Entry(self.root)
        self.contact.grid(row=5, column=1, padx=15, pady=15)

        self.deg = Entry(self.root)
        self.deg.grid(row=6, column=1, padx=15, pady=15)

        #------------frame---------
        self.btn_frame = Frame(self.root, bd=4, bg='light pink', relief=RIDGE)
        self.btn_frame.place(x=20, y=350, width=600, height=50)

        self.table_frame = Frame(self.root, bd=4, bg='light pink', relief=RIDGE)
        self.table_frame.place(x=20, y=400, width=600, height=350)

        #-------scrollbar--------
        self.scroll_x = Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y = Scrollbar(self.table_frame, orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT, fill=Y)

        #----------Table---------
        self.student_table=ttk.Treeview(self.table_frame, columns=('Id','fname', 'lname', 'Address', 'Age','contact','Degree'),
                                        xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.student_table.heading('Id', text='ID')
        self.student_table.heading('fname',text='Fname')
        self.student_table.heading('lname', text='Lname')
        self.student_table.heading('Address', text='Address')
        self.student_table.heading('Age', text='Age')
        self.student_table.heading('contact', text='Contact number')
        self.student_table.heading('Degree', text='Degree')
        self.student_table.pack(fill=BOTH,expand=True)

        self.student_table['show']='headings'

        self.student_table.column('Id', width=40)
        self.student_table.column('fname',width=70)
        self.student_table.column('lname', width=70)
        self.student_table.column('Address', width=80)
        self.student_table.column('Age', width=80)
        self.student_table.column('contact', width=90)
        self.student_table.column('Degree', width=90)


        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)

        self.show()

        self.student_table.bind('<ButtonRelease-1>',self.pointer)
        self.student_table.pack(fill=BOTH, expand=True)



        #-----------button--------
        self.addbtn=Button(self.btn_frame, text='Add',command=self.add_info, width=15,height=2)
        self.addbtn.grid(row=5, column=0,padx=10)

        self.upbtn=Button(self.btn_frame,text='Update',command=self.update,width=15,height=2)
        self.upbtn.grid(row=5,column=2,padx=10)
        self.deletebtn=Button(self.btn_frame,text='Delete',command=self.delete,width=15,height=2)
        self.deletebtn.grid(row=5,column=4,padx=10)
        self.clearbtn=Button(self.btn_frame,text='Clear',command=self.clear,width=15,height=2)
        self.clearbtn.grid(row=5,column=6,padx=10)


        self.detail_frame=Frame(self.root,bd=4,relief=RIDGE)
        self.detail_frame.place(x=280,y=10,width=400,height=200)


        self.searchlbl=Label(self.detail_frame,text= 'Search text',width=10,font=('arial',10))
        self.searchlbl.grid(row=2,column=0,pady=5)

        self.searchentry=Entry(self.detail_frame,width=20)
        self.searchentry.grid(row=2,column=1,pady=5)

        self.searchbtn=Button(self.detail_frame,text='Search',command=self.search,font=('arial',10),width=8)
        self.searchbtn.grid(row=2,column=3,pady=10,padx=10)

        self.lblsort = Label(self.detail_frame, text='Sort By', font=('arial', 10))
        self.lblsort.grid(row=0, column=0, pady=5)

        self.sortcombo = ttk.Combobox(self.detail_frame, font=('arial', 10), state='readonly',width=15)
        self.sortcombo['values'] = ('Ascending', 'Descending')
        self.sortcombo.set("Ascending")
        self.sortcombo.grid(row=0, column=1, pady=5, padx=5)

        self.sortcombo.bind("<<ComboboxSelected>>", lambda e: self.sort())


    def add_info(self):
        try:
            id = self.id.get()
            fname = self.firsten.get()
            lname = self.len.get()
            Address = self.Adden.get()
            Age = self.ageen.get()
            cont = self.contact.get()
            degr = self.deg.get()
            query = 'insert into babita1 values(%s,%s,%s,%s,%s,%s,%s);'
            values = (id, fname, lname, Address, Age, cont, degr)
            cur.execute(query, values)
            print('1 row inserted')
            con.commit()
            self.show()
            self.clear()
        except ValueError as err:
            print(err)

    def show(self):
        query='select * from babita1'
        cur.execute(query)
        rows=cur.fetchall()

        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('',END,values=row)


    def clear(self):
        self.id.delete(0,END)
        self.firsten.delete(0,END)
        self.len.delete(0,END)
        self.Adden.delete(0,END)
        self.ageen.delete(0,END)
        self.contact.delete(0,END)
        self.deg.delete(0,END)

    def bubbleSort(self, arr):
        n = len(arr)

        if self.sortcombo.get() == "Ascending":
            # Traverse through all array elements
            for i in range(n):

                # Last i elements are already in place
                for j in range(0, n - i - 1):

                    # traverse the array from 0 to n-i-1
                    # Swap if the element found is greater
                    # than the next element
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        else:
            # Traverse through all array elements
            for i in range(n):

                # Last i elements are already in place
                for j in range(0, n - i - 1):

                    # traverse the array from 0 to n-i-1
                    # Swap if the element found is greater
                    # than the next element
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    def sort(self):
        query = 'select * from babita1'
        cur.execute(query)
        rows = cur.fetchall()

        self.bubbleSort(rows)

        self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('', END, values=row)



    def update(self):
        try:
            d1 = self.id.get()
            d2 = self.firsten.get()
            d3 = self.len.get()
            d4 = self.Adden.get()
            d5 = self.ageen.get()
            d6 = self.contact.get()
            d7 = self.deg.get()

            query = 'update babita1 set fname=%s,lname=%s,address=%s,age=%s,contact=%s,deg=%s where id=%s'
            values = (d2, d3, d4, d5, d6, d7, d1)
            cur.execute(query, values)
            con.commit()
            self.clear()
            self.show()
        except ValueError as err:
            print(err)


    def pointer(self,event):
        try:
            point = self.student_table.focus()
            content = self.student_table.item(point)
            row = content['values']
            self.clear()
            self.id.insert(0, row[0])
            self.firsten.insert(0, row[1])
            self.len.insert(0, row[2])
            self.Adden.insert(0, row[3])
            self.ageen.insert(0, row[4])
            self.contact.insert(0, row[5])
            self.deg.insert(0, row[6])
        except IndexError:
            pass


    def delete(self):
        selected_item = self.student_table.selection()
        self.student_table.delete(selected_item)

        age=self.ageen.get()
        query = 'delete from babita1 where Age=%s'
        values=(age,)

        cur.execute(query,values)
        con.commit()
        self.clear()
        #self.show()


    def search(self, mylist=None):
        if not mylist:
            query = 'select * from babita1'
            cur.execute(query)
            rows = cur.fetchall()
        else:
            rows = mylist
        found = []
        target = self.searchentry.get()
        for value in rows:
            if target in value:
                found.append(value)

        self.student_table.delete(*self.student_table.get_children())

        for row in found:
            self.student_table.insert('',END,values=row)

        return found


if __name__ == '__main__':
    root = Tk()
    root.geometry('700x700+0+0')
    root.title('Student Form')
    root.configure(bg='light blue')
    gui = Student_info(root)
    root.mainloop()


