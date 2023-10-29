from tkinter import *
import requests
response = requests.get("https://api.kanye.rest")
quote = response.json()["quote"]
def get_quote():
    global quote,response
    response = requests.get("https://api.kanye.rest")
    quote = response.json()["quote"]
    canvas.itemconfig(text1, text=quote)



window = Tk()
window.title("Kanyee Says..")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
kanye_img = PhotoImage(file="kanye.png")
back_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=back_img)
text1 = canvas.create_text(150, 207, text=quote, width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

btn = Button(image=kanye_img, highlightthickness=0, command=get_quote)
btn.grid(column=1, row=2)

window.mainloop()