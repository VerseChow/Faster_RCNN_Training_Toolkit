#!/bin/sh

echo "Cleaning Cache"
rm -rf $(pwd)/data/cache/
echo "Done cleaning, begin training!"
#pretrained model directory
PRETRAINED_WEIGHT=data/faster_rcnn_models/vgg16_faster_rcnn_iter_3000.iros.13obj

./experiments/scripts/faster_rcnn_end2end.sh 0 VGG16 progress -train \
	${PRETRAINED_WEIGHT}
