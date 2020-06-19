import wikipedia

while True:
    question = input("Q: ")

    print(wikipedia.summary(question, sentences=2))