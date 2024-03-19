from point import Point

def bezier_curve_function(point1, point2, point3, t) :
    temp_x = ((1-t)**2)*point1.x + 2*(1-t)*t*point2.x + (t**2)*point3.x
    temp_y = ((1-t)**2)*point1.y + 2*(1-t)*t*point2.y + (t**2)*point3.y
    return Point(temp_x,temp_y)

def main_function(point1, point2, point3, n_iterate) :
    hasil = []
    for i in range (2**n_iterate+1) :
        hasil.append(bezier_curve_function(point1, point2, point3, i/(2**n_iterate)))
    return hasil