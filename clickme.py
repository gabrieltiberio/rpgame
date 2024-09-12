import random
from colorama import Fore, Style

# Função que solicita e define o idioma do jogo (linhas 9-15)
def escolher_idioma():
    while True:
        escolha = input("Escolha o idioma (P para Português / E for English): ").strip().lower()
        if escolha in ['p', 'e']:
            return 'pt' if escolha == 'p' else 'en'  # Retorna 'pt' ou 'en'
        print("Por favor, digite uma letra válida!")

idioma = escolher_idioma()  # Define o idioma baseado na escolha do usuário (linha 17)

# Mensagens que mudam conforme o idioma escolhido (linha 19-35)
mensagens = {
    "pt": {
        "digite_nome": "Digite o nome do jogador: ",
        "npc_venceu": "O Orc venceu a batalha!!!",
        "player_venceu": "{} Venceu a batalha!!!",
        "rodada_vencida": "{} venceu a rodada! {} de EXP!",
        "rodada_perdida": "{} venceu a rodada!",
    },
    "en": {
        "digite_nome": "Enter player's name: ",
        "npc_venceu": "The Orc won the battle!!!",
        "player_venceu": "{} won the battle!!!",
        "rodada_vencida": "{} won the round! {} EXP!",
        "rodada_perdida": "{} won the round!",
    }
}

# Solicita e armazena o nome do jogador (linha 37-39)
nome_jogador = input(mensagens[idioma]["digite_nome"])
print(f"Nome do jogador definido como: {nome_jogador}")

# Dados iniciais do jogador (linha 41-48)
player = {
    "nome": nome_jogador,
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "dano": 25,
}

# Função que cria NPCs com base no nível (linha 50-56)
def criar_npc(level):
    return {
        "nome": f"Orc #{level}",
        "level": level,
        "dano": random.randint(5 * level, 10 * level),  # Dano do NPC depende do nível
        "hp": random.randint(50 * level, 100 * level),  # HP do NPC depende do nível
        "hp_max": 100 * level,
        "exp": 7 * level,
    }

# Gera uma lista de NPCs e embaralha para batalhas (linha 58-62)
def gerar_npcs(n_npcs):
    npcs = [criar_npc(x + 1) for x in range(n_npcs)]  # Cria n NPCs
    random.shuffle(npcs)  # Embaralha os NPCs
    return npcs

# Exibe as informações do jogador ou NPC (linha 64-68)
def exibir_dados(entidade, tipo="player"):
    cor = Fore.BLUE if tipo == "player" else Fore.GREEN  # Cor diferente para jogador e NPC
    print(f"{cor}Nome: {entidade['nome']} // Level: {entidade['level']} // Dano: {entidade['dano']} // HP: {entidade['hp']}/{entidade['hp_max']}{Style.RESET_ALL}")

# Reseta o HP de qualquer entidade (jogador ou NPC) para o máximo (linha 70-71)
def reset_hp(entidade):
    entidade["hp"] = entidade["hp_max"]

# Aumenta o nível do jogador se o EXP máximo for atingido (linha 73-80)
def level_up():
    if player["exp"] >= player["exp_max"]:
        player["level"] += 1  # Aumenta o nível
        player["exp"] -= player["exp_max"]  # Reseta o EXP
        player["exp_max"] *= 2  # Dobra o valor de EXP necessário para o próximo nível
        player["hp_max"] += 20  # Aumenta o HP máximo
        reset_hp(player)  # Reseta o HP do jogador

# Função que inicia a batalha entre o jogador e o NPC (linha 82-92)
def iniciar_batalha(npc):
    reset_hp(player)  # Reinicia o HP do jogador
    reset_hp(npc)     # Reinicia o HP do NPC
    
    while player["hp"] > 0 and npc["hp"] > 0:  # Loop até que alguém vença
        npc["hp"] -= player["dano"]  # O jogador ataca o NPC
        if npc["hp"] <= 0:  # Se o NPC foi derrotado, o jogador vence
            return "player"
        player["hp"] -= npc["dano"]  # O NPC ataca o jogador
        exibir_dados(player)  # Exibe o estado do jogador
        exibir_dados(npc, "npc")  # Exibe o estado do NPC
    return "npc"  # Se o jogador perder, o NPC vence

# Variáveis para contar as vitórias de jogador e NPC (linha 94-95)
pontos_player = 0
pontos_npc = 0

# Gera 5 NPCs para batalhas (linha 97-98)
npcs = gerar_npcs(5)

# Loop para realizar 5 batalhas (linha 100-119)
for i in range(5):
    npc_selecionado = npcs[i % len(npcs)]  # Seleciona um NPC da lista
    vencedor = iniciar_batalha(npc_selecionado)  # Inicia a batalha com o NPC

    if vencedor == "player":  # Se o jogador venceu
        pontos_player += 1
        print(f"{Fore.YELLOW}" + mensagens[idioma]["rodada_vencida"].format(nome_jogador, npc_selecionado['exp']) + Style.RESET_ALL)
        player["exp"] += npc_selecionado["exp"]  # O jogador ganha a EXP do NPC
        level_up()  # Verifica se o jogador sobe de nível
        exibir_dados(player)  # Exibe as informações do jogador
    else:  # Se o NPC venceu
        pontos_npc += 1
        print(f"{Fore.RED}" + mensagens[idioma]["rodada_perdida"].format(npc_selecionado['nome']) + Style.RESET_ALL)
        exibir_dados(npc_selecionado, "npc")  # Exibe as informações do NPC

    # Verifica se algum lado venceu 4 batalhas (linha 120-125)
    if pontos_player >= 4:  # Jogador vence
        print(f"{Fore.YELLOW}" + mensagens[idioma]["player_venceu"].format(nome_jogador) + Style.RESET_ALL)
        break
    elif pontos_npc >= 4:  # NPC vence
        print(f"{Fore.RED}" + mensagens[idioma]["npc_venceu"] + Style.RESET_ALL)
        break
        
