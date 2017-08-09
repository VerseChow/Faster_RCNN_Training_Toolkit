#!/bin/sh


echo "Cleaning Cache"
rm -r ./data/cache/
echo "Done cleaning, begin training!"

./experiments/scripts/faster_rcnn_end2end.sh 0 VGG16 progress
