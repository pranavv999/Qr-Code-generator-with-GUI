import tkinter as tk
from qr_gene import generate_qr

#initializing tkinter
root = tk.Tk()

#setting geometry
root.geometry("500x350")

#title of App
root.title("QR Code Generator")

#greet
greet = tk.Label(root, text="Welcome to QRcode Generator", fg='orange', font='ariel 20 bold')
greet.pack(pady=15)


#getting file name of the user else provide a custom name
intro = tk.Label(root, text="Provide file name below(such as 'new_file.png')", fg="green", font="verdana 12 italic")
intro.pack(pady=10)

file_name = tk.StringVar()
entry1 = tk.Entry(root, justify="center", text=file_name, width=40, bg='light blue', font="Terminal 13 italic")
entry1.pack(pady=10)

#entry widget to get user input but this will be a text to take multiline input
intro1 = tk.Label(root, text="Enter your Data to convert in QRCode", fg="green", font="verdana 12 italic")
intro1.pack(pady=10)

entry2 = tk.Text(root, height=4, width=40, bg='light yellow', font="TimesNewRoman, 12" )
entry2.pack()

#generator function
def generate():
	try:
		data = entry2.get("1.0", "end-1c")
		message = generate_qr(data, file_name)
		file_name.set(f"saved as {message}.png")
		root.update()

	except:
		
		file_name.set("Oppss...Something wrong with input try again")
		root.update()



#Creating Generate Button
button = tk.Button(root, text=" Generate ", command=generate)
button.pack(pady=20)

#running mainloop
root.mainloop()

