#!/usr/bin/env python2
# coding: utf-8

# In[ ]:


import keras
from keras.utils import np_utils
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.preprocessing.image import array_to_img, img_to_array
from keras.preprocessing.image import load_img, ImageDataGenerator
from keras.applications import imagenet_utils
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from PIL import Image
import datetime, time, os, random, sys
from glob import glob

def list_pictures(path):
    from glob import glob
    r = glob(os.path.join(path, '*.png'))
    assert len(r) != 0
    return r

# In[ ]:
argvs = sys.argv
argc = len(argvs)
if (argc != 2):
    print("err")
else:
    imgpath = argvs[1]


number_list = os.listdir('../../numberimg/imgs')
output_classes = len(number_list)
#output_classes = 10

#number = number_list[random.randrange(0, 100)]
#sample_name = list_pictures(os.path.join('../../numberimg/imgs/', number))[87]
#sample_name = '../../numberimg/imgs/5366/1.png'
sample_name = '../php/' + imgpath[2:]
print(sample_name)
img = load_img(sample_name, target_size=(64, 64))
x_sample = img_to_array(img)

#print(number_list)
#print(output_classes)
#plt.imshow(img)
#plt.show()
#print(number)


# In[ ]:


model = Sequential()

model.add(Conv2D(32, (3, 3), padding='same', input_shape=x_sample.shape))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(32, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(output_classes))
model.add(Activation('softmax'))

#model.summary()
model.compile(loss='categorical_crossentropy', optimizer='SGD', metrics=['accuracy'])


# In[ ]:


weight_file = glob('../../weight/resizeO10_*.hdf5')[-1]

model.load_weights(weight_file)


# In[ ]:


predict_classes = model.predict_classes(np.asarray([x_sample]), verbose=1)
#print("Predict : " + str(predict_classes[0]))
#print(['9052', '2223', '9282', '5140', '3802', '5366', '5495', '1683', '2694', '3277', '4082', '1327', '4581', '3837', '9851', '9864', '4019', '9137', '3289', '3229', '8778', '5922', '3606', '3719', '3413', '9203', '6091', '6407', '3300', '4675', '8176', '2340', '2514', '1796', '9173', '5810', '4814', '6906', '8294', '7611', '8583', '8677', '8478', '7046', '6010', '4121', '1753', '9472', '1778', '8009', '4646', '3355', '3186', '7212', '7464', '6257', '5562', '1393', '1741', '9054', '9547', '4775', '4628', '1664', '6877', '5682', '3403', '2370', '6856', '7743', '8151', '8255', '9673', '3695', '8640', '3111', '3953', '6830', '2060', '6554', '5006', '1834', '6182', '3920', '2650', '3842', '5511', '6758', '4265', '1177', '5948', '2481', '5567', '7240', '4956', '3926', '5091', '5992', '1292', '8412'][predict_classes[0]])
class_list = ['1283', '1313', '1349', '1407', '1557', '1752', '1760', '1766', '1772', '1860', '2142', '2162', '2181', '2310', '2366', '2450', '2498', '2613', '2690', '2751', '2795', '2819', '2876', '2935', '2977', '2983', '2990', '2996', '3004', '3159', '3290', '3325', '3328', '3524', '3682', '3715', '3765', '3839', '3853', '3891', '4189', '4401', '4512', '4600', '4601', '4776', '4955', '4964', '5037', '5066', '5208', '5262', '5293', '5477', '5481', '5502', '5652', '5882', '5928', '5953', '5956', '6243', '6263', '6310', '6311', '6357', '6365', '6480', '6554', '6662', '6666', '6686', '6696', '6744', '7089', '7142', '7304', '7308', '7324', '7340', '7521', '7640', '7772', '7886', '8008', '8143', '8239', '8481', '8498', '8579', '8611', '8926', '9049', '9119', '9399', '9835', '9864', '9865', '9929']
print(class_list[predict_classes[0]])
