import numpy
from keras.models import load_model
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


model = load_model('CatsvsDogs_model_20epoch.h5')

# dictionary to label all traffic signs class.
classes = {
    0: 'I am a Cat!',
    1: 'I am a Dog!',
}
# initialise GUI
top = tk.Tk()
top.geometry('820x650')
top.title('Classifier')


top.configure(background='Black')


label = Label(top, background='Black', font=('Small Fonts', 15, 'bold'))
sign_image = Label(top)


def classify(file_path):
    image = Image.open(file_path)
    image = image.resize((128, 128))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    image = image / 255
    pred = model.predict_classes([image])[0]
    sign = classes[pred]
    print(sign)
    label.configure(foreground='Yellow', text=sign)


def enable_classify(file_path):
    classify_b = Button(top, text="What am I?", command=lambda: classify(file_path), padx=10, pady=10)
    classify_b.configure(background='Yellow', foreground='Black',
                         font=('Small Fonts', 12, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)


def upload():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25),
                            (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        enable_classify(file_path)
    except:
        pass


upload = Button(top, text="Upload", command=upload, padx=10, pady=10)
upload.configure(background='Yellow', foreground='Black', font=('Small Fonts', 12, 'bold'))
upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Cats vs Dogs Classification", pady=20, font=('Comic Sans Ms', 20, 'bold'))
heading.configure(background='Black', foreground='Yellow')
heading.pack()
top.mainloop()