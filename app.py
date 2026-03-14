from flask import Flask, render_template, request
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html", extracted_text="")

@app.post("/ocr")
def ocr():
    file = request.files.get("image")
    selected_langs= request.form.getlist("langs")
    lang="+".join(selected_langs) if selected_langs else "eng"
    if file is None or file.filename =="":
        return render_template("index.html",extracted_text="No Image selected.")
    
    image=Image.open(file.stream)
    image = image.convert("L")
    image= image.resize((image.width*2, image.height*2))

    config="--oem 3 --psm 6"
    text=pytesseract.image_to_string(image, lang=lang, config=config)
    
    return render_template("index.html", extracted_text=text)

if __name__ == "__main__":
    app.run(debug=True)