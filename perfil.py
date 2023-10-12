import customtkinter
import random
from database import food_items, animal_items, object_items  # importando as listas

customtkinter.set_appearance_mode("light")  # define o tema como claro

window = customtkinter.CTk()
window.geometry("800x450")

logo = customtkinter.CTkLabel(
    window, text="Perfil", text_color="#FFAC33", font=("Arial", 35)
)
logo.pack(padx=10, pady=(10, 80))

category_page_title = customtkinter.CTkLabel(
    window, text="Selecione a categoria", font=("Arial", 24)
)

categories = ["Comida", "Animal", "Objeto"]


def handle_exit():  # fecha o programa
    window.destroy()


def display_menu_page():  # funçao de voltar para o menu
    back_to_menu_button.pack_forget()
    category_1_button.pack_forget()
    category_2_button.pack_forget()
    category_3_button.pack_forget()
    category_page_title.pack_forget()

    logo.pack(padx=10, pady=(10, 70))
    play_button.pack(padx=10, pady=10)
    instruction_button.pack(padx=10, pady=10)
    quit_button.pack(padx=10, pady=10)


def display_category_page():  # vai para a parte de categorias
    logo.pack_forget()
    play_button.pack_forget()
    instruction_button.pack_forget()
    quit_button.pack_forget()

    logo.pack(padx=10, pady=15)
    category_page_title.pack(padx=10, pady=(20, 30))

    category_1_button.pack(padx=10, pady=10)
    category_2_button.pack(padx=10, pady=10)
    category_3_button.pack(padx=10, pady=(10, 30))

    back_to_menu_button.pack(padx=10, pady=10)


def display_play_page(category_name, item):  # vai para o jogo em si
    category_page_title.pack_forget()
    category_1_button.pack_forget()
    category_2_button.pack_forget()
    category_3_button.pack_forget()
    back_to_menu_button.pack_forget()

    random_item = random.choice(item)
    answer = random_item[0]
    attempts = 5
    

    if category_name == categories[0]:
        message_label = customtkinter.CTkLabel(
            window, text=f"Sou uma {category_name}", font=("Arial", 24)
        )
    else:
        message_label = customtkinter.CTkLabel(
            window, text=f"Sou um {category_name}", font=("Arial", 24)
        )
    message_label.pack(padx=10, pady=(20, 30))

    
    def check_guess():  # verifica se o usuario acertou
        nonlocal attempts
        user_input = user_guess.get()
        if user_input.lower() == answer.lower():
            fail_label.configure(text="")
            print("Acertou")
        else:
            fail_label.configure(text="Tente novamente.")
            attempts -= 1
            attempts_label.configure(text=f"{attempts}/5 Tentativas")
            if attempts == 0:
                exit_match()


    guess_frame = customtkinter.CTkFrame(window, fg_color="transparent")
    guess_frame.pack(padx=10, pady=10)

    guess_label = customtkinter.CTkLabel(guess_frame, text="Palpite")
    guess_label.pack(side="left", padx=(0, 10))

    user_guess = customtkinter.CTkEntry(guess_frame)
    user_guess.pack(side="left")

    submit_button = customtkinter.CTkButton(
        guess_frame, text="Enviar", command=check_guess
    )
    submit_button.pack(side="left", padx=(10, 0))

    attempts_label = customtkinter.CTkLabel(guess_frame, text="5/5 Tentativas")
    attempts_label.pack(side="left", padx=(10,0))

    fail_label = customtkinter.CTkLabel(window, text="", text_color="red")
    fail_label.pack(padx=10, pady=(2, 10))

    hint_label = customtkinter.CTkLabel(window, text="")
    hint_label.pack(padx=10, pady=10)

    hint_frame = customtkinter.CTkFrame(window, fg_color="transparent")
    hint_frame.pack(padx=10, pady=10)

    def show_hint(hint_index):  # exibe as dicas
        hint = random_item[hint_index]
        hint_label.configure(text=hint)

    for hint_index in range(1, 4):
        hint_button = customtkinter.CTkButton(
            hint_frame,
            text=f"Dica {hint_index}",
            command=lambda i=hint_index: show_hint(i),
        )
        hint_button.pack(side="left", padx=10, pady=10)

    

    def exit_match():
        message_label.pack_forget()
        hint_frame.pack_forget()
        guess_frame.pack_forget()
        exit_match_button.pack_forget()
        hint_label.pack_forget()
        fail_label.pack_forget()

        window.after(
            10, show_menu_buttons
        )  # Adiciona um pequeno atraso para melhorar a resposta

    def show_menu_buttons():
        play_button.pack(padx=10, pady=10)
        instruction_button.pack(padx=10, pady=10)
        quit_button.pack(padx=10, pady=10)

    exit_match_button = customtkinter.CTkButton(
        window, text="Abandonar partida", fg_color="#e60000", command=exit_match
    )
    exit_match_button.pack(padx=10, pady=10)


play_button = customtkinter.CTkButton(
    window, text="Jogar", command=display_category_page
)
play_button.pack(padx=10, pady=10)

instruction_button = customtkinter.CTkButton(window, text="Instruções")
instruction_button.pack(padx=10, pady=10)

quit_button = customtkinter.CTkButton(window, text="Sair", command=handle_exit)
quit_button.pack(padx=10, pady=10)


back_to_menu_button = customtkinter.CTkButton(
    window, text="Voltar", command=display_menu_page
)

category_1_button = customtkinter.CTkButton(  # Seleciona categoria de comidas
    window,
    text=categories[0],
    command=lambda: display_play_page(categories[0], food_items),
)
category_2_button = customtkinter.CTkButton(  # Seleciona categoria de animais
    window,
    text=categories[1],
    command=lambda: display_play_page(categories[1], animal_items),
)
category_3_button = customtkinter.CTkButton(  # Seleciona categoria de objetos
    window,
    text=categories[2],
    command=lambda: display_play_page(categories[2], object_items),
)

window.mainloop()
