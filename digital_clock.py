from tkinter import Label, Tk
import time

# box configuration
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x150")
app_window.resizable(1,1)

# text configuration
text_font = ("Boulder",68,'bold')
background = "#f2e750"  # yellow color 
foreground = "#363529"  # black color
border_width = 25

# give input to tkinter box
label = Label(app_window,font=text_font,bg=background,fg=foreground,bd=border_width)
label.grid(row=0,column=1)

# function of clock 
def digitalclock():
    live_time = time.strftime("%H:%M:%S")
    label.config(text = live_time)
    label.after(200,digitalclock)

# Main Program
digitalclock()
app_window.mainloop()