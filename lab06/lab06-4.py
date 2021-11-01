import tkinter

def count(text, out_data):
    data = text.get('0.0', tkinter.END)
    counts = {}
    for char in 'ATCG':
        counts[char] = data.count(char)
    print(counts)
    out_data.set('Num As: {0} Num Ts: {1} Num Cs: {2} Num Gs: {3}'.format(
     counts['A'], counts['T'], counts['C'], counts['G']))

window = tkinter.Tk()
text = tkinter.Text(window, height=10, width=40)
text.pack()

out_data = tkinter.StringVar()

button = tkinter.Button(window, text='Count', command=lambda: count(text,
out_data))
button.pack()

label = tkinter.Label(window, textvar=out_data)
label.pack()

window.mainloop()