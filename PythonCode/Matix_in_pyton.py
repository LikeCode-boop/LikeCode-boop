import numpy as np

def matrix():
# make a matrix with numpy
    gfg = np.matrix('[1, 2, 3; 4, 5, 6; 7, 8, -9]')

    # applying matrix.put() method
 #   gfg.put(2, 43);
    print(gfg)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    matrix();

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
