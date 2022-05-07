listname = ['name', 'john', 'paul blart']
def greeter(name):
    print("Hello, " + name + ". Good Morning")
    print("How are you, " + name + "?")
    print(name + " that's cool i dont care.")

for i in listname:
    greeter(i)
