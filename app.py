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
    
    preset_words = preset_sentence.split()
    temp = list(preset_words)

    for word in sentence.split():
        if word.replace('.','').upper() in preset_sentence.replace('.','').upper():
            highlighted_sentence += f"<span class='highlight'>{word}</span> "
        else:
            highlighted_sentence += f"<span class='highlight2'>{word}</span> "
              
    for word in preset_sentence.split():
        if word.replace('.','').upper() in sentence.replace('.','').upper():
            highlighted_answer += f"<span class='highlight'>{word}</span> "
        else:
            highlighted_answer += f"<span class='highlight3'>{word}</span> "

    # for word in temp:
    #     wordm = word.replace('.', '')
    #     llword = word.lower()
    #     cccword = word.capitalize()
    #     if wordm in sentence_words:
    #         highlighted_answer += f"<span class='highlight'>{word}</span> "
    #         sentence_words.remove(f"{wordm}")
    #     elif word in sentence_words:
    #         highlighted_answer += f"<span class='highlight'>{word}</span> "
    #         sentence_words.remove(f"{word}")
    #     elif llword in sentence_words:
    #         highlighted_answer += f"<span class='highlight'>{word}</span> "
    #         sentence_words.remove(f"{llword}")
    #     elif cccword in sentence_words:
    #         highlighted_answer += f"<span class='highlight'>{word}</span> "
    #         sentence_words.remove(f"{cccword}")
    #     else:
    #         worde = word+"."
    #         if worde in sentence_words:
    #             highlighted_answer += f"<span class='highlight'>{word}</span> "
    #             sentence_words.remove(f"{worde}")
    #         else:
    #             highlighted_answer += f"<span class='highlight3'>{word}</span> "
    #             if word in sentence_words:
    #                 sentence_words.remove(f"{word}")
    arr = [highlighted_answer.strip(), highlighted_sentence.strip()]
    return arr


if __name__ == '__main__':
    app.run(debug=True)