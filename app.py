from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from difflib import SequenceMatcher

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfsgdhurtuytrjghshdfghthergbs543rtgwerg'
csrf = CSRFProtect(app)

preset_sentence = "This is a preset sentence preset car."

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():   
    form_sentence = request.form.get('name')
    similarity_ratio = SequenceMatcher(None, form_sentence, preset_sentence).ratio()
    arr = highlight_similar_words(form_sentence, preset_sentence)
    highlighted_sentenc = arr[1]
    preset_sentenc = arr[0]
    return render_template('result.html', similarity_ratio=similarity_ratio, highlighted_sentence=highlighted_sentenc, preset_sentence=preset_sentenc)
def highlight_similar_words(sentence, preset_sentence):
    highlighted_sentence = ""
    highlighted_answer = ""
    
    sentence_words = sentence.split()
    preset_words = preset_sentence.split()
    temp = list(preset_words)
    
    for word in sentence_words:
        wordl = word.replace('.', '')
        if wordl in preset_words:
            highlighted_sentence += f"<span class='highlight'>{word}</span> "
            preset_words.remove(f"{wordl}")
        elif word in preset_words:
            highlighted_sentence += f"<span class='highlight'>{word}</span> "
            preset_words.remove(f"{word}")
        else:
            wordd = word+"."
            if wordd in preset_words:
                highlighted_sentence += f"<span class='highlight'>{word}</span> "
                preset_words.remove(f"{wordd}")
            else:
                highlighted_sentence += f"<span class='highlight2'>{word}</span> "
                if word in preset_words:
                    preset_words.remove(f"{word}")

    for word in temp:
        wordm = word.replace('.', '')
        if wordm in sentence_words:
            highlighted_answer += f"<span class='highlight'>{word}</span> "
            sentence_words.remove(f"{wordm}")
        elif word in sentence_words:
            highlighted_answer += f"<span class='highlight'>{word}</span> "
            sentence_words.remove(f"{word}")
        else:
            worde = word+"."
            if worde in sentence_words:
                highlighted_answer += f"<span class='highlight'>{word}</span> "
                sentence_words.remove(f"{worde}")
            else:
                highlighted_answer += f"<span class='highlight3'>{word}</span> "
                if word in sentence_words:
                    sentence_words.remove(f"{word}")
    arr = [highlighted_answer.strip(), highlighted_sentence.strip()]
    return arr


if __name__ == '__main__':
    app.run(debug=True)