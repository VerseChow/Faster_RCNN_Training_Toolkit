#!/bin/sh

echo "Cleaning Cache"
rm -r ./data/cache/
rm -r ./data/progress/annotations_cache
echo "Done cleaning, begin training!"

./experiments/scripts/faster_rcnn_end2end.sh 0 VGG16 progress -test \
	/home/verse/Documents/Faster_RCNN_Training_Toolkit/output/faster_rcnn_end2end/train/vgg16_faster_rcnn_iter_80000.caffemodel