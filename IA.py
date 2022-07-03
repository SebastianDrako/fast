#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 21:21:43 2022

@author: long
"""
import csv
import tensorflow as tf
import numpy as np

file = open('rem1.csv')
csvreader = csv.reader(file)
rows = []

time = []
num = []
mem = []

for row in csvreader:
        rows.append(row)

file.close()


for row in rows:
    try:
        time.append(int(row[0]))
    except:
        pass
    try:
        num.append(int(row[0]))
    except:
        pass
    try:
        mem.append(int(row[0]))
    except:
        pass

del row, rows     


core = tf.keras.Sequential([
    tf.keras.layers.Dense(units=4 , input_shape=[1]),
    tf.keras.layers.Dense(units=3),
    tf.keras.layers.Dense(units=3),
    tf.keras.layers.Dense(units=2)
    ])

core.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)




historial = core.fit(mem, [time , num], epochs=1, verbose=False)


model.save('G1PRedic.h5')
