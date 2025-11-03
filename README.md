# 👋🏻 Leonardo de Moura Fuseti

Estudante de Defesa Cibernetica no Polo Estacio Piumhi MG . Formação tecnica em Tecnico em Redes de Computadores no IFMG Bambui MG , intusiasta na programação gostando muito de Python e evoluindo dia a dia .

### Conecte-se comigo

[![Perfil DIO](https://img.shields.io/badge/-Meu%20Perfil%20na%20DIO-30A3DC?style=for-the-badge)](https://www.dio.me/users/mourafuseti)
[![E-mail](https://img.shields.io/badge/-Email-000?style=for-the-badge&logo=microsoft-outlook&logoColor=E94D5F)](mailto:mourafuseti@gmail.com)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=30A3DC)](https://www.linkedin.com/in/leonardo-moura-fuseti-4052b0359/)

### Habilidades

![HTML](https://img.shields.io/badge/HTML-000?style=for-the-badge&logo=html5&logoColor=30A3DC)
![CSS3](https://img.shields.io/badge/CSS3-000?style=for-the-badge&logo=css3&logoColor=E94D5F)
![JavaScript](https://img.shields.io/badge/JavaScript-000?style=for-the-badge&logo=javascript&logoColor=F0DB4F)
![Sass](https://img.shields.io/badge/SASS-000?style=for-the-badge&logo=sass&logoColor=CD6799)
![Bootstrap](https://img.shields.io/badge/bootstrap-000?style=for-the-badge&logo=bootstrap&logoColor=553C7B)
[![Git](https://img.shields.io/badge/Git-000?style=for-the-badge&logo=git&logoColor=E94D5F)](https://git-scm.com/doc)
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=30A3DC)](https://docs.github.com/)

### GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=mourafuseti&theme=transparent&bg_color=000&border_color=30A3DC&show_icons=true&icon_color=30A3DC&title_color=E94D5F&text_color=FFF)

**`README.md` – PAC-MAN PROFISSIONAL (Python + Pygame)**  
**Leonardo de Moura Fuseti – 2025**

---

```markdown
# PAC-MAN – Jogo Completo em Python

> **Um Pac-Man 100% funcional, profissional e moderno**  
> **Tela cheia | Mapa gigante | Som | Vidas | Power Pellets piscando | Highscore com nome | Fantasmas aleatórios**

---

## FUNCIONALIDADES

| Recurso | Status |
|--------|--------|
| Mapa gigante 50×30 | Done |
| Tela cheia (FULLSCREEN) | Done |
| Pac-Man com boca animada | Done |
| 4 Fantasmas em posições aleatórias | Done |
| Power Pellets piscando (amarelo/branco) | Done |
| 3 Vidas (ícones no canto direito) | Done |
| Sons completos (chomp, power, morte, fantasma) | Done |
| Highscore salvo em `highscore.txt` | Done |
| Digitar nome ao vencer | Done |
| Reiniciar com `R` | Done |
| Sair com `ESC` | Done |

---

## ESTRUTURA DO PROJETO

```
pacman/
│
├── pacman.py               ← Código principal
├── highscore.txt           ← Criado automaticamente (record)
└── sounds/                 ← Sons do jogo
    ├── chomp.wav
    ├── power.wav
    ├── death.wav
    ├── ghost_eat.wav
    └── start.wav
```

---

## REQUISITOS

```bash
Python 3.8+
Pygame
```

Instale com:
```bash
pip install pygame
```

---

## COMO EXECUTAR

```bash
py -3.13 pacman.py
```

### Controles:
| Tecla | Ação |
|------|------|
| `↑ ↓ ← →` | Mover Pac-Man |
| `ENTER` | Iniciar jogo |
| `R` | Reiniciar (Game Over) |
| `ESC` | Sair |

---

## BAIXAR SONS (OBRIGATÓRIO)

> **Sem os sons, o jogo funciona, mas fica mudo.**

Baixe os arquivos WAV originais do Pac-Man aqui:  
[https://github.com/arcade-museum/pacman-sounds](https://github.com/arcade-museum/pacman-sounds)

Coloque os arquivos `.wav` dentro da pasta `sounds/`.

---

## HIGHSCORE

- O recorde é salvo em `highscore.txt`  
- Formato:  
  ```
  12500
  Leonardo
  ```

---

## CRIAR .EXE (OPCIONAL)

Transforme em executável com **PyInstaller**:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=pacman.ico pacman.py
```

> O `.exe` será gerado em `dist/pacman.exe`

---

## MAPA (50×30)

```text
1 = Parede (azul)
0 = Bolinha (branca)
2 = Power Pellet (pisca amarelo/branco)
  = Caminho vazio
```

---

## TELAS

1. **Tela Inicial**  
   - Banner + Título + Highscore  
   - `ENTER` para jogar

2. **Jogo**  
   - HUD: `SCORE` e vidas à direita  
   - Fantasmas se movem e perseguem

3. **Vitória**  
   - Digite seu nome (máx. 12 caracteres)  
   - Salva highscore se bater recorde

4. **Game Over**  
   - `R` para reiniciar

---

## AUTOR

> **Leonardo de Moura Fuseti**  
> Estudante | Desenvolvedor Python | Apaixonado por jogos retrô

---

## LICENÇA

**MIT License** – Livre para uso, modificação e distribuição.

> **Divirta-se!**  
