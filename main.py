from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
CYAN = "#93B5C6"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    tick_mark_label.config(text="")
    canvas.itemconfig(countdown_text, text="00:00")
    global reps
    reps =0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_seconds = 5*60
    short_break_seconds = 5*60
    long_break_seconds = LONG_BREAK_MIN*60

    if reps == 8:
        countdown(long_break_seconds)
        timer_label.config(text="Long break", fg=PINK)
    elif reps%2 == 0:
        countdown(short_break_seconds)
        timer_label.config(text="Short break", fg=GREEN)
    else:
        countdown(work_seconds)
        timer_label.config(text="Work time")




    #countdown(5min*60sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_minute = math.floor(count/60)
    count_seconds = round(count % 60)
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"


    canvas.itemconfig(countdown_text, text=f"{count_minute}:{count_seconds}")
    if count >0:
       global timer
       timer = window.after(1000, countdown, count-1)
    else:

        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✔"
        tick_mark_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=CYAN)




timer_label = Label(text="Timer", font=(FONT_NAME,30,"italic"), fg=RED, bg=CYAN)
timer_label.grid(row=0, column=1)

canvas = Canvas(height=240, width=234, bg=CYAN, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(115,117, image= tomato)
countdown_text = canvas.create_text(115, 130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=2, column=1)


start_button = Button(text="Start", command=start_timer)
# FIRST FUNCTION CALL IS DONE OVER HERE IN THE COMMAND
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=3, column=2)

tick_mark_label = Label(text="", fg=GREEN, bg=CYAN, font=(10))
tick_mark_label.grid(row=3, column=1)



window.mainloop()