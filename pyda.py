import wolframalpha

input = input("Question: ")
app_id = "53XQ53-622WXPK9TP"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print(answer)