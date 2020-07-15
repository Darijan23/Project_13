from ctypes import *
import os
import cv2
import darknet
import glob

#lokacija slika za detekciju
ulazna_mapa = "./data/input/"
#lokacija detektiranih slikam
izlazna_mapa = "./data/output/"

def convertBack(x, y, w, h):								# Convert from center coordinates to bounding box coordinates
    xmin = int(round(x - (w / 2)))
    xmax = int(round(x + (w / 2)))
    ymin = int(round(y - (h / 2)))
    ymax = int(round(y + (h / 2)))
    return xmin, ymin, xmax, ymax


def cvDrawBoxes(detections, img):
    if len(detections) > 0:
        person_detection = 0
        for detection in detections:
            name_tag = detection[0].decode()
            if name_tag == 'person':
                x, y, w, h = detection[2][0],\
	                detection[2][1],\
	                detection[2][2],\
	                detection[2][3]
                xmin, ymin, xmax, ymax = convertBack(float(x), float(y), float(w), float(h))
                pt1 = (xmin, ymin)
                pt2 = (xmax, ymax)
                cv2.rectangle(img, pt1, pt2, (102, 102, 102), 2)
                cv2.putText(img,"[" + str(round(detection[1] * 100, 2)) + "]",(pt1[0], pt1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (102, 102, 102), 2)
        person_detection += 1

    return img
    #=================================================================#


netMain = None
metaMain = None
altNames = None


def YOLO(image_list):

    global metaMain, netMain, altNames
    configPath = "./cfg/yolo-obj.cfg"
    weightPath = "./proj13.weights"
    metaPath = "./data/obj.data"
    if not os.path.exists(configPath):
        raise ValueError("Invalid config path `" +
                         os.path.abspath(configPath)+"`")
    if not os.path.exists(weightPath):
        raise ValueError("Invalid weight path `" +
                         os.path.abspath(weightPath)+"`")
    if not os.path.exists(metaPath):
        raise ValueError("Invalid data file path `" +
                         os.path.abspath(metaPath)+"`")
    if netMain is None:
        netMain = darknet.load_net_custom(configPath.encode(
            "ascii"), weightPath.encode("ascii"), 0, 1)  # batch size = 1
    if metaMain is None:
        metaMain = darknet.load_meta(metaPath.encode("ascii"))
    if altNames is None:
        try:
            with open(metaPath) as metaFH:
                metaContents = metaFH.read()
                import re
                match = re.search("names *= *(.*)$", metaContents,
                                  re.IGNORECASE | re.MULTILINE)
                if match:
                    result = match.group(1)
                else:
                    result = None
                try:
                    if os.path.exists(result):
                        with open(result) as namesFH:
                            namesList = namesFH.read().strip().split("\n")
                            altNames = [x.strip() for x in namesList]
                except TypeError:
                    pass
        except Exception:
            pass

    for i in range(len(image_list)):
        image = cv2.imread(image_list[i])
        width = image.shape[1]
        height = image.shape[0]

        # Create an image we reuse for each detect
        darknet_image = darknet.make_image(width, height, 3)

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_rgb = cv2.resize(image_rgb,
                                       (width, height),
                                       interpolation=cv2.INTER_LINEAR)

        darknet.copy_image_from_bytes(darknet_image, image_rgb.tobytes())

        detections = darknet.detect_image(netMain, metaMain, darknet_image, thresh=0.25)


        image = cvDrawBoxes(detections, image_rgb)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        #cv2.imshow('Output', image)

        #exif_data = meta_data.get_exif_data()
        #print(exif_data)
        #======================================================

        filename = izlazna_mapa + "det" + str(i) + ".jpg"
        cv2.imwrite(filename, image)
        #cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
	#================================================================
    # Purpose : Get the list of Input Image Files
    #================================================================
    image_list = glob.glob(ulazna_mapa + "*.jpg")			#  Get list of Images
    print("Ukupno %d slika za detekciju.",len(image_list))			#  Get list of Images
    print(image_list)
    #=================================================================#
    YOLO(image_list)
