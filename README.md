# 🥊 Code Clash — Battle of Programming Languages

A full-stack Python web application where programming languages fight each other in an animated, turn-based battle arena. The winner is decided by **real-world stats, domain strengths, and special powers** — not by random chance.

![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **12 Programming Languages** — Python, Java, JavaScript, TypeScript, C, C++, C#, Go, Rust, Ruby, PHP, Swift
- **Deterministic Battle Engine** — Each language has base stats (HP, Attack, Defense, Speed) and 3 unique signature moves
- **Domain Multipliers** — Fight in AI, Web Dev, Systems Programming, or Enterprise. Each domain boosts different languages
- **Dodge / Block / Hit Mechanics** — Not every attack lands; faster languages dodge more, tankier ones block
- **Animated Combat** — GSAP-powered stick-figure fighters with sword & gun weapon swaps
- **Sound Effects** — Sword hit on every strike, gunshot on the finishing blow
- **Floating Damage Numbers** — RPG-style damage popups, round counter, and live status bar

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.13+** installed on your machine
- **pip** (comes with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Code-Clash---Battle-of-Programming-Languages.git
   cd Code-Clash---Battle-of-Programming-Languages
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**

   - **Windows (PowerShell)**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **macOS / Linux**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` file** in the project root:
   ```
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///database.db
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open your browser** and go to:
   ```
   http://127.0.0.1:5000
   ```

---

## 🎮 How to Play

1. Click **Start Battle** on the landing page
2. **Select 2 programming languages** from the grid (click to select, click again to deselect)
3. Click **Proceed to Arena**
4. **Choose a domain** (AI, Web Dev, Systems, Enterprise) — this affects who gets stat boosts
5. **Watch the battle** play out with animations, sound effects, and floating damage numbers
6. The stronger language for that domain wins!

---

## 📁 Project Structure

```
Code-Clash---Battle-of-Programming-Languages/
├── app.py                  # Flask application & routes
├── config.py               # Configuration (secret key, DB URL)
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in git)
├── .gitignore              # Git ignore rules
│
├── models/
│   └── __init__.py         # SQLAlchemy models
│
├── services/
│   └── battle_engine.py    # Stats, powers, domain multipliers, simulation
│
├── static/
│   ├── css/
│   │   └── style.css       # Global styles (neon theme, glassmorphism)
│   ├── js/
│   │   ├── main.js         # Frontend logic (selection, animations)
│   │   └── particles-config.json
│   ├── img/
│   │   ├── sword.png       # Sword weapon image
│   │   └── gun.png         # Gun weapon image
│   └── sound_effect/
│       ├── knife hit body.mp3   # Sword hit sound
│       └── gun sound.mp3       # Gunshot finishing blow
│
└── templates/
    ├── base.html           # Base template (navbar, scripts)
    ├── index.html           # Landing page
    ├── select.html          # Language selection grid
    ├── arena.html           # Domain/battlefield selection
    └── battle.html          # Animated battle arena
```

---

## ⚙️ Battle Engine

Each language has these base stats:

| Stat    | Description                        |
|---------|------------------------------------|
| HP      | Health points                      |
| Attack  | Base damage per strike             |
| Defense | Reduces incoming damage            |
| Speed   | Determines turn order & dodge rate |

**Domain multipliers** boost a language's stats when fighting in their specialty:

| Domain     | Boosted Languages              |
|------------|--------------------------------|
| AI         | Python (1.5x), C++ (1.2x)     |
| Web        | JavaScript (1.5x), TypeScript (1.4x), PHP (1.3x) |
| Systems    | C (1.5x), C++ (1.5x), Rust (1.5x) |
| Enterprise | Java (1.5x), C# (1.5x)        |

---

## 🛠️ Tech Stack

**Backend:** Python 3.13+, Flask, SQLAlchemy, SQLite

**Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, GSAP, AOS, Typed.js, Particles.js, Devicon

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
