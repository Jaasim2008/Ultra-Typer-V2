from tkinter import *
from tkinter import messagebox
from json_manager import *
from pynput.keyboard import Key, Controller
import time

root = Tk()
root.title('Ultra Typer v2')
root.geometry('700x400')
my_icon = PhotoImage(file='keyboard.png')
root.iconphoto(False, my_icon)
dark_col = '#3d3d3d'
root.config(bg=dark_col)

frame1 = Frame(root, bg=dark_col)
frame1.pack(fill=BOTH)


def page_two():
    frame2 = Frame(bg=dark_col)
    frame2.pack(fill=BOTH)

    def start_type():
        new_module = Json_Manager('settings.json')
        word_data = new_module.get_data('word')
        number_data = new_module.get_data('number')
        keyb = Controller()
        time.sleep(5)
        for x in range(int(number_data)):
            time.sleep(0.1)
            for char in word_data:
                keyb.press(char)
                keyb.release(char)
        messagebox.showinfo('Done!', 'Finished Typing!')
        new_module.clear_data()

    btn2 = Button(frame2, bg=dark_col, text='Start Typing ( start in 5 sec )', font=('Arial Italic', 20), relief=SUNKEN
                  , bd=0, command=start_type, fg='white')
    btn2.pack(pady=20)

    btn3 = Button(frame2, bg=dark_col, text='Quit App', font=('Arial Italic', 20), relief=SUNKEN, bd=0,
                  command=root.destroy, fg='white')
    btn3.pack(pady=20)


def save_and_move():
    the_word = ent1.get()
    the_number = ent2.get()

    new_mod = Json_Manager('settings.json')
    new_mod.write_data('word', the_word)
    new_mod.append_data('number', the_number)

    frame1.pack_forget()
    page_two()


lbl = Label(frame1, bg=dark_col, text='Enter Word :', font=('Arial Italic', 17), fg='white')
lbl.pack(pady=20)

ent1 = Entry(frame1, bg=dark_col, bd=1, relief=SUNKEN, font=('Arial Italic', 20), fg='white')
ent1.pack(pady=20)

lbl2 = Label(frame1, bg=dark_col, text='Enter Number Of Times The Word Should Be Typed :', fg='white', bd=0
             , font=('Arial Italic', 17))
lbl2.pack(pady=20)

ent2 = Entry(frame1, bg=dark_col, bd=1, relief=SUNKEN, font=('Arial Italic', 20), fg='white')
ent2.pack(pady=20)

btn1 = Button(frame1, bg=dark_col, text='Submit Data', bd=1, relief=SUNKEN, font=('Arial Italic', 20), fg='orange'
              , command=save_and_move)
btn1.pack(pady=20, side=BOTTOM)

root.mainloop()
