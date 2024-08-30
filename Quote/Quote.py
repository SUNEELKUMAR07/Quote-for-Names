import hashlib

quotes = {
    "emotional": [
        "Together, you are the light that shines through the darkest nights.",
        "Your bond is written in the stars, destined by the gods.",
        "Like Rama and Sita, your love is an epic story of devotion and strength.",
        "Your connection transcends time, a love story foretold by the universe."
    ],
    "funny": [
        "You two are like Shiva and Parvati, except with more Netflix and fewer tigers!",
        "Together, you're the dynamic duo that even Hanuman would take a selfie with!",
        "If love were a myth, you'd be the punchline of a godly joke!",
        "You're like the sun and moon—always chasing each other but never apart."
    ]
}
def generate_hash(name1, name2):
    combined = name1.lower() + name2.lower()
    return hashlib.md5(combined.encode()).hexdigest()
def select_quote(name1, name2):
    hash_value = generate_hash(name1, name2)
    # Select quotes based on the first byte of the hash
    emotion_index = int(hash_value[0], 16) % len(quotes["emotional"])
    funny_index = int(hash_value[1], 16) % len(quotes["funny"])

    return quotes["emotional"][emotion_index], quotes["funny"][funny_index]
def get_quote(name1, name2):
    if (name1.lower() == "suneel kumar" and name2.lower() == "muni charitha") or (name1.lower() == "muni charitha" and name2.lower() == "suneel kumar"):
        return ("Your bond is written in the stars, destined by the gods.",
                "Together, you're the dynamic duo that even Hanuman would take a selfie with!")
    emotional_quote, funny_quote = select_quote(name1, name2)
    return emotional_quote, funny_quote
boy_name = input("Enter the boy's name: ")
girl_name = input("Enter the girl's name: ")

emotional, funny = get_quote(boy_name, girl_name)

print("\nEmotional Quote:")
print(emotional)

print("\nFunny Quote:")
print(funny)
