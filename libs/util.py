from random import randint
import itertools
import numpy as np
import cv2


def single_rect_mask(height, width, channels=3, max_rw=-1, max_rh=-1, min_rw=1, min_rh=1):
    '''
    Generates random rectangular mask images
    :param height: height of the image
    :param width: width of the image
    :param channels: number of channels in image
    :param max_rw: Max width of mask rectangle
    :param max_rh: Max height of mask rectangle
    :param min_rw: Min width of mask rectangle
    :param min_rh: Min height of mask rectangle
    :return: mask
    '''

    if width < 64 or height < 64:
        raise Exception("Width and Height of mask must be at least 64!")

    # Create an empty black image
    img = np.zeros((height, width, channels), np.uint8)

    # Draw ONE random rectangle
    x1, y1 = randint(1, width-min_rw-4), randint(1, height-min_rh-4)
    if max_rw == -1:
        x2 = randint(x1+min_rw, width-3)
    else:
        x2 = randint(x1+min_rw, min(width-3, x1 + max_rw))

    if max_rh == -1:
        y2 =randint(y1+min_rh, height-3)
    else:
        y2 = randint(y1+min_rh, min(height - 3, y1 + max_rh))

    cv2.rectangle(img, (x1,y1),(x2,y2), color=(1,1,1), thickness=cv2.FILLED)

    return 1 - img


def random_mask(height, width, channels=3):
    """Generates a random irregular mask with lines, circles and elipses"""    
    img = np.zeros((height, width, channels), np.uint8)

    # Set size scale
    size = int((width + height) * 0.03)
    if width < 64 or height < 64:
        raise Exception("Width and Height of mask must be at least 64!")
    
    # Draw random lines
    for _ in range(randint(1, 20)):
        x1, x2 = randint(1, width), randint(1, width)
        y1, y2 = randint(1, height), randint(1, height)
        thickness = randint(3, size)
        cv2.line(img,(x1,y1),(x2,y2),(1,1,1),thickness)
        
    # Draw random circles
    for _ in range(randint(1, 20)):
        x1, y1 = randint(1, width), randint(1, height)
        radius = randint(3, size)
        cv2.circle(img,(x1,y1),radius,(1,1,1), -1)
        
    # Draw random ellipses
    for _ in range(randint(1, 20)):
        x1, y1 = randint(1, width), randint(1, height)
        s1, s2 = randint(1, width), randint(1, height)
        a1, a2, a3 = randint(3, 180), randint(3, 180), randint(3, 180)
        thickness = randint(3, size)
        cv2.ellipse(img, (x1,y1), (s1,s2), a1, a2, a3,(1,1,1), thickness)
    
    return 1-img
