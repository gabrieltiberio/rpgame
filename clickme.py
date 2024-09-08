import random
from colorama import Fore, Style

# Função para obter o idioma do jogo / Function to get the game language
def escolher_idioma():
    while True:
        escolha = input("Escolha o idioma / Choose your language: (P para Português / E for English): ").strip().lower()
        if escolha == 'p':
            return 'pt'
        elif escolha == 'e':
            return 'en'
        else:
            print("Por favor, digite uma letra válida! / Please enter a valid letter!")

# Define o idioma escolhido / Set the chosen language
idioma = escolher_idioma()

# Mensagens traduzidas / Translated messages
mensagens = {
    "pt": {
        "digite_nome": "Digite o nome do jogador: ",
        "npc_venceu": "O Orc venceu a batalha!!!",
        "player_venceu": "{} Venceu a batalha!!!",
        "rodada_vencida": "O {} venceu a rodada! {} de EXP!",
        "rodada_perdida": "O {} venceu a rodada!",
    },
    "en": {
        "digite_nome": "Enter player's name: ",
        "npc_venceu": "The Orc won the battle!!!",
        "player_venceu": "{} won the battle!!!",
        "rodada_vencida": "{} won the round! {} EXP!",
        "rodada_perdida": "{} won the round!",
    }
}

# Função para obter o nome do jogador / Function to get the player's name
def obter_nome_jogador():
    nome = input(mensagens[idioma]["digite_nome"])
    return nome

# Nome do jogador escolhido pelo usuário / Name chosen by the user
nome_jogador = obter_nome_jogador()
print(f"Nome do jogador definido como: {nome_jogador}")  # Verificação de depuração / Debug verification

# Dados iniciais do jogador / Player's initial stats
player = {
    "nome": nome_jogador,  # Nome do jogador obtido da entrada / Player's name from input
    "level": 1,            # Nível inicial do jogador / Initial level
    "exp": 0,              # Experiência acumulada inicial / Initial experience
    "exp_max": 30,         # Experiência necessária para subir de nível / EXP needed to level up
    "hp": 100,             # Pontos de vida atuais do jogador / Current health points
    "hp_max": 100,         # Pontos de vida máximos do jogador / Maximum health points
    "dano": 25,            # Dano causado pelo jogador / Damage dealt by the player
}

# Cria um NPC com base no nível / Creates an NPC based on level
def criar_npc(level):
    novo_npc = {
        "nome": f"Orc #{level}",                     # Nome do NPC com base no nível / NPC's name based on level
        "level": level,                             # Nível do NPC / NPC level
        "dano": random.randint(5 * level, 10 * level), # Dano do NPC, ajustado pelo nível / NPC's damage based on level
        "hp": random.randint(50 * level, 100 * level), # HP do NPC, ajustado pelo nível / NPC's health points based on level
        "hp_max": 100 * level,                      # HP máximo do NPC / NPC's maximum health points
        "exp": 7 * level,                           # EXP que o NPC concede ao ser derrotado / EXP awarded after defeating NPC
    }
    return novo_npc

# Gera uma lista de NPCs / Generates a list of NPCs
def gerar_npcs(n_npcs):
    lista_npcs = [criar_npc(x + 1) for x in range(n_npcs)]  # Cria NPCs com níveis de 1 a n_npcs / Creates NPCs with levels from 1 to n_npcs
    random.shuffle(lista_npcs)  # Embaralha a lista de NPCs para aleatoriedade / Shuffles the NPC list for randomness
    return lista_npcs

# Exibe as informações do NPC / Displays NPC information
def exibir_npc(npc):
    print(
        f"{Fore.GREEN}Nome: {npc['nome']} // "        # Nome do NPC / NPC's name
        f"Level: {npc['level']} // "                # Nível do NPC / NPC's level
        f"Dano: {npc['dano']} // "                  # Dano do NPC / NPC's damage
        f"HP: {npc['hp']} // "                     # HP atual do NPC / NPC's current health points
        f"EXP: {npc['exp']}{Style.RESET_ALL}"       # EXP concedida pelo NPC / EXP awarded by the NPC
    )

# Exibe as informações do jogador / Displays player information
def exibir_player():
    print(
        f"{Fore.BLUE}Nome: {nome_jogador} // "       # Nome do jogador / Player's name
        f"Level: {player['level']} // "            # Nível do jogador / Player's level
        f"Dano: {player['dano']} // "              # Dano do jogador / Player's damage
        f"HP: {player['hp']}/{player['hp_max']} // " # HP atual / máximo do jogador / Player's current / maximum health points
        f"EXP: {player['exp']}/{player['exp_max']}{Style.RESET_ALL}"  # EXP atual / máxima do jogador / Player's current / maximum EXP
    )

# Reseta o HP do jogador para o máximo / Resets player's health points to maximum
def reset_player():
    player["hp"] = player["hp_max"]

