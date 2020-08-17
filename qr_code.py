import qrcode

#function to generate qrcode
def generate_qr(data, name)-> 0:

	generate_qr.__annotations__['return'] += 1
	save_as = name.get() or f"untitled_{generate_qr.__annotations__['return']}"

	qr = qrcode.make(data.get())
	qr.save(f"{save_as}.png")

	return save_as
