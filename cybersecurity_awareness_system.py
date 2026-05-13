
print(" ETHIOPIA CYBERSECURITY AWARENESS SYSTEM ")
print("==========================================\n")

score = 0


def ask(num, question, correct, explanation):
    global score

    print("\nQuestion", num)
    print(question)

    while True:
        ans = input("Answer (a/b/c/d): ").lower().strip()

        if ans in ["a", "b", "c", "d"]:
            break
        else:
            print("⚠ Invalid input! Please type ONLY a, b, c, or d.")

    if ans == correct:
        print("✔ Good job!")
        score += 1
    else:
        print("✖ Not correct.")
        print("✔ Correct answer:", correct)

    print("💡", explanation)
    print("------------------------------------------")


# ================= QUESTIONS (20) =================

ask(1,"What is phishing?\na) Fishing\nb) Fake messages to steal data\nc) Gaming\nd) App","b",
"Phishing is when attackers trick users into giving personal information.")

ask(2,"Strong password is:\na) 123456\nb) Name\nc) Mix letters, numbers, symbols\nd) password","c",
"Strong passwords are hard to guess and protect accounts.")

ask(3,"Suspicious links:\na) Click\nb) Ignore\nc) Share\nd) Reply","b",
"They may contain malware or scams.")

ask(4,"Malware is:\na) Safe software\nb) Harmful software\nc) Browser\nd) Game","b",
"Malware damages or steals data from systems.")

ask(5,"2FA means:\na) Password\nb) Extra security step\nc) Virus\nd) WiFi","b",
"It adds an extra verification layer for security.")

ask(6,"Public WiFi is:\na) Safe\nb) Risky\nc) Private\nd) Offline","b",
"It can be easily attacked by hackers.")

ask(7,"Social engineering is:\na) Coding\nb) Tricking humans\nc) Hardware\nd) Gaming","b",
"Attackers manipulate people to get sensitive data.")

ask(8,"Email attachments:\na) Always safe\nb) May contain viruses\nc) No risk\nd) Always good","b",
"They may contain malware.")

ask(9,"Safe browsing means:\na) Any site\nb) Trusted sites only\nc) Random clicking\nd) Download all","b",
"Only use trusted websites.")

ask(10,"Antivirus is used for:\na) Gaming\nb) Protection\nc) Typing\nd) Browsing","b",
"It protects your device from malware.")

ask(11,"OTP should be:\na) Shared\nb) Secret\nc) Posted\nd) Ignored","b",
"OTP must never be shared with anyone.")

ask(12,"Software updates:\na) Useless\nb) Fix security issues\nc) Harm device\nd) Slow internet","b",
"Updates fix security vulnerabilities.")

ask(13,"Weak passwords are:\na) Safe\nb) Easy to hack\nc) Fast\nd) Secure","b",
"Weak passwords are easily guessed by attackers.")

ask(14,"Digital footprint is:\na) Shoe size\nb) Online trace\nc) Virus\nd) App","b",
"It is the trace you leave online.")

ask(15,"Ransomware:\na) Game\nb) Locks files for money\nc) Browser\nd) Antivirus","b",
"It locks data and demands payment.")

ask(16,"Same password everywhere:\na) Safe\nb) Dangerous\nc) Fast\nd) Good","b",
"If one account is hacked, others are at risk.")

ask(17,"Unknown links:\na) Safe\nb) Dangerous\nc) Fast\nd) Helpful","b",
"They may lead to scams or malware.")

ask(18,"Logging out is:\na) Useless\nb) Important\nc) Risky\nd) Optional","b",
"It prevents unauthorized access.")

ask(19,"Bank OTP should be:\na) Shared\nb) Private\nc) Posted\nd) Saved","b",
"Banks never ask for OTP.")

ask(20,"Cybersecurity helps Ethiopia by:\na) No use\nb) Protecting systems\nc) Gaming\nd) Fun","b",
"It protects national digital infrastructure.")


# ================= FINAL RESULT =================

print("\n==========================================")
print(" FINAL RESULT ")
print("==========================================")

print("Score:", score, "/20")

percentage = (score / 20) * 100
print("Percentage:", percentage, "%")

if percentage >= 85:
    print("\n🌟 Excellent! Strong cybersecurity awareness.")
    print("You are ready for advanced cybersecurity learning.")
elif percentage >= 60:
    print("\n👍 Good job!")
    print("You understand basics but need improvement.")
else:
    print("\n⚠ Keep improving!")
    print("Cybersecurity is learned step by step.")

# ================= TIPS SECTION =================

print("\n==========================================")
print(" CYBERSECURITY TIPS (IMPORTANT) ")
print("==========================================")

print("- Never share passwords or OTP with anyone")
print("- Avoid clicking unknown links or messages")
print("- Use strong and unique passwords")
print("- Always update your software and apps")
print("- Use two-factor authentication (2FA)")
print("- Be careful on public WiFi networks")
print("- Think before sharing personal information online")

print("\nThank you for completing the Ethiopia Cybersecurity Awareness System.")
