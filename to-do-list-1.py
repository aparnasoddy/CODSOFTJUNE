#importing packages 
from  tkinter import * 
import tkinter.messagebox
from tkinter import messagebox
from tkinter import ttk


#function to enter the task in the Listbox
def entertask():
    #A new window to pop up to take input
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
           show_custom_warning()
        else:
            listbox_task.insert(END,input_text)
            #close the root1 window
            root1.destroy()
    root1=Tk()
    root1.title("Add task")
    root1.configure(bg="blue")
    entry_task=Text(root1,width=40,height=4,bg="lightgray")
    entry_task.pack()
    button_temp=Button(root1,text="Add task",command=add, bg="green", fg="white")
    button_temp.pack()
    root1.mainloop()
    
def show_custom_warning():
    global warning_box
    x, y = root1.winfo_pointerxy()
    warning_box = Toplevel(root1)
    warning_box.geometry("+{}+{}".format(x, y))
    warning_box.title("Warning!")
    warning_box.configure(bg="red")
    message_label = Label(warning_box, text="Please Enter some Text", bg="red", fg="white")
    message_label.pack()

#function to facilitate the delete task from the Listbox
def deletetask():
    #selects the slected item and then deletes it 
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])
#Executes this to mark completed 

def markcompleted():
    marked=listbox_task.curselection()
    temp=marked[0]
    #store the text of selected item in a string
    temp_marked=listbox_task.get(marked)
    #update it 
    temp_marked=temp_marked+" ✔"
    #delete it then insert it 
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)
#creating the initial window
window=Tk()
#giving a title
window.title("To_Do_APP")


#Frame widget to hold the listbox and the scrollbar
frame_task=Frame(window)
frame_task.pack()

#to hold items in a listbox
listbox_task=Listbox(frame_task,bg="grey",fg="white",height=15,width=50,font = "Helvetica")  
listbox_task.pack(side=LEFT, fill=BOTH, expand=True)


#Scrolldown in case the total list exceeds the size of the given window 
scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)


#Button widget 
entry_button=Button(window,text="Add task",width=50,command=entertask, bg="green", fg="white")
entry_button.pack(pady=3)

delete_button=Button(window,text="Delete selected task",width=50,command=deletetask,bg="red", fg="white")
delete_button.pack(pady=3)

mark_button=Button(window,text="Mark as completed ",width=50,command=markcompleted, bg="blue", fg="white")
mark_button.pack(pady=3)


window.mainloop()


