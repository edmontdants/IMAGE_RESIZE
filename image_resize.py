from tkinter import *
from PIL import Image
from PIL import ImageTk
import os
import shutil


def clear_temp():
	files_in_directory = os.listdir(f"{path}\\temp")
	filtered_files = [file for file in files_in_directory if file.endswith(".PNG")]
	for file in filtered_files:
		path_to_file = os.path.join(f"{path}\\temp", file)
		os.remove(path_to_file)
	os.rmdir(f"{path}\\temp")

def clear_save():
	files_in_directory = os.listdir(f"{path}\\save")
	filtered_files = [file for file in files_in_directory if file.endswith(".PNG")]
	for file in filtered_files:
		path_to_file = os.path.join(f"{path}\\save", file)
		os.remove(path_to_file)
	os.rmdir(f"{path}\\save")

def main():

	root = Tk() 
	root.geometry("800x600") 
	root.title("IMAGE RESIZER")
	# root.configure(bg = 'grey')
	v1 = DoubleVar() 

	temp=0
	if not os.path.exists(f"{path}\\temp"):
		try:
			os.mkdir(f"{path}\\temp")
		except OSError:
				print (f"Creation of the directory {path}\\temp failed")
		else:
				print (f"Successfully created the directory {path}\\temp ")

	if not os.path.exists(f"{path}\\save"):
		try:
			os.mkdir(f"{path}\\save")
		except OSError:
				print (f"Creation of the directory {path}\\save failed")
		else:
				print (f"Successfully created the directory {path}\\save ")


	def save(): 
		temp=int(v1.get())
		shutil.copy(f'{path}\\temp\\Resized_image_{temp}.{image_format}',f'{path}\\save')
		Label.update_idletasks()
		

	def show1(): 

		temp=int(v1.get())
		image1 = Image.open(f'{path}\\temp\\Resized_image_{temp}.{image_format}')
		image2 =  ImageTk. PhotoImage(image1)
		image_label = Label(root , image =image2)
		image_label.place(x = 300 , y = 200)
		Label.update_idletasks()
		

	s1 = Scale( root, variable = v1, 
			from_ = 1, to = 100, 
			orient = HORIZONTAL) 

	l3 = Label(root, text = "Horizontal Scaler") 

	b1 = Button(root, text ="Display Image", 
				command = show1, 
				bg = "yellow") 

	b2 = Button(root, text ="Save Image", 
				command = save, 
				bg = "yellow") 

	l1 = Label(root) 

	image=Image. open('image.png')
	image_format=image.format
	a,b=image.size
	ratio=a/b
	for i in range(1,101):
		new_image = image.resize((int(ratio*i*2), i*2))
		new_image.save(f'{path}\\temp\\Resized_image_{i}.{image_format}')



	s1.pack(anchor = CENTER) 
	l3.pack() 
	b1.pack(anchor = CENTER) 
	l1.pack() 
	b2.pack(side  = BOTTOM ) 

	root.mainloop() 

if __name__ == "__main__":

	path=os.getcwd()

	if os.path.exists(f"{path}\\save"):
		clear_save()

	main()
	
	if os.path.exists(f"{path}\\temp"):
		clear_temp()

