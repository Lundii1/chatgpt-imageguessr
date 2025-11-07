# 🎨 ChatGPT Image Guessr

A simple and fun terminal game that generates AI images using OpenAI’s API — your goal is to **guess the original prompt**.
Each correct answer increases your score… but one wrong guess ends it all!

---

## 🧠 What It Does

* 🎲 Picks a random word from a built-in list
* 🖼️ Uses OpenAI’s Image API to generate a picture
* 🕹️ Displays the image and asks you to guess the word
* 🧮 Tracks your score — ends on the first mistake
* ♻️ Lets you restart after each round

---

## ⚙️ Requirements

### 🧰 You’ll Need

* **Python** `3.8+`
* **OpenAI API key**
* **Libraries:** `openai`, `matplotlib`, `pillow`

### 💾 Install Dependencies

`pip install openai matplotlib pillow`

---

## 🔧 Setup

### 1. Clone the Repository

`git clone https://github.com/Lundii1/chatgpt-imageguessr`
`cd chatgpt-imageguessr`

### 2. Add Your OpenAI API Key

**Option A — Environment Variable (recommended)**
`export OPENAI_API_KEY="your_api_key_here"` (macOS/Linux)
`$env:OPENAI_API_KEY="your_api_key_here"` (Windows PowerShell)

Then in your code:
`openai.api_key = os.getenv("OPENAI_API_KEY")`

**Option B — Hardcode (not recommended)**
`openai.api_key = "your_api_key_here"`

---

## ▶️ How to Play

Run the game:
`python program.py`

### 🕹️ Game Flow

1. The script prints **“Loading…”** and generates an image.
2. The image opens in a pop-up window.
3. Type your guess in the terminal.
4. If correct → +1 point, new image!
5. If wrong → Game over, the answer is revealed.
6. Type **“yes”** to play again.

---

## 🎨 Customization

**🖼️ Change Image Size**
`size="512x512"`  — try `1024x1024` for higher quality

**✏️ Edit or Add Prompts**
Modify the `dictionnary` list at the top of the script.

**🔁 Fix Restart Command**
Replace
`os.system("program.py")`
with
`import sys`
`os.system(f"{sys.executable} {__file__}")`

---
