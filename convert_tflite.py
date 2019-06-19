import tensorflow as tf

img = tf.placeholder(name='img', dtype=tf.float32,
                     shape=(1, 416, 416, 3))
var = tf.get_variable('weights')
