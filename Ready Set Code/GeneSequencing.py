# DNA Trait Decoder — For loop for each trait separately
# Each trait has its own list of codes and traits

# 1. Eye Color
eye_codes = ["ATC", "CGA", "TCG"]
eye_traits = ["Brown (dominant)", "Blue (recessive)", "Green (recessive)"]

# 2. Hair Color
hair_codes = ["ACG", "GAT", "TGC"]
hair_traits = ["Dark (dominant)", "Blonde (recessive)", "Red (recessive)"]

# 3. Freckles
freckle_codes = ["CGC", "ATT"]
freckle_traits = ["Has freckles (dominant)", "No freckles (recessive)"]

# 4. Dimples
dimple_codes = ["GAA", "TAC"]
dimple_traits = ["Has dimples (dominant)", "No dimples (recessive)"]

# 5. Handedness
hand_codes = ["ATG", "GTA"]
hand_traits = ["Right-handed (dominant)", "Left-handed (recessive)"]

# 6. Hair Type
hair_type_codes = ["TTA", "CCA", "GCC"]
hair_type_traits = ["Curly (dominant)", "Straight (recessive)", "Wavy (incomplete dominance)"]

# 7. Blood Type
blood_codes = ["AAG", "GGA", "AGA", "TTT"]
blood_traits = ["Type A", "Type B", "Type AB", "Type O"]

# Ask user to input all 7 codes at once
print("Enter your 7-gene sequence codes in order:")
print("Eye, Hair Color, Freckles, Dimples, Handedness, Hair Type, Blood Type")
print("Example: ATC ACG CGC GAA ATG TTA AAG")
codes_input = input("> ").upper().split()

if len(codes_input) != 7:
    print("Error: Please enter exactly 7 codes.")
else:
    print("\n🧬 Your Genetic Traits:")

    # Eye Color
    for i in range(len(eye_codes)):
        if codes_input[0] == eye_codes[i]:
            print("Eye Color:", eye_traits[i])
            break
    else:
        print("Eye Color: Unknown")

    # Hair Color
    for i in range(len(hair_codes)):
        if codes_input[1] == hair_codes[i]:
            print("Hair Color:", hair_traits[i])
            break
    else:
        print("Hair Color: Unknown")

    # Freckles
    for i in range(len(freckle_codes)):
        if codes_input[2] == freckle_codes[i]:
            print("Freckles:", freckle_traits[i])
            break
    else:
        print("Freckles: Unknown")

    # Dimples
    for i in range(len(dimple_codes)):
        if codes_input[3] == dimple_codes[i]:
            print("Dimples:", dimple_traits[i])
            break
    else:
        print("Dimples: Unknown")

    # Handedness
    for i in range(len(hand_codes)):
        if codes_input[4] == hand_codes[i]:
            print("Handedness:", hand_traits[i])
            break
    else:
        print("Handedness: Unknown")

    # Hair Type
    for i in range(len(hair_type_codes)):
        if codes_input[5] == hair_type_codes[i]:
            print("Hair Type:", hair_type_traits[i])
            break
    else:
        print("Hair Type: Unknown")

    # Blood Type
    for i in range(len(blood_codes)):
        if codes_input[6] == blood_codes[i]:
            print("Blood Type:", blood_traits[i])
            break
    else:
        print("Blood Type: Unknown")
