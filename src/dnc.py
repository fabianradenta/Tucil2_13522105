from point import Point
import matplotlib.pyplot as plot

# 1. DECLARE PROCEDURE AND FUNCTION
def mid_point(p1,p2) :
    mid_x = (p1.x + p2.x)/2
    mid_y = (p1.y + p2.y)/2
    return Point(mid_x,mid_y)

def mid_of_mid(p1,p2,p3) :
    left_mid = mid_point(p1,p2)
    right_mid = mid_point(p2,p3)
    return mid_point(left_mid,right_mid)

def divide_and_conquer(point1, point2, point3, n_iterate) :
    # base case
    if (n_iterate==1) :
        return [point1,mid_of_mid(point1,point2,point3)]
    
    #recurrent
    else :
        left = divide_and_conquer(point1,mid_point(point1,point2),mid_of_mid(point1,point2,point3), n_iterate-1)
        right = divide_and_conquer(mid_of_mid(point1,point2,point3), mid_point(point2,point3),point3, n_iterate-1)
        return left + right


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


# MAIN PROGRAM
hasil = divide_and_conquer(p1, p2, p3, iterasi)
hasil.append(p3)


# DRAW CURVE
x_points = [point.x for point in hasil]
y_points = [point.y for point in hasil]
plot.figure(figsize=(8, 6))
plot.plot(x_points, y_points, color='blue')
plot.plot([p1.x, p2.x], [p1.y, p2.y], color='red')
plot.plot([p2.x, p3.x], [p2.y, p3.y], color='red')
plot.scatter(x_points, y_points, color='black',s=25)
plot.scatter(p1.x, p1.y, color='red')
plot.scatter(p2.x, p2.y, color='red')
plot.scatter(p3.x, p3.y, color='red')
plot.xlabel('X Coordinate')
plot.ylabel('Y Coordinate')
plot.title('Bezier Curve')
plot.grid(True)
plot.gca().set_aspect("equal",adjustable="box")
plot.show()