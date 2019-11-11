#!/usr/bin/env python3

from __future__ import absolute_import, division, print_function, unicode_literals

import os
import matplotlib.pyplot as plt

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from IPython.display import Image, display

#Needed for cuDNN version not sure why########################
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)
##############################################################

print("TensorFlow version: {}".format(tf.__version__))

#import data
train_csv = pd.read_csv('data/train.csv')

