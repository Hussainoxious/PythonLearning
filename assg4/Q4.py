import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9]+)*[\.a-zA-Z]$'
    if re.match(pattern, email):
        return True
    else:
        return False

if __name__ == "__main__":
    email_addresses = [
        "nsommer@wooster.edu",
        "n.sommer@cs.wooster.edu",
        "yippee_skippy@yee-haw.wheeeee",
        "fun-times@Taylor.hall.wooster.edu",
        "n@sommer@wooster.edu",
        "n sommer@wooster.edu",
        "nsommer@wooster..edu",
        "nsommer@wooster.edu-org",
    ]

    for email in email_addresses:
        if validate_email(email):
            print(f"[{email}] is a VALID email address.")
        else:
            print(f"[{email}] is an INVALID email address.")