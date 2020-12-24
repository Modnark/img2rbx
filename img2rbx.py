import os
import uuid
from PIL import Image

scriptName = uuid.uuid4()

def writetoscript(contents):
    scriptfile = open(f"{scriptName}.txt", "a")
    scriptfile.write(f"{contents}\n")

script = ""

imageFile = input("Enter the name or directory of the image: ")

if os.path.exists(imageFile):
    if os.path.isfile(imageFile):
        print(f"Loading {imageFile}")
        image = Image.open(imageFile)
        imgW = image.size[0]
        imgH = image.size[1]
        angle = 270
        out = image.rotate(angle, expand=True)
        imgPx = out.convert('RGB')
        print(f"Writing script...")
        script += f"local f = Instance.new(\"Model\")\nf.Parent = workspace\nf.Name = \"{scriptName}\"\nlocal pr = workspace[\"{scriptName}\"]\n"
        for x in reversed(range(imgW)):
            for y in reversed(range(imgH)):
                r, g, b = imgPx.getpixel((y, x))
                script += f"p{x}{y} = Instance.new(\"Part\")\np{x}{y}.Anchored = true\np{x}{y}.Size = Vector3.new(0.05,0.05,0.05)\np{x}{y}.Color = Color3.fromRGB({r}, {g}, {b})\np{x}{y}.Position = Vector3.new({0.05*x}, {0.05*y}, 0)\np{x}{y}.Parent = pr\n"

        writetoscript(script)
        print(f"Finished!")
    else:
        print(f"{imageFile} is not a file!")
else:
    print(f"{imageFile} was not found...")