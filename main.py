import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, roots):
        self.filename = None
        self.root = roots
        self.root.title("Watermark App")
        self.root.geometry("400x200")

        self.image_label = tk.Label(roots, text="No image selected")
        self.image_label.pack()

        self.select_button = tk.Button(roots, text="Select Image", command=self.select_image)
        self.select_button.pack()

        self.watermark_entry = tk.Entry(roots)
        self.watermark_entry.pack()

        self.watermark_button = tk.Button(roots, text="Add Watermark", command=self.add_watermark)
        self.watermark_button.pack()

    def select_image(self):
        self.filename = filedialog.askopenfilename(title="Select Image", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")))
        self.image_label.config(text=self.filename)

    def add_watermark(self):
        if not hasattr(self, 'filename'):
            self.image_label.config(text="Please select an image first!")
            return

        try:
            image = Image.open(self.filename)
            draw = ImageDraw.Draw(image)
            width, height = image.size
            watermark_text = self.watermark_entry.get()

            font_size = 36
            font = ImageFont.truetype("arial.ttf", font_size)
            text_width = draw.textlength(watermark_text, font=font)
            text_height = 40

            x = width - text_width - 10
            y = height - text_height - 10

            draw.text((x, y), watermark_text, fill="white", font=font)
            image = image.convert("RGB")
            image.show()
            # to save the image
            image.save("output.jpg")
        except Exception as e:
            self.image_label.config(text=f"Error: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
