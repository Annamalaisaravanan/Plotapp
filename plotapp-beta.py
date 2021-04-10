import tkinter as tk
import seaborn as sns
from tkinter.filedialog import askopenfilename
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog, messagebox, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,FigureCanvas
root=tk.Tk()
sns.set_theme(color_codes=True)




def file2():
    return malai
    


def file1():
    global malai
    malai=filedialog.askopenfilename(initialdir="/",
                                              title="Select A File",
                                              filetype=(("CSC files", "*.csv"),("xlsx files", "*.xlsx"),("All Files", "*.*")))
    return malai

def get():
    
    # initalise the tkinter GUI
    root = tk.Tk()
    
    root.geometry("500x500") # set the root dimensions
    root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
    root.resizable(0, 0) # makes the root window fixed in size.
    
    # Frame for TreeView
    frame1 = tk.LabelFrame(root, text="Excel Data")
    frame1.place(height=250, width=500)
    
    # Frame for open file dialog
    file_frame = tk.LabelFrame(root, text="Open File")
    file_frame.place(height=100, width=400, rely=0.65, relx=0)
    
    # Buttons
    button1 = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
    button1.place(rely=0.65, relx=0.50)
    
    button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
    button2.place(rely=0.65, relx=0.30)
    
    # The file/file path text
    label_file = ttk.Label(file_frame, text="No File Selected")
    label_file.place(rely=0, relx=0)
    
    
    ## Treeview Widget
    tv1 = ttk.Treeview(frame1)
    tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).
    
    treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
    treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
    tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
    treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget
    
    
    def File_dialog():
        """This Function will open the file explorer and assign the chosen file path to label_file"""
        filename = file1()
        label_file["text"] = filename
        return None
    
    
    def Load_excel_data():
        """If the file selected is valid this will load the file into the Treeview"""
        file_path = label_file["text"]
        try:
            excel_filename = r"{}".format(file_path)
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)
    
        except ValueError:
            tk.messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror("Information", f"No such file as {file_path}")
            return None
    
        clear_data()
        tv1["column"] = list(df.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column) # let the column heading = column name
    
        df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
        for row in df_rows:
            tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
        return None
    
    
    def clear_data():
        tv1.delete(*tv1.get_children())
        return None
    
    
    root.mainloop()
     
def show():
    filename=file2()
    my_data=pd.read_csv(filename)
    root1=tk.Tk()
    figure1=plt.figure(figsize=(5,4),dpi=100)
    ax1=figure1.add_subplot(211)
    bar1=FigureCanvas(figure1,root1)
    bar1.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH)
    df1=my_data[[str(ans2.get()),str(ans3.get())]].groupby(str(ans2.get())).sum()
    df1.plot(kind="line",ax=ax1,legend=True)
    ax1.set_title(str(ans2.get())+" vs "+str(ans3.get()))

    figure2=plt.figure(figsize=(5,5),dpi=100)
    ax2=figure2.add_subplot(111)
    line=FigureCanvas(figure2,root1)
    line.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH)
    df1=my_data[[str(ans2.get()),str(ans3.get())]].groupby(str(ans2.get())).sum()
    df1.plot(kind="line",ax=ax2,legend=True)
    ax1.set_title(str(ans2.get())+" vs "+str(ans3.get()))

    figure3=plt.figure(figsize=(5,4),dpi=100)
    ax3=figure3.add_subplot(111)
    ax3.scatter(my_data[str(ans2.get())],my_data[str(ans3.get())],color="g")
    scatter3=FigureCanvas(figure3,root1)
    scatter3.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH)

    ax3.set_title(str(ans2.get())+" vs "+str(ans3.get()))
    
    ax4=figure1.add_subplot(212)
    bar1=FigureCanvas(figure1,root1)
    df1=my_data[[str(ans2.get()),str(ans3.get())]].groupby(str(ans2.get())).sum()
    df1.plot(kind="box",ax=ax4,legend=True)
    
    root1.mainloop()
    
    

canvas=tk.Canvas(root,height=500,width=500)
canvas.pack()

label=tk.Label(root,text="PlotData",bg="gray90")
canvas.create_window(110,100,window=label)

entry1=tk.Entry(root,width=27)
canvas.create_window(225,100,window=entry1)
button=tk.Button(root,text="show",command=get,bg="gray90")
canvas.create_window(225,130,window=button)

button2=tk.Button(root,text="plot",command=show,bg="gray90")
canvas.create_window(350,230,window=button2)

label2=tk.Label(root,text="Column1",bg="gray90")
canvas.create_window(300,160,window=label2)
ans2=tk.Entry(root,width=13)
canvas.create_window(370,160,window=ans2)

label3=tk.Label(root,text="Column2",bg="gray90")
canvas.create_window(300,190,window=label3)
ans3=tk.Entry(root,width=13)
canvas.create_window(370,190,window=ans3)

root.mainloop()