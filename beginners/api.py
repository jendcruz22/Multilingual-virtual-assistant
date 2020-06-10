import wikipedia
import wolframalpha
from flask import Flask, request, render_template,jsonify

app = Flask(__name__)

def do_something(question):
    #wiki
    final = wikipedia.summary(question)
    if final == 'null':
         #wolframalpha
        app_id = "53XQ53-622WXPK9TP"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        return(answer)

    else:
        return(final)
   

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    question = request.form['question']
    word = request.args.get('question')
    answer = do_something(question)
    result = {
        "output": answer
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

