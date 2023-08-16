
import tkinter as tk


def Deshabilitar_botones(row, col):
    for vertical in range(10):
        botones[vertical][col].config(state='disable', bg='red')
    for horiz in range(5):
        botones[row][horiz].config(state='disable',  bg='red')


brr = tk.Tk()

botones = []
for vertical in range(10):
    row_botones = []
    for horiz in range(5):
        Button = tk.Button(brr, text=' ', width=5, height=2,
                           command=lambda vertical=vertical, horiz=horiz: Deshabilitar_botones(vertical, horiz))
        Button.grid(row=vertical, column=horiz)
        row_botones.append(Button)
    botones.append(row_botones)

brr.mainloop()