import keras.backend as K
from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from keras.models import Model
import numpy as np

# Note the image_shape must be multiple of patch_shape
image_shape = (256, 256, 3)


def l1_loss(y_true, y_pred):
    return K.mean(K.abs(y_pred - y_true))


def perceptual_loss_100(y_true, y_pred):
    return 100 * perceptual_loss(y_true, y_pred)


def perceptual_loss(y_true, y_pred):
    vgg = VGG19(include_top=False, weights='imagenet', input_shape=image_shape)
    loss_model = Model(inputs=vgg.input, outputs=vgg.get_layer('block4_conv4').output)
    loss_model.trainable = False
    return K.mean(K.square(loss_model(y_true) - loss_model(y_pred)))


def wasserstein_loss(y_true, y_pred):
    return K.mean(y_true*y_pred)

