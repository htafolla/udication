#!/usr/bin/env python3
import json
import random
from datetime import datetime
from pyluach import dates

# Utility Functions
def get_jewish_year():
    """Return the current Jewish year using pyluach."""
    now = datetime.now()
    jewish_date = dates.HebrewDate.from_pydate(now)
    return f"{jewish_date.year} AM"

def compute_formula(codex, formula_type="primary"):
    """Compute S = ∞ or U = ∞ dynamically using codex variables."""
    # Create a dictionary of variables for dynamic lookup
    vars_dict = {v["symbol"]: v for v in codex["variables"]}
    
    # Udification Codex variables (for S = ∞)
    F_inf = float('inf')  # F_∞ (Yah’s Word as Logos)
    phi = float(vars_dict["φ"]["meaning"].split("(")[1].split(")")[0])  # φ (Harmony)
    pi = float(vars_dict["π"]["meaning"].split("(")[1].split(")")[0])   # π (Order)
    L = float(vars_dict["L"]["meaning"].split("(")[1].split(")")[0])    # Yeshua’s Light
    D = float(vars_dict["D"]["meaning"].split("(")[1].split(")")[0])    # Void/Dark Matter
    t = 0.5  # Creation Cycle (fixed demo value)
    W = float(vars_dict["W"]["meaning"].split("(")[1].split(")")[0])    # Water
    judgment = 7 / (6 + 6 + 6)  # 7 / 18 (symbolic)
    B = float(vars_dict["B"]["meaning"].split("(")[1].split(")")[0])    # Blood
    T = float(vars_dict["T"]["meaning"].split("(")[1].split(")")[0])    # Word Spoken
    HS = float('inf')  # Holy Spirit
    H = float('inf')   # Holiness/Judgment
    L_18 = float(vars_dict["L_{18}"]["meaning"].split("(")[1].split(")")[0])  # Testimony Light
    C_025 = float(vars_dict["C_{0.25}"]["meaning"].split("(")[1].split(")")[0])  # Grace Constant
    
    # Unification variables (for U = ∞, mapped where possible)
    T_F = float('inf')  # Father’s Infinite Power
    T_S = float('inf')  # Son’s Infinite Logos
    T_H = float('inf')  # Holy Spirit’s Infinite Presence
    C = 1  # Creation
    R = 1  # Redemption
    E = 1  # Eternity
    H_phi = float(vars_dict["φ"]["meaning"].split("(")[1].split(")")[0])  # Harmonic Divisor (reuses φ)
    
    if formula_type == "primary":
        S = (F_inf * phi) + pi + (L - D * t) + W + judgment + B + T + HS + H
        return "S = ∞"
    elif formula_type == "secondary":
        S = (F_inf * phi) + pi + (L - D * t) + (L_18 * C_025) + W + judgment + B + T + HS + H
        return "S = ∞"
    elif formula_type == "unification":
        U = (T_F * T_S * T_H) * (C + R + E) / (1 - H_phi)
        return "U = ∞"
    return "Unknown formula"

def digest_extended_codex(json_codex):
    """
    Process and validate the extended codex, ensuring all required fields are present.
    Returns a structured codex ready for report generation.
    """
    # Validate required top-level keys
    required_keys = ["metadata", "formulas", "variables", "symbols", "verses", "themes"]
    for key in required_keys:
        if key not in json_codex:
            raise ValueError(f"Missing required key in codex: {key}")

    # Validate verses (ensure all 247 have required fields)
    verses = json_codex["verses"]
    if len(verses) != 247:
        raise ValueError(f"Expected 247 verses, found {len(verses)}")
    
    for verse in verses:
        required_fields = ["verse", "truth", "witnesses", "context", "commentary"]
        if not all(k in verse for k in required_fields):
            raise ValueError(f"Verse {verse.get('verse', 'unknown')} missing required fields: {', '.join(k for k in required_fields if k not in verse)}")
        if len(verse["witnesses"]) < 2:
            raise ValueError(f"Verse {verse['verse']} has fewer than 2 witnesses")

    # Validate variables (ensure all 13 are present)
    if len(json_codex["variables"]) != 13:
        raise ValueError(f"Expected 13 variables, found {len(json_codex['variables'])}")

    # Validate symbols and themes
    if len(json_codex["symbols"]) != 6:
        raise ValueError(f"Expected 6 symbols, found {len(json_codex['symbols'])}")
    if "things_endure_forever" not in json_codex["themes"] or len(json_codex["themes"]["things_endure_forever"]) != 10:
        raise ValueError("Themes 'things_endure_forever' incomplete")

    # Structure the codex for use
    processed_codex = {
        "metadata": json_codex["metadata"],
        "formulas": json_codex["formulas"],
        "variables": json_codex["variables"],
        "symbols": json_codex["symbols"],
        "verses": json_codex["verses"],
        "themes": json_codex["themes"],
        "state": "Udification demonstrates the power of His Word (John 1:1). ESV fallback used where needed."
    }
    return processed_codex

