import Augmentor
import argparse
import os

def main(args):
    p = Augmentor.Pipeline(args.input_dir)
    if args.right_rotat != 0:
        p.rotate(probability=0.9, max_left_rotation=float(args.left_rotat), max_right_rotation=float(args.right_rotat)) # 旋转角度
    if args.skew != 0:
        p.skew_tilt(probability=0.8, magnitude=float(args.skew)) # 上下左右仿射形变
    if args.distortion != 0:
        p.random_distortion(probability=0.9, grid_height=5, grid_width=16, magnitude=float(args.distortion)) # 随机弹性扭曲
    if args.erasing != 0:
        p.random_erasing(probability=1, rectangle_area=float(args.erasing)) # 随机遮挡噪音
    if args.zoom != 0:
        p.zoom(probability=0.8, min_factor=1.1, max_factor=float(args.zoom)) # 随机缩放
    if args.flip != 0:
        p.flip_left_right(probability=0.5) # 左右镜像
    if args.crop:
        p.crop_random(probability=1, percentage_area=float(args.crop), randomise_percentage_area=False) # 按百分比随机裁剪
    if args.hist != 0:
        p.histogram_equalisation(probability=0.5) # 直方图平均
    if args.color_max != 0:
        p.random_color(probability=0.5, min_factor=float(args.color_min), max_factor=float(args.color_max)) # 灰度变化
    if args.contrast_max != 0:
        p.random_contrast(probability=0.5, min_factor=float(args.contrast_min), max_factor=float(args.contrast_min)) # 对比度变化
    p.sample(int(args.num))
    p.process()
    return

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='align facr from pictures')
    parser.add_argument('--input_dir', help='images file direction')
    parser.add_argument('--num', default=20, help='output images num(0-*)')
    parser.add_argument('--left_rotat', default=0, help='left rotation(0-25)')
    parser.add_argument('--right_rotat', default=0, help='right rotation(0-25)')
    parser.add_argument('--skew', default=0, help='skew tilt magnitude(0-1)')
    parser.add_argument('--distortion', default=0, help='random distortion magnitude(0-10)')
    parser.add_argument('--erasing', default=0, help='image erasing rectangle area(0.1-1)')
    parser.add_argument('--zoom', default=0, help='zoom max_factor(0.1-10)')
    parser.add_argument('--flip', default=0, help='flip or not(0, 1)')
    parser.add_argument('--crop', default=0, help='random crop percentage area(0-1)')
    parser.add_argument('--hist', default=0, help='histogram equalisation or not(0, 1)')
    parser.add_argument('--color_min', default=0, help='color min factor(0-1)')
    parser.add_argument('--color_max', default=0, help='color max factor(0-1)')
    parser.add_argument('--contrast_min', default=0, help='contrast min factor(0-1)')
    parser.add_argument('--contrast_max', default=0, help='contrast max factor(0-1)')
    args = parser.parse_args()
    main(args)
    print ('done')