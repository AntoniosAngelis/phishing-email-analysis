email_text = input("Paste the email content:\n")

warnings = []

phishing_keywords = [
    "urgent",
    "verify your account",
    "click here",
    "login now",
    "password",
    "bank",
    "suspended",
    "limited time"
]

for word in phishing_keywords:
    if word.lower() in email_text.lower():
        warnings.append(f"Suspicious keyword detected: '{word}'")


if "http://" in email_text or "https://" in email_text:
    warnings.append("Email contains a link - verify carefully")


if email_text.isupper():
    warnings.append("Email uses all caps - suspicious")


print("\nAnalysis Result:\n")

if warnings:
    print(" Potential phishing email detected!\n")
    for w in warnings:
        print(f"- {w}")
else:
    print(" No obvious phishing indicators found.")