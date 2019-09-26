import tkinter as tk
global outputLabel = tk.Label(window, text = output, font=("Helvetica", 16))
def displayOutput(output):

    outputLabel = tk.Label(window, text = output, font=("Helvetica", 16)).pack()#pack() works kinda like stack
def getTextFromTextBox():
    input = textBox.get()
    changeLabel()
    displayOutput(input)
def changeLabel():
    outputLabel.destroy()



window = tk.Tk()
window.title("TARS")

window.geometry("1600x900")
textBox = tk.Entry(window, width = 100)#create textBox in window
button = tk.Button(window,text = "Submit", command = lambda:getTextFromTextBox(), width = 50)#use lambda bc it goes immediatyl other wise

button.pack(side=tk.BOTTOM)
textBox.pack(side=tk.BOTTOM)
label = tk.Label(window, text = "Hello i am TARS").pack(side=tk.BOTTOM)#pack() works kinda like stack



window.mainloop() #Makes the window actually appear
