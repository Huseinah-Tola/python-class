# def area_of_square(side):
#     return 2**side

# print(area_of_square(4))


def convert(s):
    '''convert a string to an integer'''
    try:
        x = int(s)
        print("Conversion succeeded! x =", x)
    except ValueError:
        print("Conversion failed!")
        x = -1
    return x
# from exceptional import convert
# convert("34")
# convert("giraffe")
