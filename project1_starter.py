COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Jared Raysor
Date: 10/27/2025

AI Usage: AI helped with file I/O error handling logic, stat formula design, and level-up implementation.
"""

# ============================================
# Character Creation & Stat Calculation
# ============================================

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    Returns: tuple of (strength, magic, health)
    """

    # Stat formulas per class (custom but consistent)
    class_data = {
        "Warrior": {"str_base": 10, "mag_base": 2, "hp_base": 120, "str_growth": 5, "mag_growth": 1, "hp_growth": 20},
        "Mage": {"str_base": 3, "mag_base": 10, "hp_base": 80, "str_growth": 1, "mag_growth": 5, "hp_growth": 10},
        "Rogue": {"str_base": 7, "mag_base": 5, "hp_base": 90, "str_growth": 3, "mag_growth": 2, "hp_growth": 15},
        "Cleric": {"str_base": 5, "mag_base": 8, "hp_base": 100, "str_growth": 2, "mag_growth": 4, "hp_growth": 18},
    }

    if character_class not in class_data:
        return None  # Invalid class name

    stats = class_data[character_class]
    strength = stats["str_base"] + stats["str_growth"] * (level - 1)
    magic = stats["mag_base"] + stats["mag_growth"] * (level - 1)
    health = stats["hp_base"] + stats["hp_growth"] * (level - 1)

    return strength, magic, health


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """

    level = 1
    gold = 100

    stats = calculate_stats(character_class, level)
    if stats is None:
        print("Error: Invalid character class. Choose from Warrior, Mage, Rogue, or Cleric.")
        return None

    strength, magic, health = stats

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return character


# ============================================
# File Saving / Loading
# ============================================

def save_character(character, filename):
    """
    Saves character to text file in specific format.
    Returns: True if successful, False if error occurred.
    """

    try:
        with open(filename, "w") as f:
            f.write(f"Character Name: {character['name']}\n")
            f.write(f"Class: {character['class']}\n")
            f.write(f"Level: {character['level']}\n")
            f.write(f"Strength: {character['strength']}\n")
            f.write(f"Magic: {character['magic']}\n")
            f.write(f"Health: {character['health']}\n")
            f.write(f"Gold: {character['gold']}\n")
        return True

    except PermissionError:
        print("Error: Permission denied when trying to save the file.")
        return False
    except Exception as e:
        print(f"Unexpected error while saving: {e}")
        return False


def load_character(filename):
    """
    Loads character from text file.
    Returns: character dictionary if successful, None if file not found.
    """

    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        char = {}
        for line in lines:
            if ": " in line:
                key, value = line.strip().split(": ", 1)
                key = key.lower().replace(" ", "_")  # e.g., "Character Name" → "character_name"
                char[key.split("_")[-1]] = value

        # Convert numeric values
        char["level"] = int(char["level"])
        char["strength"] = int(char["strength"])
        char["magic"] = int(char["magic"])
        char["health"] = int(char["health"])
        char["gold"] = int(char["gold"])

        return char

    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error loading character: {e}")
        return None


# ============================================
# Display & Level-Up
# ============================================

def display_character(character):
    """
    Prints formatted character sheet.
    """

    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


def level_up(character):
    """
    Increases character level and recalculates stats.
    Modifies the character dictionary directly.
    """

    character["level"] += 1
    new_stats = calculate_stats(character["class"], character["level"])
    if new_stats:
        character["strength"], character["magic"], character["health"] = new_stats


# ============================================
# Testing Section (optional)
# ============================================

if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")

    char = create_character("Aria", "Mage")
    if char:
        display_character(char)

        if save_character(char, "aria.txt"):
            print("\nCharacter saved successfully!")

        loaded = load_character("aria.txt")
        if loaded:
            print("\nLoaded Character:")
            display_character(loaded)

            level_up(loaded)
            print("\nAfter Level Up:")
            display_character(loaded)