# Reseta o HP do NPC para o máximo / Resets NPC's health points to maximum
def reset_npc(npc):
    npc["hp"] = npc["hp_max"]

# Verifica e realiza a evolução do jogador quando atinge o máximo de EXP / Checks and performs player level-up when maximum EXP is reached
def level_up():
    if player["exp"] >= player["exp_max"]:
        player["level"] += 1                   # Aumenta o nível do jogador / Increases player's level
        player["exp"] -= player["exp_max"]     # Subtrai o EXP usado / Subtracts used EXP
        player["exp_max"] *= 2                 # Dobra o EXP necessário para o próximo nível / Doubles EXP needed for next level
        player["hp_max"] += 20                 # Aumenta o HP máximo do jogador / Increases player's maximum health points
        player["hp"] = player["hp_max"]        # Reseta o HP para o máximo / Resets health points to maximum

# Inicia uma batalha entre o jogador e um NPC / Starts a battle between player and NPC
def iniciar_batalha(npc):
    reset_player()  # Reinicia o HP do jogador / Resets player's health points
    reset_npc(npc)  # Reinicia o HP do NPC / Resets NPC's health points
    
    while player["hp"] > 0 and npc["hp"] > 0:  # Continua a batalha enquanto ambos tiverem HP positivo / Continues battle while both have positive health points
        atacar_npc(npc)  # O jogador ataca o NPC / Player attacks NPC
        if npc["hp"] <= 0:  # Verifica se o NPC foi derrotado / Checks if NPC was defeated
            return "player"  # Retorna que o jogador venceu / Returns that the player won
        atacar_player(npc)  # O NPC ataca o jogador / NPC attacks player
        exibir_info_batalha(npc)  # Exibe o estado atual da batalha / Displays current battle state

    return "npc"  # Retorna que o NPC venceu se o loop terminar / Returns that the NPC won if the loop ends

# O jogador ataca o NPC / Player attacks NPC
def atacar_npc(npc):
    npc["hp"] -= player["dano"]

# O NPC ataca o jogador / NPC attacks player
def atacar_player(npc):
    player["hp"] -= npc["dano"]

# Exibe as informações da batalha atual / Displays current battle information
def exibir_info_batalha(npc):
    print(f"{Fore.BLUE}Player: {nome_jogador} {player['hp']}/{player['hp_max']}")  # HP do jogador / Player's health points
    print(f"{Fore.GREEN}NPC: {npc['nome']}: {npc['hp']}/{npc['hp_max']}{Style.RESET_ALL}")  # HP do NPC / NPC's health points
    print("-----------------\n")

# Inicializa os pontos dos vencedores / Initializes winner points
pontos_player = 0
pontos_npc = 0

# Gera NPCs para a batalha / Generates NPCs for battle
npcs = gerar_npcs(5)
print("NPCs gerados com sucesso")  # Verificação de depuração / Debug verification

# Faz 5 batalhas / Performs 5 battles
for i in range(5):
    npc_selecionado = npcs[i % len(npcs)]  # Seleciona um NPC da lista, alternando entre eles / Selects an NPC from the list, alternating between them
    vencedor = iniciar_batalha(npc_selecionado)  # Inicia a batalha com o NPC selecionado / Starts the battle with the selected NPC

    if vencedor == "player":  # Se o jogador vencer / If the player wins
        pontos_player += 1  # Adiciona um ponto ao jogador / Adds a point to the player
        print(f"{Fore.YELLOW}" + mensagens[idioma]["rodada_vencida"].format(nome_jogador, npc_selecionado['exp']) + Style.RESET_ALL)
        player["exp"] += npc_selecionado["exp"]  # Adiciona a EXP do NPC ao jogador / Adds NPC's EXP to the player
        level_up()  # Verifica se o jogador deve evoluir / Checks if the player should level up
        exibir_player()  # Exibe o estado atual do jogador / Displays current player state
    else:  # Se o NPC vencer / If the NPC wins
        pontos_npc += 1  # Adiciona um ponto ao NPC / Adds a point to the NPC
        print(f"{Fore.RED}" + mensagens[idioma]["rodada_perdida"].format(npc_selecionado['nome']) + Style.RESET_ALL)
        exibir_npc(npc_selecionado)  # Exibe as informações do NPC vencedor / Displays the winning NPC's information

    # Verifica se algum dos lados ganhou 4 batalhas / Checks if either side has won 4 battles
    if pontos_player >= 4:
        print(f"{Fore.YELLOW}" + mensagens[idioma]["player_venceu"].format(nome_jogador) + Style.RESET_ALL)
        break  # Encerra o loop se o jogador ganhar 4 batalhas / Ends the loop if the player wins 4 battles
    elif pontos_npc >= 4:
        print(f"{Fore.RED}" + mensagens[idioma]["npc_venceu"] + Style.RESET_ALL)
        break  # Encerra o loop se o NPC ganhar 4 batalhas / Ends the loop if the NPC wins 4 battles
