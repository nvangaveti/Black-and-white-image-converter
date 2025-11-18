import cv2
from tkinter import Tk, filedialog
image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")]
)
#image_path = input("Enter image path: ")
img = cv2.imread(image_path)
Grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
if img is not None:
    input1 = input("Select either Image to show or save: ").lower()
    if input1 == "show":
        cv2.imshow('show',Grayscale_img)
        print("Image shown Successfully")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif input1 == "save":
        cv2.imwrite('Grayscale_img.jpg', Grayscale_img)
        print("Image Saved Successfully")
else:
    print("Image not found")
