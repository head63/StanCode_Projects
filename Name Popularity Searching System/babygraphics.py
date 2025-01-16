"""
File: babygraphics.py
Name: Yvonne
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    year_x = (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)
    x = GRAPH_MARGIN_SIZE + year_index * year_x
    return x


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # 上下兩條水平線
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    
    # 垂直線
    for index in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, index), 0, get_x_coordinate(CANVAS_WIDTH, index), CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, index) + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[index], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for name_index in range(len(lookup_names)):
        # 設定好name,color,rank_height
        name = lookup_names[name_index]
        color = COLORS[name_index % len(COLORS)]
        rank_height = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK
        for year_index in range(len(YEARS)):
            # x座標不受rank影響
            new_x = get_x_coordinate(CANVAS_WIDTH, year_index)
            old_x = get_x_coordinate(CANVAS_WIDTH, year_index-1)
            # 判斷year是否在YEARS內,顯示出text,new_y座標
            if str(YEARS[year_index]) in sorted(name_data[name], key=lambda ele: ele[0]):
                show = name + name_data[name][str(YEARS[year_index])]
                new_y = GRAPH_MARGIN_SIZE + int(name_data[name][str(YEARS[year_index])]) * rank_height
            else:
                show = name + '*'
                new_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            # 當index>0,即可判斷old_y座標
            if year_index > 0:
                if str(YEARS[year_index-1]) not in sorted(name_data[name], key=lambda ele: ele[0]):
                    old_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                else:
                    old_y = GRAPH_MARGIN_SIZE + int(name_data[name][str(YEARS[year_index-1])]) * rank_height
                canvas.create_line(old_x, old_y, new_x, new_y, width=LINE_WIDTH, fill=color)
            canvas.create_text(new_x+TEXT_DX, new_y, text=show, anchor=tkinter.SW, fill=color, font='setofont 10')
                

# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
