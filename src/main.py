import bruteforce
import dnc
import utils
import matplotlib.pyplot as plot

utils.welcome()
try : 
    iterasi = int(input("Jumlah iterasi : "))
    input_point_1 = input("Titik 1 : ")
    input_point_2 = input("Titik 2 : ")
    input_point_3 = input("Titik 3 : ")

    p1, p2, p3 = utils.process_input_point(input_point_1, input_point_2, input_point_3)

    if p1 is None or p2 is None or p3 is None:
        raise ValueError("Titik yang dimasukkan tidak valid.")

    hasil = []
    utils.method_option()
    tipe = int(input("Masukkan pilihan anda : "))
    while tipe not in [1,2] :
        tipe = int(input("Tolong masukkan input yang valid\nMasukkan pilihan anda : "))

    if (tipe==1) :
        hasil = dnc.divide_and_conquer(p1, p2, p3, iterasi)
        hasil.append(p3)
    else :
        hasil = bruteforce.main_function(p1, p2, p3, iterasi)

    # DRAW CURVE
    x_points = [point.x for point in hasil]
    y_points = [point.y for point in hasil]
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

except ValueError as e :
    print("Program berhenti. Error:",e)

utils.thanks()