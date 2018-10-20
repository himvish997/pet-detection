OXFORD-IIIT PET Dataset
-----------------------
Omkar M Parkhi, Andrea Vedaldi, Andrew Zisserman and C. V. Jawahar

They have created a 37 category pet dataset with roughly 200 images for each class. 
The images have a large variations in scale, pose and lighting. All images have an 
associated ground truth annotation of breed, head ROI, and pixel
level trimap segmentation.<br>
Link: http://www.robots.ox.ac.uk/~vgg/data/pets/<br>

## Downloads
The data needed for evaluation are: you can download the data from given link below and extract it(annotations & images) in the dataset directory.

Dataset(Images): http://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz<br>
Groundtruth data(Annotations): http://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz<br>

Contents:
--------
### Annotations: 
<pre>
`trimaps/` 	Trimap annotations for every image in the dataset
		Pixel Annotations: 1: Foreground 2:Background 3: Not classified
		
`xmls/`		Head bounding box annotations in PASCAL VOC Format

`list.txt`	Combined list of all images in the dataset.
		&nbsp;Each entry in the file is of following nature:<br/>
		Image CLASS-ID SPECIES BREED ID<br/>
		ID: 1:37 Class ids<br/>
		SPECIES: 1:Cat 2:Dog<br/>
		BREED ID: 1-25:Cat 1:12:Dog<br/>
		All images with 1st letter as captial are cat images while
		images with small first letter are dog images.
		
`trainval.txt`	Files describing splits used in the paper.However,

`test.txt`	you are encouraged to try random splits.
</pre>

### images
<pre>
This folder contains the all images of cat and dogs.
All images with 1st letter as captial are cat images while
images with small first letter are dog images. 
</pre>


Support:
-------
For any queries contact,

Omkar Parkhi: omkar@robots.ox.ac.uk

References:
----------
[1] O. M. Parkhi, A. Vedaldi, A. Zisserman, C. V. Jawahar
   Cats and Dogs  
   IEEE Conference on Computer Vision and Pattern Recognition, 2012

Note:
----
Dataset is made available for research purposes only. Use of these images must respect 
the corresponding terms of use of original websites from which they are taken.
See [1] for list of websites.   
