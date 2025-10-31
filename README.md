[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21234842&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character

calculate_stats(character_class, level) - Calculate character stats

save_character(character, filename) - Save character to file

load_character(filename) - Load character from file

display_character(character) - Display character info

level_up(character) - Increase character level

# 🎭 Character Classes
Implement these character classes with unique stat distributions:


Warrior: High strength, low magic, high health

Mage: Low strength, high magic, medium health

Rogue: Medium strength, medium magic, low health

Cleric: Medium strength, high magic, high health

# 📁 Required File Format
Your save_character() function must create files in this exact format:

Character Name: [name]

Class: [class]

Level: [level]

Strength: [strength]

Magic: [magic]

Health: [health]

Gold: [gold]


# Run specific test file
python -m pytest tests/test_character_creation.py -v

# Test your main program
python project1_starter.py

GitHub Testing:

After pushing your code, check the Actions tab to see automated test results:

✅ Green checkmarks = tests passed
❌ Red X's = tests failed (click to see details)

# ⚠️ Important Notes
Protected Files

DO NOT MODIFY files in the tests/ directory

DO NOT MODIFY files in the .github/ directory

Modifying protected files will result in automatic academic integrity violation

# AI Usage Policy

✅ Allowed: AI assistance for implementation, debugging, learning

📝 Required: Document AI usage in code comments

🎯 Must be able to explain: Every line of code during interview

# 📝 Submission Checklist

 All required functions implemented
 
 Code passes all automated tests
 
 README updated with your documentation
 
 Interview scheduled and completed
 
 AI usage documented in code comments
What's Your RPG World About
My RPG world is about creating and managing a fantasy character that grows stronger over time. Players can choose a class such as Warrior, Mage, Rogue, or Cleric, each with different strengths and abilities. The program allows players to view their stats, level up, and save their progress for future adventures. It’s a mix of fantasy role-playing and programming logic that helps bring an RPG character to life through Python code.
  How the Code Works

The code is divided into clear sections:

Character Creation:

Takes in a name and class, calculates stats based on formulas for that class.

Initializes the character with level 1 and 100 gold.

Stat Calculation:

Uses a function calculate_stats() that assigns base stats and growth per level.

Stats increase automatically when the character levels up.

Saving and Loading Files:

save_character() writes the character’s details into a .txt file in a readable format.

load_character() retrieves the information and reconstructs the character.

Level-Up System:

The level_up() function increases level and recalculates stats using the class formulas.

Display:

display_character() neatly prints all the character’s information like a profile sheet.

AI Usage

AI tools were used responsibly to:

Help design stat growth formulas for each class.

Suggest better file I/O error handling and code structure.

Improve readability and organization of code sections.

All logic, structure, and testing were written and verified by the student. AI was used as a coding assistant, not as a replacement for original work.

 Design Choices

Classes: Four distinct classes to reflect different playstyles (power, magic, balance, and healing).

File Handling: Simple text format for easy reading and saving.

Scalability: Modular design — more classes or features can easily be added later.

Error Handling: Prevents crashes when invalid input or missing files occur.

User Experience: Clean print layout that mimics a character sheet.
# 🏆 Grading

Implementation (70%): Function correctness, file operations, error handling

Interview (30%): Code explanation and live coding challenge
