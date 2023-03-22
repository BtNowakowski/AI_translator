import openai
from tkinter import *
from tkinter import messagebox
from api_key import API_KEY

# set API key
openai.api_key = API_KEY

# placeholders for target language and source text fields
target_language_placeholder = "Polish"
source_text_placeholder = "Your veeeeeeeeeeeeeeery long sentence to be translated"

# translate function - takes text and target language as arguments and returns translated text
def translate(text, target_language):
    prompt = f"Translate text to {target_language} \"{text}\""

    # call OpenAI API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    # show translated text in messagebox
    messagebox.showinfo("Translation", "Your translated sentence: "+response.choices[0].text)

# translation process - checks if fields are empty and if not, translate the text to target language, if yes, ask user if he wants to translate the placeholder text  
def translation_process(text, target_language):
    if len(text) <= 2 or len(target_language) <= 2:
        messagebox.showerror("Error", "Please enter text to translate")
    elif text == source_text_placeholder:
        if messagebox.askyesno("You sure", "Are you sure you want to translate this text?") == True:
            translate(text, target_language)
    else:
        translate(text, target_language)

# GUI
window = Tk()
window.geometry("620x150")
window.title("Translator")
window.resizable(False, False)

source_text = StringVar()
target_language = StringVar()

frame = Frame(window, highlightcolor="white")
frame.pack(pady=10, padx=15)

# target language field
Label(frame, text="Translate to: ", font=(
    "Calibri 14")).grid(row=0, column=0, pady=5, columnspan=1, sticky=W)
target_language_entry = Entry(frame, textvariable=target_language, width=50, font=("Calibri", 12))
target_language_entry.grid(row=0, column=1, padx=5, pady=5, ipady=3)

# placeholder for target language field
target_language_entry.insert('0', target_language_placeholder)
target_language_entry.bind("<FocusIn>", lambda args: target_language_entry.delete('0', 'end'))

# source text field
Label(frame, text="Text to translate: ", font=(
    "Calibri 14")).grid(row=1, column=0, pady=5, columnspan=1, sticky=W)
source_text_entry = Entry(frame, textvariable=source_text, width=50, font=("Calibri", 12))
source_text_entry.grid(row=1, column=1, padx=5, pady=5, ipady=3)

# placeholder for source text field
source_text_entry.insert('0', source_text_placeholder)
source_text_entry.bind("<FocusIn>", lambda args: source_text_entry.delete('0', 'end'))

submit_button = Button(frame, cursor="hand2",
                    height=1, width=10, text="Submit", command=lambda: translation_process(source_text.get(), target_language.get())).grid(row=2, column=1, padx=5, pady=5, ipady=3, sticky=W+E+N+S)
mainloop()