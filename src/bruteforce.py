from point import Point
import matplotlib.pyplot as plot 

def bezier_curve_function(point1, point2, point3, t) :
    temp_x = ((1-t)**2)*point1.x + 2*(1-t)*t*point2.x + (t**2)*point3.x
    temp_y = ((1-t)**2)*point1.y + 2*(1-t)*t*point2.y + (t**2)*point3.y
    return Point(temp_x,temp_y)

def main_function(point1, point2, point3, n_iterate) :
    hasil = []
    for i in range (2**n_iterate+1) :
        hasil.append(bezier_curve_function(point1, point2, point3, i/(2**n_iterate)))
    return hasil


# 2. INPUT
# terima input
iterasi = int(input("iterasi : "))
input_titik_1 = input("titik 1 : ")
input_titik_2 = input("titik 2 : ")
input_titik_3 = input("titik 3 : ")

# pisahkan absis dan oordinat
x_str_1, y_str_1 = input_titik_1.split(',')
x_str_2, y_str_2 = input_titik_2.split(',')
x_str_3, y_str_3 = input_titik_3.split(',')

# casting tipe data
x1 = float(x_str_1)
x2 = float(x_str_2)
x3 = float(x_str_3)
y1 = float(y_str_1)
y2 = float(y_str_2)
y3 = float(y_str_3)

# declare point
p1 = Point(x1,y1)
p2 = Point(x2,y2)
p3 = Point(x3,y3)


# MAIN ALGORITHM
sol = main_function(p1, p2, p3, iterasi)
print(sol)

# DRAW CURVE
x_points = [point.x for point in sol]
y_points = [point.y for point in sol]
plot.figure(figsize=(8, 6))
plot.plot([p1.x, p2.x], [p1.y, p2.y], color='red')
plot.plot([p2.x, p3.x], [p2.y, p3.y], color='red')
plot.scatter(x_points, y_points, color='black',s=25)
plot.scatter(p1.x, p1.y, color='red')
plot.scatter(p2.x, p2.y, color='red')
plot.scatter(p3.x, p3.y, color='red')
plot.plot(x_points, y_points, color='blue')
plot.xlabel('X Coordinate')
plot.ylabel('Y Coordinate')
plot.title('Bezier Curve')
plot.grid(True)
plot.gca().set_aspect("equal",adjustable="box")
plot.show()