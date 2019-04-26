from __future__ import print_function
import cv2
import numpy as np



MAX_FEATURES = 500
GOOD_MATCH_PERCENT = 0.15

image_dir = './picture4/'
# method = 'ORB'
method = 'SIFT'
# method = 'SURF'
TF = '/TRUE/'
# TF = '/FALSE/'
result_dir = image_dir + method +'/'
film_dir = result_dir+'film/'


def alignImages(im1, im2 , meth='ORB'):
	input_img1 = im1.copy()
	input_img2 = im2.copy()
	# input_img1 = cv2.cvtColor(input_img1, cv2.COLOR_BGR2GRAY)
	# input_img2 = cv2.cvtColor(input_img2, cv2.COLOR_BGR2GRAY)
	if TF == '/TRUE/':
		cross = True
	else:
		cross = False
	print(meth)
	if meth == 'ORB':
		# Detect ORB features and compute descriptors.
		detector = cv2.ORB_create(MAX_FEATURES)
		matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=cross)
		# Convert images to grayscale

	elif meth == 'SURF':
		detector = cv2.xfeatures2d.SURF_create(MAX_FEATURES)
		matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck=cross)
	elif meth == 'SIFT':
		detector = cv2.xfeatures2d.SIFT_create(MAX_FEATURES)
		matcher = cv2.BFMatcher(cv2.NORM_L2, crossCheck=cross)

	keypoints1, descriptors1 = detector.detectAndCompute(input_img1, None)
	keypoints2, descriptors2 = detector.detectAndCompute(input_img2, None)

	# Match features.
	# create BFMatcher object
	# matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
	# matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
	matches = matcher.match(descriptors1, descriptors2, None)


	# Sort matches by score
	matches.sort(key=lambda x: x.distance, reverse=False)

	# Remove not so good matches
	numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
	matches = matches[:numGoodMatches]

	# Draw top matches
	imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
	# cv2.imwrite("matches.jpg", imMatches)

	# Extract location of good matches
	points1 = np.zeros((len(matches), 2), dtype=np.float32)
	points2 = np.zeros((len(matches), 2), dtype=np.float32)

	for i, match in enumerate(matches):
		points1[i, :] = keypoints1[match.queryIdx].pt
		points2[i, :] = keypoints2[match.trainIdx].pt

	# Find homography
	h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

	# Use homography
	height, width, channels = im2.shape
	im1Reg = cv2.warpPerspective(im1, h, (width, height))

	return im1Reg, h , imMatches
 
def cut_center(img,rate):
	height, width, channels = img.shape
	center_h = int(height/2)
	center_w = int(width/2)
	new_center_h = int(height*rate/2)
	new_center_w = int(width*rate/2)
	result = img.copy()
	result = result[center_h-new_center_h:center_h+new_center_h,center_w-new_center_w:center_w+new_center_w,:]
	return result

def combine_images(imgs):
  height0, width0, channels0 = imgs[0].shape
  height, width, channels = imgs[1].shape
  new_img = imgs[0].copy()
  for i in range(1,len(imgs)):
    print("process image %d ..."%i)
    img = imgs[i]
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(img[:,:,3])
    for x in range(height):
      for y in range(width):
        if img_gray[x,y]!=0:
          new_img[int((height0-height)/2)+x,int((width0-width)/2)+y,:]=img[x,y,:]
  return new_img

def make_loop(img):
  height, width, channels = img.shape
  rate = 0.5
  img2 = cv2.resize(img.copy(),(int(width*rate),int(height*rate)))

  imReg, h = alignImages(img2, img)
  cv2.imwrite(result_dir+"loop.jpg", imReg)
  img_combine = combine_images([img,img2])
  return img_combine

def make_film(img,rate,times):
	img2 = img.copy()
	for i in range(times):
		img2 = cv2.resize(cut_center(img2,rate),(1080,1920))
		outFilename = film_dir+"film%d.jpg"%i
		print("Saving film image : ", outFilename); 
		cv2.imwrite(outFilename, img2)


if __name__ == '__main__':

	# # Read reference image
	# # refFilename = image_dir+"Snapshot(0).jpg"
	# refFilename = image_dir+"0.jpg"
	# print("Reading reference image : ", refFilename)
	# imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)
	# imReference = cv2.resize(imReference,(1080,1920))
	# print(imReference.shape)
	# # imReference = imReference[419:1500,:,:]
	# # result=make_loop(imReference)
	# # cv2.imwrite("result.jpg", result)

	# img_combine = imReference
	# rate = 0.8
	# for i in range(1,6):
	# 	print(i)
	# 	if i not in []:
	# 		# Read image to be aligned
	# 		# imFilename = image_dir+"Snapshot(%d).jpg"%i
	# 		imFilename = image_dir+"%d.jpg"%i
	# 		print("Reading image to align : ", imFilename);  
	# 		im = cv2.imread(imFilename, cv2.IMREAD_COLOR)
	# 		im = cv2.resize(im,(1080,1920))
	# 		# im = im[419:1500,:,:]


	# 		print("Aligning images ...")
	# 		# Registered image will be resotred in imReg. 
	# 		# The estimated homography will be stored in h.
	# 		print('rate=%f'%rate) 
	# 		imReference = cut_center(imReference,rate)
	# 		height,width,c = imReference.shape
	# 		# rate = rate*0.95
	# 		# imReference = cut_center(imReference,0.95)

	# 		imReg, h ,match = alignImages(im, imReference, method)
	# 		cv2.imwrite(result_dir+"matches%d.jpg"%i, match)
			 
	# 		# Write aligned image to disk. 
	# 		outFilename = result_dir+"aligned%d.jpg"%i
	# 		print("Saving aligned image : ", outFilename); 
	# 		cv2.imwrite(outFilename, imReg)

	# 		# Print estimated homography
	# 		print("Estimated homography : \n",  h)

	# 		img_combine = combine_images([img_combine,imReg])
	# 		cv2.imwrite(result_dir+"combine%d.jpg"%i, img_combine)

	# 		# imReference = img_combine
	# 		imReference = imReg
	# 		# imReference = im

	# refFilename = image_dir+"0.jpg"
	# print("Reading reference image : ", refFilename)
	# imReference = cv2.imread(refFilename, cv2.IMREAD_COLOR)
	# # print((height,width))
	# # print(imReference)
	# imReference = cv2.resize(imReference,(width,height))
	# img_combine = combine_images([img_combine,imReference])
	# cv2.imwrite(result_dir+"combine_final.jpg",img_combine)

	# img = img_combine
	img = cv2.imread(result_dir+'combine5.jpg', cv2.IMREAD_COLOR)
	make_film(img,0.98,60)