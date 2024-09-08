from classifier_linear import clsfr,dataset_1
# import classifier_linear as cl
import numpy
import os
import logging

# Suppress TensorFlow logs
logging.getLogger('tensorflow').setLevel(logging.ERROR)  # Hide all but errors

# Disable oneDNN optimizations to avoid further logs
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

inputs,val_true = dataset_1(100)
predictions,w,b = clsfr(inputs,val_true,0.1,7)
print(inputs.shape)
print(val_true.shape)
print(predictions.shape)

# for i in range(len(predictions)):
#     if(predictions[i] < 0.5):
#         print(0)
#     else:
#         print(1)