import wikipedia
import wolframalpha

while True:
    question = input("Q: ")

    try:
        #wolframalpha
        app_id = "53XQ53-622WXPK9TP"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        print(answer)

    except:
        #wiki
        print(wikipedia.summary(question))