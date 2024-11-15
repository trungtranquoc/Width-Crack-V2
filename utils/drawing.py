import matplotlib.pyplot as plt
import numpy as np

from .polygon import Polygon, VisibilityPolygon
from .point import Point
from .geometry_2d import Segment
from typing import List, Union

def plot_polygon(pol: Union[Polygon, List[Point]], color: str, label: str = '', line_width: float = 1):
    if isinstance(pol, Polygon):
        draw_pol = pol.get_points() + [pol[0]]
    else:
        draw_pol = pol + [pol[0]]

    x, y = zip(*draw_pol)

    plt.plot(x, y, color=color, linewidth=line_width, label=label)

def plot_width_of_polygon(p: Point, pol: Polygon, vis_pol: VisibilityPolygon, join_segments: List[Segment]):
    plot_polygon(pol, color='red')
    plot_polygon(vis_pol, 'blue', line_width=0.5)
    plt.plot(p[0], p[1], marker='o', markersize=2, color='black')

    for segment in join_segments:
        x_value = segment[0][0], segment[1][0]
        y_value = segment[0][1], segment[1][1]

        plt.plot(x_value, y_value, color='green')

    plt.draw()