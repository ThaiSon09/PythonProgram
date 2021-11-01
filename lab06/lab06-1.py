import tkinter
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, text='Goodbye', command=lambda:
window.destroy())