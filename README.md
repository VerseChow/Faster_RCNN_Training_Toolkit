# Introduction

This is the reimplementation of the Faster RCNN based on Progress Lab Dataset, the original one could be referred to [official code](https://github.com/rbgirshick/py-faster-rcnn). I cleaned the redundant code for specific usage of [4Progress Lab](http://progress.eecs.umich.edu/).

There are two usages of this program, one is used for training end to end faster rcnn model, the other one is used for testing the model trained. Also with the following instruction, you could train your own dataset.

# Detailed Usage

## Training Own Dataset

1. Constuct your dataset structure and follow the dataset structure like [VOC2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/), and put it in `/data` folder like `/progressiros` folder in there
2. In `/data/scripts` folder, run fetch_imagenet_models.sh to fetch pretrained imagenet model and put it into `/data/faster_rcnn_models`
3. In `/lib/models/progressiros/VGG16/faster_rcnn_end2end`, modify two files named test.protxt and train.protxt to specify your dataset. In `test.protxt` file, modify cls_score and bbox_pred layers output to number of your dataset classes and 4*(num of your dataset classes)
4. In `/lib/datasets/tools` folder, in progress.py, modify name of classes
5. specify pretrained model in `train_progress.sh`

Then run following command in `ROOT FOLDER` to begin to train
```
sh train_progress.sh
```

Attention!!!
Before that!!!

Please include caffe module in ROOT FOLDER [caffe-fast-rcnn](https://github.com/rbgirshick/caffe-fast-rcnn/tree/0dcd397b29507b8314e252e850518c5695efbb83) and compile that!!!

The trained model will be in `/output/faster_rcnn_end2end/train` folder

## Testing

1. Please put test image in /data/demo folder
2. In `/tools/` folder, in demo.py file, modify class name and model name you want to use
3. Run `demo.py` file to see the results and specify pretrianed model

### Usage for Calculating mAP
1. specify pretrained model in `test_progress.sh`
2. Run `sh test_progress.h`
3. The default setting for calculating mAP is to read results from text file and compare them to xml file, you can change the setting in `experiments/scripts/faster_rcnn_end2end.sh` by setting `--txt` to 0. Then it well detect the image and calculate the mAP
4. The format of results of detection is like following:
```
obj1 xmin ymin xmax ymax
obj2 xmin ymin xmax ymax
...
```

### Note
1. You may have to change path in `lib/datasets/tools/factory.py` for training
2. You may have to change path in line 258 in `lib/fast_rcnn/test.py` and line 85 in `tools/train_net.py` for reading img and detection results path for testing

For more detail, please email ywchow@umich.edu

More features would be released soon!


