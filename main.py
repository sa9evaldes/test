from pyscript import display, document

# 1. Predefined list of club members
club_members = [
    "Juan Dela Cruz",
    "Maria Santos",
    "Jose Rizal",
    "Clara Bonifacio",
    "Alex Reyes"
]

def check_membership(event):
    # 2 & 3. Get inputs and combine them into a single full name
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    candidate_name = f"{first_name} {last_name}".strip()

    # 4. Check whether the full name is in the list (evaluates to True or False)
    is_member = candidate_name in club_members

    # 5. Display message without if/else or loops using dictionary key mapping
    messages = {
        True: f"Congratulations {candidate_name}! You are now part of the ICT club.",
        False: f"Sorry {candidate_name}, your name is not on the club membership list."
    }

    # Extract output based on the boolean result of membership check
    result_message = messages[is_member]

    # Output result to HTML
    document.getElementById("output").innerHTML = ""
    display(result_message, target="output", append=False)
