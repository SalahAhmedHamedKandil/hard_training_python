# pactical imge manipulation with pillow
from PIL import Image
# PIL => pillow
# open the image 
myimage=Image.open(r"D:\elzero_python\qqq.png")
# show the image
myimage.show()
# my cropped image
myBox=(0,0,400,400)
myNewImage=(myimage.crop(myBox))
# show my new image
myNewImage.show()
