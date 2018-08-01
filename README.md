# Lleida apple dataset

That repository contains scripts and functions to help to visualize the annotations on the images, and also provides a tool for crop original images and also modify the annotations.

Useful when preparing a dataset to be passed to a faster RCNN network.

First, when we've got the original images and its annotations, we try to execute visualize_annot.py, and if annotations doesn't fit the original images, the images can be rotated until the annotations fits the referenced images.
