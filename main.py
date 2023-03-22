import openai
from tkinter import *
from tkinter import messagebox
from api_key import API_KEY

openai.api_key = API_KEY

def translate(text, target_language):
    prompt = f"Translate text to {target_language} \"{text}\""

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    messagebox.showinfo("Translation", "Your translated sentence: "+response.choices[0].text)

window = Tk()
window.geometry("620x150")
window.title("Translator")
window.resizable(False, False)

source_text = StringVar()
target_language = StringVar()

frame = Frame(window, highlightcolor="white")
frame.pack(pady=10, padx=15)

Label(frame, text="Translate to: ", font=(
    "Calibri 14")).grid(row=0, column=0, pady=5, columnspan=1, sticky=W)
target_language_entry = Entry(frame, textvariable=target_language, width=50, font=("Calibri", 12))
target_language_entry.grid(row=0, column=1, padx=5, pady=5, ipady=3)

Label(frame, text="Text to translate: ", font=(
    "Calibri 14")).grid(row=1, column=0, pady=5, columnspan=1, sticky=W)
source_text_entry = Entry(frame, textvariable=source_text, width=50, font=("Calibri", 12))
source_text_entry.grid(row=1, column=1, padx=5, pady=5, ipady=3)

submit_button = Button(frame, cursor="hand2",
                    height=1, width=10, text="Submit", command=lambda: translate(source_text.get(), target_language.get())).grid(row=2, column=1, padx=5, pady=5, ipady=3, sticky=W+E+N+S)
mainloop()