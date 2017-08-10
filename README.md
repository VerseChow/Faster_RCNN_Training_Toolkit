# Introduction

This is the reimplementation of the Faster RCNN based on Progress Lab Dataset, the original one could be referred to [official code](https://github.com/rbgirshick/py-faster-rcnn). I cleaned the redundant code for specific usage of [4Progress Lab](http://progress.eecs.umich.edu/).

There are two usages of this program, one is used for training end to end faster rcnn model, the other one is used for testing the model trained. Also with the following instruction, you could train your own dataset.

# Detailed Usage

## Training Own Dataset

1. Constuct your dataset structure and follow the dataset structure like [VOC2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/), and put it in /data folder like /progress folder in there
2. In /data/scripts folder, run fetch_imagenet_models.sh to fetch pretrained imagenet model and put it into /imagenet_models
3. In /lib/models/progress/VGG16/faster_rcnn_end2end, modify two files named test.protxt and train.protxt to specify your dataset. In test.protxt file, modify cls_score and bbox_pred layers output to number of your dataset classes and 4*(num of your dataset classes)
4. In /lib/datasets/tools folder, in progress.py, modify name of classes

Then run train_progress.sh in ROOT FOLDER to begin to train

Attention!!!
Before that!!!

Please include caffe module in ROOT FOLDER [caffe-fast-rcnn](https://github.com/rbgirshick/caffe-fast-rcnn/tree/0dcd397b29507b8314e252e850518c5695efbb83) and compile that!!!

The trained model will be in /output/faster_rcnn_end2end/train folder

## Testing

1. Please put the trained model into /data/faster_rcnn_models/ folder, which could be downloaded in [model](https://drive.google.com/open?id=0BwzTAZGR6DHda1NNMHNRVU9ZZEk)
2. Please put test image in /data/demo folder
3. In /tools/ folder, in demo.py file, modify class name and model name you want to use
4. Run demo.py file to see the results

For more detail, please email ywchow@umich.edu

More features would be released soon!


