from keras.models import load_model
import cv2
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

model = load_model('PlantSeedlings_Xception.h5')


def load_image(img_path, show=False):
    img = image.load_img(img_path, target_size=(71, 71))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor,
                                axis=0)
    img_tensor /= 255.

    if show:
        plt.imshow(img_tensor[0])
        plt.axis('off')
        plt.show()

    return img_tensor


img_path = 'D:/dataset/images/kaggle/test/Sugar beet/278bb719464c.png'
new_image = load_image(img_path,True)

# check prediction
pred = model.predict_classes(new_image)
print(pred)