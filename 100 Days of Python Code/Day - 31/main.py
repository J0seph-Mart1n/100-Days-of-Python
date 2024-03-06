import tkinter
import random
import csv
import codecs

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
random_word = 0
list_of_words = []
try:
    with open("data/words_to_learn.csv", 'r') as data_file:
        data = csv.reader(data_file)
        for word in data:
            list_of_words.append(word)
except FileNotFoundError:
    pass

#Reading CSV File
with codecs.open('data/japanese_word_pro.csv', 'r', encoding="shift_jis") as data_file:
    data = csv.reader(data_file)
    japanese_words = []
    for word in data:
        japanese_words.append(word)
    print(japanese_words[0])


#changing the words when the button is clicked


def right():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.randint(1, 2999)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(language, text="Japanese", fill='black')
    japanese_text = japanese_words[random_word][0]
    pronunciation = japanese_words[random_word][1]
    canvas.itemconfig(language_text, text=f"{japanese_text}", fill='black', font=('arial', 60, "bold"))
    canvas.itemconfig(pronunciation_text, text=f"{pronunciation}")
    flip_timer = window.after(5000, flip_card)

def wrong():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.randint(1, 2999)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(language, text="Japanese", fill='black')
    japanese_text = japanese_words[random_word][0]
    pronunciation = japanese_words[random_word][1]
    canvas.itemconfig(language_text, text=f"{japanese_text}", fill='black', font=('arial', 60, "bold"))
    canvas.itemconfig(pronunciation_text, text=f"{pronunciation}")
    word_to_learn = canvas.itemcget(language_text, "text")
    word_pronunciation = canvas.itemcget(pronunciation_text, "text")
    english_translation = japanese_words[random_word][2]
    with codecs.open('data/words_to_learn.csv', 'w', encoding="shift_jis") as data_file:
        list_of_words.append([word_to_learn, word_pronunciation, english_translation])
        csvwriter = csv.writer(data_file)
        csvwriter.writerows(list_of_words)
    flip_timer = window.after(5000, flip_card)
#Changing cards

def flip_card():
    word_to_learn = canvas.itemcget(language_text, "text")
    word_pronunciation = canvas.itemcget(pronunciation_text, "text")
    english_translation = japanese_words[random_word][2]

    with codecs.open('data/words_to_learn.csv', 'w', encoding="shift_jis") as data_file:
        list_of_words.append([word_to_learn, word_pronunciation, english_translation])
        csvwriter = csv.writer(data_file)
        csvwriter.writerows(list_of_words)

    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(language_text, text=f"{english_translation}", fill='white', font=(('arial', 20, "bold")))
    canvas.itemconfig(pronunciation_text, text='')


window = tkinter.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(5000, flip_card)
canvas = tkinter.Canvas(width=810, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
#getting images
card_front = tkinter.PhotoImage(file='images/card_front.png')
card_back = tkinter.PhotoImage(file='images/card_back.png')
right_img = tkinter.PhotoImage(file="images/right.png")
wrong_img = tkinter.PhotoImage(file="images/wrong.png")
canvas_image = canvas.create_image(410,263, image=card_front)
language = canvas.create_text(405,150, text="Japanese", fill='black', font=('arial', 40, 'italic'))
language_text = canvas.create_text(405,233, text=f"", fill='black', font=('arial', 60, "bold"))
pronunciation_text = canvas.create_text(405,323, text=f"", fill='black', font=('arial', 30, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#buttons
right_button = tkinter.Button(image=right_img, highlightthickness=0, fg=BACKGROUND_COLOR, command=right)
right_button.grid(row=1, column=0)
wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0, fg=BACKGROUND_COLOR, command=wrong)
wrong_button.grid(row=1, column=1)

window.mainloop()