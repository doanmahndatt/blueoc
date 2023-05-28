import bubble_sort, selection_sort, quick_sort
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sort some numbers.')
    parser.add_argument('numbers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sort', dest='sort', action='store_const',
                        const='sort', default='sort',
                        help='sort the numbers')
    parser.add_argument('--quick', dest='sort', action='store_const',
                        const='quick', default='sort',
                        help='sort the numbers')
    parser.add_argument('--selection', dest='sort', action='store_const',
                        const='selection', default='sort',
                        help='sort the numbers')
    args = parser.parse_args()
    if args.sort == 'sort':
        print(bubble_sort.bubble_sort(args.numbers))
    elif args.sort == 'quick':
        print(quick_sort.quick_sort(args.numbers))
    elif args.sort == 'selection':
        print(selection_sort.selection_sort(args.numbers))
    else:
        print("Unknown sort type")