import wikipedia
import wolframalpha
from flask import Flask, request, render_template,jsonify

app = Flask(__name__)

def virtualassistant(question):
    try:
        app_id = "53XQ53-622WXPK9TP"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        searchresult = next(res.results).text
        return(searchresult)
    except:
        print(wikipedia.summary(question))
        

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    question = request.form['question']
    searchresult = virtualassistant(question)
    result = {
        "output": searchresult
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

