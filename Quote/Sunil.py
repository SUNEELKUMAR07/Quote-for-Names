from flask import Flask, request, jsonify, render_template_string
import hashlib

app = Flask(__name__)

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
    emotion_index = int(hash_value[0], 16) % len(quotes["emotional"])
    funny_index = int(hash_value[1], 16) % len(quotes["funny"])
    
    if int(hash_value[2], 16) % 2 == 0:
        return quotes["emotional"][emotion_index]
    else:
        return quotes["funny"][funny_index]


@app.route('/')
def home():
    with open('Quote.html') as f:
        return render_template_string(f.read())

@app.route('/generate-quote', methods=['GET'])
def generate_quote():
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    if not name1 or not name2:
        return jsonify({'quote': 'Please provide both names.'})
    
    quote = select_quote(name1, name2)
    return jsonify({'quote': quote})

if __name__ == '__main__':
    app.run(debug=True)
