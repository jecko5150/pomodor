from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
# window.minsize(width=200, height=224)
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
Canvas()
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'bold'))
timer_label.grid(column=0, row=0)

canvas.grid()
check_mark = Label(text="✔",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, 'bold'))
check_mark.grid(column=0, row=5)

window.mainloop()
