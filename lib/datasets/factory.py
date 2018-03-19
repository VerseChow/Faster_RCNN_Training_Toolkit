# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""Factory method for easily getting imdbs by name."""

__sets = {}

from datasets.pascal_voc import pascal_voc
from datasets.progress import progress
from datasets.coco import coco
import numpy as np

#specify the data path
progress_path = '/home/verse/Documents/py-faster-rcnn/data/progressiros'
for split in ['train', 'test']:
    name = '{}_{}'.format('progressiros', split)
    __sets[name] = (lambda split=split: progress(split, progress_path))

def get_imdb(name):
    """Get an imdb (image database) by name."""
    if not __sets.has_key(name):
        raise KeyError('Unknown dataset: {}'.format(name))
    return __sets[name]()

def list_imdbs():
    """List all registered imdbs."""
    return __sets.keys()
