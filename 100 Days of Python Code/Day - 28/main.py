import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps, check
    reps = 0
    check = 0
    window.after_cancel(timer)
    #timer_text 00:00
    canvas.itemconfig(timer_text, text=f"00:00")
    #title_label Timer
    timer_label.config(text='Timer', fg=GREEN)
    #reset check_marks
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    reps += 1

    # If it's the 8th rep:
    if reps % 8 == 0:
        timer_label.config(text='Break', fg=RED)
        count_down(long_break_min)
    # If it's the 2nd/4nd/6th:
    elif reps % 2 == 0:
        timer_label.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    # If it's the 1st/3rd/5th/7th rep:
    else:
        timer_label.config(text='Work', fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count % 60}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down,count-1)
    else:
        global check
        if reps % 8 == 0:
            check = 0
            check_label.config(text = "")
        elif reps % 2 != 0:
            check += 1
            check_label.config(text = "✔"*check)

        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
img_tomato = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(103,112, image=img_tomato)
timer_text = canvas.create_text(103,130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = tkinter.Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
timer_label.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)

check_label = tkinter.Label(fg=GREEN,bg=YELLOW, font=(FONT_NAME, 10, 'bold'))
check_label.grid(column=1, row=3)

window.mainloop()