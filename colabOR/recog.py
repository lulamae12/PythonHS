!git clone https://github.com/tensorflow/models
checkpoint_name = 'mobilenet_v2_1.0_224'
!wget https://storage.googleapis.com/mobilenet_v2/checkpoints/{checkpoint_name}.tgz
!tar -xf {checkpoint_name}.tgz
checkpoint = '{0}.ckpt'.format(checkpoint_name)
