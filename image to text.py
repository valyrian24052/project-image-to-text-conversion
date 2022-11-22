import io
import csv
import cv2 as cv
from matplotlib import pyplot as plt
import glob
from PIL import Image
import pytesseract as tess 
import fitz
from numpy import asarray

#tesseract setup
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TESSDATA_PREFIX = r'C:\Program Files\Tesseract-OCR'

# Template maching algorithm setup
method=cv.TM_CCORR_NORMED

#pdf extraction
path=r"C:\Users\Valyr\Downloads\assignment_img_vrf\label.pdf"
pdf = fitz.open(path)

#list of templates
tempelates=[]
for filename in glob.glob('./symbols/*png'): 
    im=Image.open(filename)
    tempelates.append(im)

r=[]
# extract images out of a pdf
for page_index in range(len(pdf)):
    page = pdf[page_index]
    image_list=page.get_images()

    for image_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = pdf.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image1 = Image.open(io.BytesIO(image_bytes))
        text_data = tess.image_to_string(image1.convert('RGB'), lang='eng')
        array=str.split(text_data, "\n")
        lst = [x  for x in array[1:] if ('Device Name:' in x or 'LOT:' in x or 'REF' in x)]
        lst.append(array[0])
        lst[0] = lst[0][13:]
        lst[1] = lst[1][4:]
        lst[2] = lst[2][5:]
        r.append(lst)
# detecting signs in an image
        image=asarray(image1)
        image_cropped=[image[350:550,150:365], image[350:550,365:580], image[350:550,580:795], image[350:550,795:1010]]
        for croppedimg in image_cropped:
            for i in range(len(tempelates)):
                hi=asarray(tempelates[i])
                si=croppedimg
                res = cv.matchTemplate(hi, si, method)
                max_val = cv.minMaxLoc(res)[1]
                m=''
                if max_val>0.95 :
                    m+=str(i)

        r.append(m)


# writing everything in an excel file
with open('projectdata.csv','w',newline='') as f:
    writer=csv.writer(f)
    for row in r:
        writer.writerow(row)
  