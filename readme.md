# Jogo de Batalha RPG - Código Python - (https://github.com/gabrieltiberio)

### Descrição:
Este é um jogo de batalha RPG simples desenvolvido em Python. O jogador luta contra uma série de NPCs (orcs) em batalhas sequenciais. O objetivo é vencer um número específico de batalhas para ganhar o jogo. O código inclui a criação e gerenciamento de jogadores e NPCs, mecânicas de batalha, e evolução do jogador conforme ganha experiência.

### Funcionalidades:
- Criação e personalização do jogador, incluindo nome, nível, pontos de vida (HP) e dano.
- Geração de NPCs (orcs) com atributos variados e aleatórios.
- Sistema de batalha onde o jogador e os NPCs se atacam até que um dos lados seja derrotado.
- Sistema de experiência (EXP) e evolução do jogador com aumento de nível, HP máximo e dano.
- Exibição clara e colorida das informações do jogador e dos NPCs durante o jogo.

### Bibliotecas Utilizadas:
- `random`: Para gerar valores aleatórios para atributos dos NPCs.
- `colorama`: Para adicionar cores ao texto exibido no terminal, melhorando a legibilidade.

### Como Jogar:
1. Execute o script e insira o nome do jogador quando solicitado.
2. O jogo inicia e o jogador enfrenta 5 batalhas contra NPCs.
3. O objetivo é vencer pelo menos 4 batalhas para ganhar o jogo.
4. O status do jogador e dos NPCs é exibido após cada batalha, incluindo HP, dano e EXP.

### Autor:
Gabriel Tibério  
GitHub: [https://github.com/gabrieltiberio](https://github.com/gabrieltiberio)

### Data:
12/09/2024

### Versão:
1.1

---

# RPG Battle Game - Python Code - (https://github.com/gabrieltiberio)

### Description:
This is a simple RPG battle game developed in Python. The player fights against a series of NPCs (orcs) in sequential battles. The goal is to win a specific number of battles to win the game. The code includes creating and managing players and NPCs, battle mechanics, and evolving the player as they gain experience.

### Features:
- Player creation and customization, including name, level, health points (HP), and damage.
- NPC (orcs) generation with varied and random attributes.
- Battle system where the player and NPCs attack each other until one side is defeated.
- Experience (EXP) system and player evolution, increasing level, max HP, and damage.
- Clear and colorful display of player and NPC information during the game.

### Libraries Used:
- `random`: For generating random values for NPC attributes.
- `colorama`: To add color to the text displayed in the terminal, enhancing readability.

### How to Play:
1. Run the script and enter the player's name when prompted.
2. The game begins, and the player faces 5 battles against NPCs.
3. The goal is to win at least 4 battles to win the game.
4. The status of the player and NPCs is displayed after each battle, including HP, damage, and EXP.

### Author:
Gabriel Lourenço Tibério  
GitHub: [https://github.com/gabrieltiberio](https://github.com/gabrieltiberio)

### Date:
September 12, 2024

### Version:
1.1

---

## Mudanças Técnicas / Technical Changes

### Simplificação das Funções de Reset e Exibição:
As funções que resetam e exibem o HP do jogador e do NPC foram otimizadas, removendo repetições e organizando melhor a lógica, o que diminui a duplicação de código e facilita a manutenção.
- **Simplification of Reset and Display Functions:** The functions for resetting and displaying player and NPC HP were optimized by removing redundancies and improving the logic, reducing code duplication and making maintenance easier.

### Estruturação Mais Clara e Linear:
A lógica do jogo foi reorganizada de forma mais linear, separando funções de controle (como a batalha) de funções auxiliares (como resetar HP e exibir status), o que melhora a legibilidade e o fluxo do código.
- **Clearer and More Linear Structure:** The game logic was reorganized to be more linear, with a clear separation between control functions (like battles) and helper functions (such as resetting HP and displaying status), improving code readability and flow.

### Remoção de Comentários Redundantes:
Comentários explicando trechos óbvios ou triviais foram removidos, deixando apenas explicações essenciais, o que reduz a poluição visual e facilita a leitura do código.
- **Removal of Redundant Comments:** Comments that explained obvious or trivial parts of the code were removed, leaving only essential explanations, reducing visual clutter and improving code readability.

### Melhoria na Exibição de Informações:
A exibição dos status do jogador e do NPC foi simplificada para ser mais clara e sem duplicações de lógica. O uso da biblioteca colorama foi mantido para garantir uma visualização colorida e organizada.
- **Improved Information Display:** The display of player and NPC status was simplified to be clearer and avoid logic duplication. The use of the colorama library was kept to ensure clear and colorful visual organization.

### Organização e Modularidade:
O código foi reestruturado para ser mais modular, com funções reutilizáveis e menos redundância, tornando mais fácil a compreensão e futura expansão do projeto.
- **Better Organization and Modularity:** The code was reorganized to be more modular, with reusable functions and less redundancy, making it easier to understand and expand the project in the future.
