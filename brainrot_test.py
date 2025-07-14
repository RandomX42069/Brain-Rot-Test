result = []
answers = []
score = 0

brainrot_answers = [
    "fanum tax", "skibidi toilet", "quangle dingle", "gyat", "final boss",
    "capitalism", "sussy", "im gonna touch you", "sybau", "ts", "pmo", "damn is"
]

questions = [
    "What is 6 + 3?: ",
    "How are you?: ",
    "Have you ever gone through a test?: ",
    "What do you think about brainrot?: ",
    "What do you think about skibidi toilets?: "
]

for i, q in enumerate(questions):
    ans = input(q).lower()
    
    if i == 0:
        if ans in brainrot_answers:
            result.append("Q1: Brainrotted")
            score += 1
        elif ans == "9" or ans == 9:
            result.append("Q1: Normal")
        else:
            result.append("Q1: Wrong")
        answers.append(f"Q1 Answer: {ans}")
    else:
        if ans in brainrot_answers:
            label = "Brainrotted"
            score += 1
        else:
            label = "Normal"
        result.append(f"Q{i+1}: {label}")
        answers.append(f"Q{i+1} Answer: {ans}")

print("\n📊 Here is your result and answers:")
print("Diagnosis:", result)
print("Responses:", answers)
print(f"🧠 Brainrot Score: {score}/5")

# Tiered intervention messages
if score >= 5:
    print("🚨 YOUR BRAIN IS SEVERELY DAMAGED. UNINSTALL TikTok NOW. Step away from all devices. Go touch grass and drink water.")
elif score >= 3:
    print("⚠️ You are infected with SEVERE brainrot. Avoid all Skibidi content and TikTok for 72 hours. Seek reality immediately.")
elif score == 2:
    print("⚠️ Early signs of brainrot detected. You are still recoverable — avoid meme slop and focus on critical thinking.")
elif score == 1:
    print("🟡 Minor brainrot. Be cautious. Limit meme exposure.")
else:
    print("✅ You are brainrot-free. Stay sharp, king/queen.")
