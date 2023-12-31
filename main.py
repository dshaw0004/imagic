from tkinter.messagebox import showinfo, showerror
from tkinter.filedialog import askdirectory, askopenfilename
from PIL import Image
import time

import customtkinter as ct

ct.set_default_color_theme("green")


def save_img(filename: str, filetype: str):
    try:
        path = askdirectory(title='Select Folder')
        image = Image.open(filename)
        filename_with_extension = filename.split('/')
        filename_without_extension = filename_with_extension[len(
            filename_with_extension) - 1].split(".")

        image.save(
            fr"{path}\{filename_without_extension[0]}.{filetype.lower()}")
    except:
        showerror('Error', f'something went wrong', )
    else:
        showinfo("Image saved", "image has been saved to the location successfully")


def change_appearance_mode_event(new_appearance_mode: str):
    ct.set_appearance_mode(new_appearance_mode)


class App(ct.CTk):
    filename = ""
    supported_format: list[str] = [
        "ICNS",
        "ICO",
        "IM",
        'PCX',
        'PDF',
        "PNG",
        'SPIDER',
        'TFIF',
        'TGA',
        'WEBP',
    ]
    supported_file_extension: str = "*.gif;*.im;*.icns;*.ico;*.pcx;*.png;*.spider;*.tfif;*.tga;*.webp;*.jpg;*.jpeg"

    def open_image(self):
        self.filename = askopenfilename(initialdir="/", title="Select A Image",
                                        filetypes=(
                                            ("Image Files",
                                             self.supported_file_extension
                                             ),
                                        )
                                        )

        img = Image.open(self.filename)
        self.image_element.configure(dark_image=img, size=(200, 200))
        if self.btn_open.cget("state") != 'disabled':
            self.btn_save.configure(state="normal")
            self.file_type.configure(state="normal")
            self.change_img.pack(anchor=ct.CENTER)
            self.btn_open.configure(state="disabled")

    def __init__(self):
        super().__init__()
        self.title("Imagic")
        self.convert_to_filetype = ct.StringVar(value="ICO")
        self.iconbitmap(r'Assets\Imagic.ico')
        self.minsize(500, 400)
        self.image_element = ct.CTkImage(
            dark_image=Image.open(r"Assets\add-image-dark.png"),
            size=(200, 200))
        self.open_frame = ct.CTkFrame(self, fg_color='transparent')
        self.open_frame.pack(fill=ct.BOTH, expand=True, padx=10, pady=10)
        self.btn_open = ct.CTkButton(self.open_frame, command=self.open_image, image=self.image_element, text='',
                                     fg_color="transparent", hover_color=('#9ffce9', '#044030'))
        self.btn_open.pack(anchor=ct.CENTER)
        self.change_img = ct.CTkButton(
            self.open_frame, text='change image', command=self.open_image)

        self.util_frame = ct.CTkFrame(self, fg_color='transparent')
        self.util_frame.pack(fill=ct.BOTH, expand=True,
                             padx=10, anchor=ct.CENTER)
        self.util_frame.columnconfigure(0, weight=2)
        self.util_frame.columnconfigure(1, weight=2)
        self.util_frame.columnconfigure(2, weight=2)
        self.util_frame.columnconfigure(3, weight=2)

        self.btn_save = ct.CTkButton(self.util_frame, command=lambda: save_img(
            self.filename, self.convert_to_filetype.get()), text='save file', state="disabled")
        self.btn_save.grid(row=0, column=1)
        self.file_type = ct.CTkComboBox(self.util_frame, values=self.supported_format,
                                        variable=self.convert_to_filetype,
                                        state="disabled")
        self.file_type.grid(row=0, column=2, )

        self.appearance_mode = ct.CTkOptionMenu(self,
                                                values=[
                                                    "System", "Light", "Dark"],
                                                command=change_appearance_mode_event,
                                                width=2
                                                )
        self.appearance_mode.place(rely=0.95, relx=0.05, anchor='sw')

        splash_screen = ct.CTkLabel(self, text=' ',
                                    image=ct.CTkImage(
                                        dark_image=Image.open(
                                            r"Assets\Imagic.ico"),
                                        size=(150, 150))
                                    )
        splash_screen.place(x=0, y=0, relheight=1, relwidth=1)

        splash_screen.after(750, lambda: splash_screen.place_forget())


if __name__ == "__main__":
    App().mainloop()
