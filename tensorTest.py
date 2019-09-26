#tensortest
import tensorflow as tf
import numpy as np
hello = tf.constant("hello world!")
sess = tf.Session()
print(sess.run(hello))
