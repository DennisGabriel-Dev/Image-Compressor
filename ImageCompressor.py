import tkinter
from tkinter import *
from PIL import Image
from tkinter.filedialog import *

#paleta de cores
azul_pastel = '#4e5c69'
branco_condensado = '#ddcaa2'
verde_pastel_claro = '#aebea3'
rosa_pastel = '#b97479'
magenta_pastel = '#d83957'



#config da janela
window = Tk()
window.title("Image Compressor 🏞️")
window.geometry("650x500")
window.config(background=azul_pastel)

LTitle = Label(window, background=azul_pastel , foreground=branco_condensado,font='Verdana, 20', text='Image Compressor 🏞️')
LTitle.place(x=160 , y=40)

def new_file():
    path = askopenfilename()
    image = Image.open(path)
    image_height, image_width = image.size
    LSizeImage = Label(window,text='Selected Image: ' + 'Height: ' + str(image_height) + 'px, Width: ' + str(image_width) +'px',background=azul_pastel, foreground=branco_condensado, font='Arial,14')
    LSizeImage.place(x=150, y=180)
    def converter():
        height = int(EHeight_input.get())
        width = int(EWidth_input.get())
        new_geometry = (height, width)

        new_image = image.resize(new_geometry)
        new_image_path = asksaveasfilename()
        new_image.save(new_image_path + '.jpg')
        tkinter.messagebox.showinfo('', 'The Image was save!')


    LHeight = Label(window, text='Height',  background=azul_pastel, foreground=branco_condensado)
    LHeight.place(x=200, y= 130)

    EHeight_input = Entry(window, width=10, justify='center', background=branco_condensado, foreground=magenta_pastel)
    EHeight_input.place(x=200 , y = 100)

    LWidth = Label(window,  text='Width', background=azul_pastel, foreground=branco_condensado)
    LWidth.place(x=300, y=130)

    EWidth_input = Entry(window, width=10, justify='center', background=branco_condensado , foreground=magenta_pastel)
    EWidth_input.place(x=300, y= 100)

    BConverter = Button(window, background=verde_pastel_claro, command=converter, text='Transform', font='Arial,15' ,border=1)
    BConverter.place(x=248, y= 260)

button_file = Button(window, text='Open Image', font="Arial,15" , command=new_file, background=rosa_pastel, border=1)
button_file.place(x=240, y = 300)


window.mainloop()