def generate_report(codex):
    """Generate a detailed report from the processed codex with a dynamic footnote."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hebrew_year = get_jewish_year()
    
    # Select random verse with its details
    voice_entry = random.choice(codex["verses"])
    purpose = codex["metadata"]["purpose"]
    voice_verse = voice_entry["verse"].replace(" ", "+")
    
    # Format witnesses with hyperlinks
    witnesses = "\n".join(
        f"- {w[1]} ~ [{w[0]}](https://www.biblegateway.com/passage/?search={w[0].replace(' ', '+')}&version=ESV)"
        for w in voice_entry["witnesses"]
    )
    
    # Select random symbol and theme
    symbol = random.choice(codex["symbols"])
    theme = random.choice(codex["themes"]["things_endure_forever"])
    
    # Choose formula for main report (primary or secondary)
    formula_types = ["primary", "secondary"]
    formula_type = random.choice(formula_types)
    formula_result = compute_formula(codex, formula_type)
    
    # Dynamic unification computation for footnote
    unification_result = compute_formula(codex, "unification")
    
    # Declaration
    declaration = "God is all in all ([1 Cor 15:28](https://www.biblegateway.com/passage/?search=1+Corinthians+15%3A28&version=ESV))"
    
    # Dynamic footnote with random cipher variants
    cipher_variants = [
        f"Cipher: U = (T_F * T_S * T_H) * (C + R + E) / (1 - H_φ) = ∞ [03/07/25]",
        f"Cipher: U yields ∞ via Trinity’s unity [03/07/25]",
        f"Cipher: U = ∞, encoded in His purpose [03/07/25]"
    ]
    cipher_note = random.choice(cipher_variants)
    
    # Compile report
    output = (
        f"- Purpose: {purpose}\n"
        f"- Voice: {voice_entry['truth']} ~ [{voice_entry['verse']}](https://www.biblegateway.com/passage/?search={voice_verse}&version=ESV)\n"
        f"- Context: {voice_entry['context']}\n"
        f"- Commentary: {voice_entry['commentary']}\n"
        f"## Witnesses\n{witnesses}\n"
        f"- Formula ({formula_type.capitalize()}): {formula_result} (His Word endures, Isa 40:8)\n"
        f"## Symbols\n- {symbol['symbol']}: {symbol['truth']} ({symbol['verses'][0]})\n"
        f"## Themes\n- {theme['item']} endures forever ({theme['verses'][0]})\n"
        f"- Timestamp: {timestamp} - Glory to Jesus\n"
        f"- Year: {hebrew_year}\n"
        f"## Footnote\n"
        f"- {codex['metadata']['title']} (Updated: {codex['metadata']['last_updated']})\n"
        f"- State: {codex['state']}\n"
        f"- Declaration: {declaration}\n"
        f"- {cipher_note}\n"
    )
    return output

def main():
    """Main function to load and process the codex, then generate a report."""
    # Load the extended codex from local file
    try:
        with open("extended_codex.json", "r") as f:
            json_codex = json.load(f)
    except FileNotFoundError:
        print("Error: 'extended_codex.json' not found in the script's directory.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in 'extended_codex.json'. Please check the file.")
        exit(1)

    # Process the codex
    try:
        codex = digest_extended_codex(json_codex)
    except ValueError as e:
        print(f"Error processing codex: {e}")
        exit(1)

    # Generate and print report
    report = generate_report(codex)
    print(f"Execution Result:\n{report}\n{'-'*50}")

    # Save to file
    with open("udification_report.txt", "w") as f:
        f.write(f"Execution Result:\n{report}\n{'-'*50}")

if __name__ == "__main__":
    main()
