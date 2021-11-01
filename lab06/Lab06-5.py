import tkinter

def convert(f_temp, c_temp):
    f = f_temp.get()
    c_temp.set('{:.1f}'.format((f - 32) * 5 / 9))

window = tkinter.Tk()
frame = tkinter.Frame(window).pack()

f_temp = tkinter.DoubleVar()
c_temp = tkinter.StringVar()

tkinter.Label(frame, text='Temperature in Fahrenheit:').pack()

text = tkinter.Entry(frame, textvar=f_temp).pack()

label = tkinter.Label(window, textvar=c_temp).pack()

button = tkinter.Button(window, text='Convert', command=lambda: convert(f_temp,
c_temp))
button.pack()

button = tkinter.Button(window, text='Quit', command=lambda: window.destroy())
button.pack()

window.mainloop()
