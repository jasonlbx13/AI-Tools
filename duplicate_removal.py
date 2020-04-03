import os
import cv2 as cv
from skimage.measure import compare_ssim
import argparse

EXT = ['.jpg', '.jpeg', '.png']


def delete(imgs_n):
    for image in imgs_n:
        os.remove(image)


def find_sim_images(args):
    imgs_n = []
    img_files = [os.path.join(rootdir, file) for rootdir, _, files in os.walk(args.input_dir) for file in files if
                 (os.path.splitext(file)[-1] in EXT)]
    for currIndex, filename in enumerate(img_files):
        if filename in imgs_n:
            continue
        if currIndex >= len(img_files) - 1:
            break
        for filename2 in img_files[currIndex + 1:]:
            if filename2 in imgs_n:
                continue
            img = cv.imread(filename)
            img = cv.resize(img, (512,512))
            img1 = cv.imread(filename2)
            img1 = cv.resize(img1, (512, 512))
            ssim = compare_ssim(img, img1, multichannel=True)
            if ssim > float(args.threshold):
                imgs_n.append(filename2)
                print(filename, filename2, ssim)
    print(imgs_n)
    return imgs_n


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='delete duplicate pictures')
    parser.add_argument('--input_dir', help='images direction')
    parser.add_argument('--threshold', default=0.9, help='Similarity degree threshold')
    args = parser.parse_args()


    delete(find_sim_images(args))