from point import Point
import matplotlib.pyplot as plot

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