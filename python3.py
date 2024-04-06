from tkinter import Tk, Frame, Toplevel, Entry, Button, Text, Scrollbar, END, INSERT
from tkinter.messagebox import showerror
from  wikipedia import summary


# create function which will show summary
def get_summary():
    # if summary will be fetch from internet
    try:

        # clear text area
        answer.delete(1.0, END)

        # show summary in text area
        answer.insert(INSERT, summary(keyword_entry.get()))

    # if any it will give error, it will be shown in a new error window
    except Exception as error:

        # Title of new error window is "Error" and message will be
        # string given in variable error
        showerror("Error", error)

    # create a GUI window


root = Tk()

# set title of window
root.title("Wikipedia Summary")

# set geometry of geometry
root.geometry("770x650")

# set window's width and height to
# false => window will not be resizable
root.resizable(False, False)

# set background colour of window
root.configure(bg="dark grey")

# create a frame for entry and button
top_frame = Frame(root, bg="dark grey")
top_frame.pack(side="top", fill="x", padx=50, pady=10)

# create a frame for text area where summary will be displayed
bottom_frame = Frame(root, bg="dark grey")
bottom_frame.pack(side="top", fill="x", padx=10, pady=10)

# create a entry box where user can enter a keyword
keyword_entry = Entry(top_frame, font=("Arial", 20, "bold"), width=25, bd=4)
keyword_entry.pack(side="left", ipady=6)

# create a search button
search_button = Button(top_frame, text="SEARCH", font=(
    "Arial", 18, "bold"), width=15, bd=4, command=get_summary)
search_button.pack(side="right")

# create a scroll bar for text area
scroll = Scrollbar(bottom_frame)

# create a text area where summary will be displayed
answer = Text(bottom_frame, font=("Arial", 18), fg="red",
              width=55, height=20, bd=5, yscrollcommand=scroll.set)
answer.pack(side="left", fill="y")
scroll.pack(side="left", fill="y")

# start the GUI
root.mainloop()
