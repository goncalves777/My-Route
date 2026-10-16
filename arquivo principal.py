import customtkinter as ctk

app = ctk.CTk()
app.title("My Routes")
app.geometry("500x500")

################################################
# SESSÃO DE FUNÇÕES
################################################
frame_atual = ctk.CTkFrame(app)
frame_atual.pack_forget()

frame_substituto = ctk.CTkFrame(app)
frame_substituto.pack()


def troca_de_frames(frame_atual, frame_substituto):

    frame_atual.pack_forget()
    frame_substituto.pack()


################################################
# FRAME PRINCIPAL
################################################
frame_principal = ctk.CTkFrame(app)
frame_principal.pack()


################################################
# FRAME DO PERFIL DO USUÁRIO
################################################
frame_perfil = ctk.CTkFrame(app)
frame_perfil.pack_forget()

nome = ctk.CTkLabel(frame_perfil, text="Nome do usuario")
nome.pack()

veiculo = ctk.CTkLabel(frame_perfil, text="Tipo de veículo: Kangoo")
veiculo.pack()

idade = ctk.CTkLabel(frame_perfil, text="Idade:24")
idade.pack()

perfil = ctk.CTkButton(
    frame_principal,
    text="Perfil",
    anchor="nw",
    command=lambda: troca_de_frames(frame_principal, frame_perfil),
)


btn = ctk.CTkButton(
    frame_perfil,
    text="voltar",
    border_color="green",
    command=lambda: troca_de_frames(frame_perfil, frame_principal),
)

btn.pack()

perfil.pack()


################################################
# FRAME (ADICIONAR ROTAS)
################################################

frame_add_rota = ctk.CTkFrame(app)
frame_add_rota.pack_forget()


btn = ctk.CTkButton(
    frame_principal,
    text="Adicionar Rota",
    border_color="green",
    command=lambda: troca_de_frames(frame_principal, frame_add_rota),
)

btn.pack()

# PLATAFORMA

combo_box = ctk.CTkComboBox(
    frame_add_rota, values=["Mercado Livre", "Shopee", "Amazon"]
)
combo_box.pack()


# DATA DA ROTA
def formatar_data(*args):
    global formatando

    if formatando:
        return

    texto = data_format.get()
    numeros = "".join(c for c in texto if c.isdigit())[:8]

    if len(numeros) > 4:
        data = numeros[:2] + "/", numeros[2:4] + "/", numeros[4:]
    elif len(numeros) > 2:
        data = numeros[:2] + "/" + numeros[2:]
    else:
        data = numeros

    if texto != data:
        formatando = True
        data_format.set(data)
        formatando = False


data_format = ctk.StringVar()
formatando = False
data_format.trace_add("write", formatar_data)


data_rota = ctk.CTkEntry(
    frame_add_rota, placeholder_text="Data:", textvariable=data_format
)
data_rota.pack()

# PACOTES

quantidade_pacotes = ctk.CTkEntry(frame_add_rota, placeholder_text="Pacotes:")
quantidade_pacotes.pack()

# QUILOMETRAGEM

quilometragem = ctk.CTkEntry(frame_add_rota, placeholder_text="kms percorridos:")
quilometragem.pack()

# VALOR FINAL DA ROTA


valor_final = ctk.CTkEntry(frame_add_rota, placeholder_text="Valor final:")
valor_final.pack()


def salvar_rota():
    print("Rota salva com sucesso!!!")


btn = ctk.CTkButton(
    frame_add_rota,
    text="Salvar Rota",
    border_color="green",
    command=lambda: salvar_rota(),
)

btn.pack()


btn = ctk.CTkButton(
    frame_add_rota,
    text="voltar",
    border_color="green",
    command=lambda: troca_de_frames(frame_add_rota, frame_principal),
)

btn.pack()


app.mainloop()

# Commit de alteração
