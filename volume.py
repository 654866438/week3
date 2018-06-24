
#这周的online task的idea真是极其简单，就不详细的注释了，直接建个list，然后分别读取其中的半径和高，然后用带入圆柱体积公式就行了

import sys

PI = 3.141592


def main():
    args = sys.argv
    args_len = len(args)

    if args_len < 3:  # the first argument is the name of the python file
        print('Not enough arguments.')
        return

    if args_len > 3:
        print('Too many arguments.')
        return

    radius = float(args[1])
    if radius < 0:
        print('Radius cannot be negative.')
        return

    height = float(args[2])
    if height < 0:
        print('Height cannot be negative.')
        return

    volume = PI * radius ** 2 * height
    print('The volume of the cylinder is {:.2f}.'.format(volume))


if __name__ == '__main__':
    main()

