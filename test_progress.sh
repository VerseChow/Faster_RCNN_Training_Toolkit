#!/bin/sh

echo "Cleaning Cache"
rm -rf $(pwd)/data/cache/
rm -rf $(pwd)/data/progress/annotations_cache
echo "Done cleaning, begin training!"
#pretrained model directory
PRETRAINED_WEIGHT=$(pwd)/output/faster_rcnn_end2end/train/vgg16_faster_rcnn_iter_80000.caffemodel

./experiments/scripts/faster_rcnn_end2end.sh 0 VGG16 progress -test \
	${PRETRAINED_WEIGHT}