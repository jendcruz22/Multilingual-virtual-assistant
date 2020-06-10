import tkinter as tk
import wikipedia
import wolframalpha

def show_entry_fields():
    try:
        #wolframalpha
        app_id = "53XQ53-622WXPK9TP"
        client = wolframalpha.Client(app_id)
        res = client.query(e1)
        answer = next(res.results).text
        root = tk.Tk()
        w = tk.Label(root, text="Results: %s" % (answer))
        e1.delete(0, tk.END)

    except:
        #wiki
        print()
        root = tk.Tk()
        w = tk.Label(root, text="Results: %s" % (wikipedia.summary(e1)))
        e1.delete(0, tk.END)
    


master = tk.Tk()
tk.Label(master, text="Search here").grid(row=0)

e1 = tk.Entry(master)
e1.insert(10, "")

e1.grid(row=0, column=1)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=4)

master.mainloop()

tk.mainloop()