from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn import tree, metrics
from sklearn.metrics import confusion_matrix
from model import InputForm
from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestClassifier


def compute ( a,b,c,d,e,z,g,h,i):


# Preparing the data:
      data_file_name = 'breast-cancer-wisconsin.data.txt'

      first_line = "id,clump_thickness,unif_cell_size,unif_cell_shape,marg_adhesion,single_epith_cell_size,bare_nuclei,bland_chrom,norm_nucleoli,mitoses,class"
      with open(data_file_name, "r+") as f:
           content = f.read()
           f.seek(0, 0)
           f.write(first_line.rstrip('\r\n') + '\n' + content)
      df = pd.read_csv(data_file_name)
      df.replace('?', np.nan, inplace = True)
      df.dropna(inplace=True)
      df.drop(['id'], axis = 1, inplace = True)

      df['class'].replace('2',0, inplace = True)
      df['class'].replace('4',1, inplace = True)

      df.to_csv("combined_data.csv", index = False)

# Data sets
      CANCER_TRAINING = "cancer_training.csv"
      CANCER_TEST = "cancer_test.csv"

# Load datasets.
      training_set = tf.contrib.learn.datasets.base.load_csv_with_header(filename=CANCER_TRAINING,
                                                       target_dtype=np.int, features_dtype=np.int)
      test_set =     tf.contrib.learn.datasets.base.load_csv_with_header(filename=CANCER_TEST,
                                                   target_dtype=np.int, features_dtype=np.int)


        
      classifier =   RandomForestClassifier(n_estimators=10)

# Fit model.
      classifier = classifier.fit(training_set.data, training_set.target)
      k =a
      l = b
      m =c
      n= d
      o = e
      p = z
      q = g
      r = h
      s  = i   
               
      s= classifier.predict([[k,l,m,n,o,p,q,r,s]])
      if (s == [[1]]):
            return "malignant"
      else:
            return "benign"

if __name__ == '__main__':
    
      print (compute(a,b,c,d,e,f,g,h,i))