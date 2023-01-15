from tkinter import *
import tkinter.ttk as ttk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#389855"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
marks = ''
time = 1000
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps, marks
    window.after_cancel(timer)
    step_lb.config(text='')
    canvas.itemconfig(timer_text, text='')
    reps = 1
    marks = ''
    check_lb.config(text=marks)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(*args):
    if reps == 8:
        min = LONG_BREAK_MIN
        step_lb.config(text='20 min break   ⏳🛌🏻', fg=RED)
    elif reps % 2 == 0:
        min = SHORT_BREAK_MIN
        step_lb.config(text='5 min break  ⏳🛌🏻', fg=PINK)
    else:
        min = WORK_MIN
        step_lb.config(text='Work time!  💪🏻🧑🏻‍💻💪🏻', fg=GREEN)
    count_down(min*60-1)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps, marks
    min = int(count/60)
    sec = count % 60
    if sec < 10:
        sec = (f'0{sec}')
    if min < 10:
        min = (f'0{min}')
    canvas.itemconfig(timer_text, text=(f'{min}:{sec}'))
    if count > 0:
        global timer
        timer = window.after(time, count_down, count-1)
    elif reps <8:
        reps += 1
        start_timer(reps)
    else:
        step_lb.config(text='All done!')
        reps = 1
        canvas.itemconfig(timer_text, text='🎉💃🏻🎊')
        # checkmark label
    if reps % 2 == 0 and count == 0:
        marks += '✔'
        check_lb.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

# window----------------------------
window = Tk()
window.title('Pomodoro timer')
window.config(pady=50, padx=100, bg=YELLOW)

# tomato image----------------------------
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)

# timer----------------------------
timer_text = canvas.create_text(100, 130, text='', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Labels----------------------------
    # Timer label----------------------------
timer_lb = Label(text='Pomodoro\nTimer', font=(FONT_NAME, 25, 'bold'), fg=GREEN, bg=YELLOW)
timer_lb.grid(column=1, row=0)
    # step label
step_lb = Label(text='', font=(FONT_NAME, 10, 'bold'), fg=GREEN, bg=YELLOW)
step_lb.grid(column=1, row=3)
    # check label
check_lb = Label(text=marks, font=(FONT_NAME, 10, 'bold'), fg=GREEN, bg=YELLOW)
check_lb.grid(column=1, row=4)
# Buttons----------------------------
    # Star button----------------------------
start_bt = ttk.Button(text='Start', command=start_timer, width=8)
start_bt.grid(column=0, row=2)
    # Reset button----------------------------
reset_bt = ttk.Button(text='Reset', command=reset, width=8)
reset_bt.grid(column=2, row=2)









window.mainloop()
