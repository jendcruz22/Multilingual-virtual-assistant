import wikipedia
import wolframalpha
from flask import Flask, request, render_template,jsonify

app = Flask(__name__)

def do_something(question):
    #wiki
    try:
        final = wikipedia.summary(question)
        return(final)
    except wikipedia.exceptions.DisambiguationError as e:
        return("{0}".format(e))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    question = request.form['question']
    # word = request.args.get('question')
    answer = do_something(question)
    result = {
        "output": answer
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

