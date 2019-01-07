'''# Pet-Detection - create_pet_tf_record.py
   #
   # Copyright (C) 2018 Himanshu Vishwakarma <himvish997@gmail.com>
   #
   # Authors:
   #   Himanshu Vishwakarma <himvish997@gmail.com>
   #
   #   This program is free software; you can redistribute it and/or modify
   #   it under the terms of the GNU General Public License as published by
   #   the Free Software Foundation; either version 3 of the License, or
   #   (at your option) any later version.
   #
   #   This program is distributed in the hope that it will be useful,
   #   but WITHOUT ANY WARRANTY; without even the implied warranty of
   #   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   #   GNU General Public License for more details.
   #
   #   You should have received a copy of the GNU General Public License
   #   along with this program; if not, see <https://www.gnu.org/licenses/>.
   #'''

import tensorflow as tf
import numpy as np
import cv2
import os
import xml.etree.ElementTree as ET
from tqdm import tqdm
import parameters_variables as petNet



images_path = petNet.images_path
annotations_path = petNet.annotations_path
tfrecord_path =petNet.tfrecord_path
IMG_SIZE = petNet.IMG_SIZE
classes = petNet.classes
N_classes = petNet.N_classes


def read_image(fileName = "./dataset/images/Abyssinian_100.jpg", show_image = True):
    # print(fileName)
    img = cv2.imread(fileName)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    if show_image == True:
        cv2.imshow("Images", img)
        cv2.waitKey(0)
    return img


def read_xml(fileName = "pascal_voc.xml"):
    with open(fileName) as file:
        tree = ET.parse(file)
        root = tree.getroot()
        img_fileName = images_path + str(root.find('filename').text)
        img_size = root.find('size')
        w = int(img_size.find('width').text)
        h = int(img_size.find('height').text)

        boxes = []

        for object in root.iter('object'):
            box = []
            name = object.find('name').text
            if name not in classes:
                continue
            xmlbox = object.find('bndbox')
            x_min = int(float(xmlbox.find('xmin').text) * IMG_SIZE / w)
            x_max = int(float(xmlbox.find('xmax').text) * IMG_SIZE / w)
            y_min = int(float(xmlbox.find('ymin').text) * IMG_SIZE / h)
            y_max = int(float(xmlbox.find('ymax').text) * IMG_SIZE / h)
            box = [name, x_min, x_max, y_min, y_max]

            boxes.append(box)

        annotation = [img_fileName, w, h, boxes]

    return annotation


def one_hot_class(cls):
    if cls == 'cat':
        return np.array([1, 0], dtype=np.float32)
    elif cls == 'dog':
        return np.array([0, 1], dtype=np.float32)
    else:
        return np.array([0, 0], dtype=np.float32)


def center_box(xn, xx, yn, yx):
    x = int((xn + xx) / 2)
    y = int((yn + yx) / 2)
    w = int(xx - xn)
    h = int(yx - yn)
    return np.array([x, y, w, h], dtype=np.float32) / IMG_SIZE


def main():
    count = 0
    annotation_files = os.listdir(annotations_path)
    with tf.python_io.TFRecordWriter(tfrecord_path) as writer:
        for annotation_file in tqdm(annotation_files):
            count += 1
            annotation_fileName = os.path.join(annotations_path, annotation_file)
            if os.path.isfile(annotation_fileName):
                annotation = read_xml(annotation_fileName)
                image_fileName = annotation[0]
                cls, xn, xx, yn, yx = annotation[3][0]
                classes = one_hot_class(cls)
                box = center_box(xn, xx, yn, yx)
                label = np.concatenate((box, classes), axis=None)
            else:
                continue

            if os.path.isfile(image_fileName):
                img = read_image(image_fileName, show_image=False)
            else:
                continue

            image_raw = img.tostring()
            label_raw = label.tostring()

            example = tf.train.Example(features=tf.train.Features(feature={
                'label': tf.train.Feature(bytes_list=tf.train.BytesList(value=[label_raw])),
                'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_raw]))}))

            writer.write(example.SerializeToString())

            if count % 100 == 0:
                print("No of Iteration : ", count)



if __name__ == '__main__':
    main()

