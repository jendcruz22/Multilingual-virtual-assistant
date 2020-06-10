import wikipedia
import wolframalpha

def ocr_core(file):
    try:
        #wolframalpha
        app_id = "53XQ53-622WXPK9TP"
        client = wolframalpha.Client(app_id)
        res = client.query(file)
        answer = next(res.results).text
        return(answer)

    except:
        #wiki
        return(wikipedia.summary(file))
    
