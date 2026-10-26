from pyscript import display, document

# list of members
club_members = [
    "Osamu Dazai",
    "Atsushi Nakajima",
    "Doppo Kunikida",
    "Ranpo Edogawa",
    "Akiko Yosano",
    "Kenji Miyazawa",
    "Kyoka Izumi",
]

def check_membership(event):
    # combine outputs into name
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    candidate_name = f"{first_name}+' '+{last_name}".strip().title()

    # is the name on the list?
    is_member = candidate_name in club_members

    # display message if whether or not you are on the list
    messages = {
        True: f"Congratulations {candidate_name}! You are now part of the ADA.",
        False: f"Sorry {candidate_name}, your name is not on the list of ADA detectives."
    }

    # extract output based on the boolean result of membership check
    result_message = messages[is_member]

    # output result to html
    document.getElementById("output").innerHTML = ""
    display(result_message, target="output", append=False)
