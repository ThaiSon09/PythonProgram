import tkinter
def increment(text):
 """ Increment number represented by the contents of text by 1 and 
update
 text with the result."""
 count = int(text.get())
 text.set(str(count + 1))
window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
text = tkinter.StringVar()
text.set('0')
button = tkinter.Button(frame, textvariable=text,
command=lambda: increment(text))
button.pack()
window.mainloop()
print(tkinter)
