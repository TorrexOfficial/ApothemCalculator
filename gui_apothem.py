import tkinter as tk

def operation():
    f_triangle = 0.289
    f_square = 0.5
    f_pentagon = 0.688
    f_hexagon = 0.866
    f_heptagon = 1.038
    f_octagon = 1.207
    f_nonagon = 1.374
    f_decagon = 1.539
    f_dodecagon = 1.866
    figura = entry_shape.get()
    side = entry_side.get()
    risultato = ""
    if (int(figura) == 0):
        risultato = (int(side) * float(f_triangle))
    if (int(figura) == 1):
        risultato = (int(side) * float(f_square))
    if (int(figura) == 2):
        risultato = (int(side) * float(f_pentagon))
    if (int(figura) == 3):
        risultato = (int(side) * float(f_hexagon))
    if (int(figura) == 4):
        risultato = (int(side) * float(f_heptagon))
    if (int(figura) == 5):
        risultato = (int(side) * float(f_octagon))
    if (int(figura) == 6):
        risultato = (int(side) * float(f_nonagon))
    if (int(figura) == 7):
        risultato = (int(side) * float(f_decagon))
    if (int(figura) == 8):
        risultato = (int(side) * float(f_dodecagon))
    
    lbl_result["text"] = f"{risultato}"


window = tk.Tk()
window.title("calcolatore apotema")
window.resizable(width=False, height=False)

lbl_instruction = tk.Label(text="Press 0 for equilater triangle, 1 for squaref_square, 2 for pentagon, 3 for hexagon, 4 for heptagon, 5 for octagon, 6 for nonagon, 7 for decagon, 8 for dodecagon")
lbl_instruction.pack()

lbl_shape = tk.Label(text="Choose a side")
lbl_shape.pack()

entry_shape = tk.Entry()
entry_shape.pack()

lbl_shape = tk.Label (text = "Insert the side of the shape")
lbl_shape.pack()

entry_side = tk.Entry()
entry_side.pack()

btn_result = tk.Button(text = "calculate", command=operation)
btn_result.pack()

lbl_result = tk.Label(text = "Here will appear the result")
lbl_result.pack()

window.mainloop()