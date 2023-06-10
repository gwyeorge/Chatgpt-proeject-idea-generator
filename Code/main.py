import  os
import  openai
import customtkinter as ctk
import pyttsx3

engine = pyttsx3.init()

def generate():
    prompt = "Please generate 10 ideas for coding projects."
    language = language_dropdown.get()
    prompt += "The programming language is " + language + ". "
    difficulty = difficulty_value.get()
    prompt += "The difficulty is " + difficulty + ". "

    if checkbox1.get():
        prompt += "The project should include a database."
    if checkbox2.get():
        prompt += "The project should include a API"

    print(prompt)
    #replace OPENAI_API_KEY with your API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

    global answer
    answer = response.choices[0].message.content
    print(answer)
    result.insert("0.0", answer)



def readanswer():
    global answer

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(answer)

    engine.runAndWait()

window = ctk.CTk()
window.geometry("900x550")
window.title("ChatGPT Project Generator")

ctk.set_appearance_mode("dark")

title_label = ctk.CTkLabel(window,text="Project Idea Generator",
                           font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(1,1))

frame = ctk.CTkFrame(window)
frame.pack(fill="x", padx=100)

language_frame = ctk.CTkFrame(frame)
language_frame.pack(padx=100, pady=(20,5), fill="both")
language_label = ctk.CTkLabel(
    language_frame, text="Programming Language",font=ctk.CTkFont(weight="bold")
)
language_label.pack()
language_dropdown = ctk.CTkComboBox(
    language_frame, values=["Python","Java","C++","Javascript","Golang"])
language_dropdown.pack(pady=10)

difficulty_frame = ctk.CTkFrame(frame)
difficulty_frame.pack(padx=100, pady=5, fill="both")
difficulty_label = ctk.CTkLabel(
    difficulty_frame, text="Project Difficulty", font=ctk.CTkFont(weight="bold"))
difficulty_label.pack()
difficulty_value = ctk.StringVar(value="Easy")
radiobutton1 = ctk.CTkRadioButton(
    difficulty_frame, text="Easy", variable=difficulty_value,value="Easy"
)
radiobutton1.pack(side="left", padx=(20, 10), pady=10)

radiobutton2 = ctk.CTkRadioButton(
    difficulty_frame, text="Normal", variable=difficulty_value,value="Normal"
)
radiobutton2.pack(side="left",padx=(20,10), pady=10)

radiobutton3 = ctk.CTkRadioButton(
    difficulty_frame, text="Hard", variable=difficulty_value,value="Hard"
)
radiobutton3.pack(side="left",padx=(20,10), pady=10)

features_frame = ctk.CTkFrame(frame)
features_frame.pack(padx=100,pady=5, fill="both")
features_label = ctk.CTkLabel(
    features_frame, text="Features", font=ctk.CTkFont(weight="bold")
)
features_label.pack()
checkbox1 = ctk.CTkCheckBox(features_frame, text="Database")
checkbox1.pack(side="left",padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox(features_frame, text="API")
checkbox2.pack(side="left",padx=50, pady=10)

button_frame = ctk.CTkFrame(frame)
button_frame.pack(padx=100, pady=(5, 20))

button_generate = ctk.CTkButton(button_frame, text="Generate Ideas", command=generate)
button_generate.pack(side="left", padx=(0, 10))

button_read = ctk.CTkButton(button_frame, text="Read Answer", command=readanswer)
button_read.pack(side="left", padx=(10, 0))


result = ctk.CTkTextbox(window, font=ctk.CTkFont(size=15))
result.pack(pady=10, fill="x", padx=100)

window.mainloop()
