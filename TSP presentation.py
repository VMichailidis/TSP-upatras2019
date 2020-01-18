import tkinter as tk
import random as r
import time as dt
import pymprog as pm


#the functions used to automate the tk.Place method in the placement of the programme's buttons and labels 
def bt_pos(n):
	r = n*(tab_width + 5)
	return r
def sd_pos(n):
	r = 5+n*(75)
	return r

#the class used to handle points and the function used to handle the distances between them
# 
class Point():
	def __init__(self, x, y):
		self.x = x 
		self.y = y
	def distance(self, p2):
		x1 = self.x
		y1 = self.y
		x2 = p2.x
		y2 = p2.y
		d = ((x1-x2)**2+(y1-y2)**2)**0.5
		return d


#the variables are placed here for easy acess and modification
bar_colour = "#FFDE03"
square_colour = "#795548"
brown1 = "#8D6E63"
button_colour = square_colour
method1_colour = "#0336FF"
method2_colour = "#FF0266"
method3_colour = "#00E676"

distance1 = 0
distance2 = 0
distance3 = 0

distances = [distance1, distance2, distance3]


font = "Arial 20"


tab_height = 75
tab_width = 145


meth1sol = [] #method 1 solution 
class Presentation():
	''' The window in which the presentation is housed'''
	def __init__(self, root):
		root.title("Presentation")
		root.wm_geometry("1000x1000")
		self.variables()
		self.widgets()
#the class that contains the text variables that are put inside the labels 
	def variables(self):
		self.t1 = tk.StringVar()
		self.t1.set("time:\n0s")
		self.d1 = tk.StringVar()
		self.d1.set("distance\n0")


		self.t2 = tk.StringVar()
		self.t2.set("time:\n0s")
		self.d2 = tk.StringVar()
		self.d2.set("distance\n0")

		self.t3 = tk.StringVar()
		self.t3.set("time:\n0s")
		self.d3 = tk.StringVar()
		self.d3.set("distance\n0")
		#lists containing the variables so that the programme can alter any and all of them with 1 variable 
		self.time_var = [self.t1, self.t2, self.t3]
		self.dist_var = [self.d1, self.d2, self.d3]
#the class that contains the widgets that are put inside the root
	def widgets(self):
#the different Frames used to handle the buttons, the labels and the cartesian plane which the salesman traverses
		
		# the frame in which the buttons are placed 
		bar = tk.Frame(root, bg = bar_colour)
		bar.place(relwidth = 1, height = 100, x = 0, y = 0)
		#the frame in which the labels are placed 
		sidebar = tk.Frame(root, bg = square_colour)
		sidebar.place(width = 155, relheight = 1, x = 0, y = 100)
		#the frame in which the cartesian plane is placed 
		square = tk.Frame(root, bg = square_colour)
		square.place(x= 155, y = 100, relheight = 1, relwidth = 1)
#Canvas
		#the plane in which the salesman travels 
		self.cartesian = tk.Canvas(square)
		self.cartesian.place(width = 1100, height = 650, x = 50, y = 50)
#bar Buttons
		#the button for method 1 (using the pymprog library)
		method1 = tk.Button(bar, bd = 0, bg = button_colour,activebackground = brown1, font = font, text = "method 1", command = lambda: self.method_1())
		method1.place(height = tab_height, width = tab_width, y = 25, x = bt_pos(0))
		#the button for method 2 (closest point)
		method2 = tk.Button(bar, bd = 0, bg = button_colour,activebackground = brown1, font = font, text = "method 2", command = self.method_b)
		method2.place(height = tab_height, width = tab_width, y = 25, x = bt_pos(1))
		#the button for method 3 (the Heinritz-Hsiao) method)
		method3 = tk.Button(bar, bd = 0, bg = button_colour,activebackground = brown1, font = font, text = "method 3", command = self.method_3)
		method3.place(height = tab_height, width = tab_width, y = 25, x = bt_pos(2))
		#the buttons to generate 25 and 20 points respectively
		gen10 = tk.Button(bar, bd = 0, bg = button_colour,activebackground = brown1, font = font, text = "generate 25 points",command = lambda: self.show_points(25))
		gen10.place(height = tab_height, width = 250, y = 25, x = bt_pos(3))
		gen20 = tk.Button(bar, bd= 0, bg = button_colour,activebackground = brown1, font = font, text = "generate 20 points",command = lambda: self.show_points(20))
		gen20.place(height = tab_height, width = 250, y = 25, x = bt_pos(4)+105)

		#the button that clears the plane and the distance/time counters
		clear = tk.Button(bar, bd = 0,  bg = button_colour,activebackground = brown1, font = font, text = "clear", command = self.clear)
		clear.place(height = tab_height, width = tab_width, y = 25, x = bt_pos(5)+210)
#the Results being displayed in the sidebar
	#method 1
		method1_label = tk.Label(sidebar, bg = method1_colour, font = font, text = "mehtod 1")
		method1_label.place(width = tab_width, height = 75, y = sd_pos(0), x = 5)
		self.method1_time = tk.Label(sidebar, bg = method1_colour, font = font, textvariable = self.t1)
		self.method1_time.place(width = tab_width, height = 75, y = sd_pos(1), x = 5)
		self.method1_distance = tk.Label(sidebar, bg = method1_colour, font = font, textvariable = self.d1)
		self.method1_distance.place(width = tab_width, height = 75, y = sd_pos(2), x = 5)
	#method 2
		method2_label = tk.Label(sidebar, bg = method2_colour, font = font, text="mehtod 2")
		method2_label.place(width = tab_width, height = 75, y = sd_pos(3)+5, x = 5)
		self.method2_time = tk.Label(sidebar, bg = method2_colour, font = font, textvariable = self.t2)
		self.method2_time.place(width = tab_width, height = 75, y = sd_pos(4)+5, x = 5)
		self.method2_distance = tk.Label(sidebar, bg = method2_colour, font = font, textvariable = self.d2)
		self.method2_distance.place(width = tab_width, height = 75, y = sd_pos(5)+5, x = 5)
	#method 3
		method3_label = tk.Label(sidebar, bg = method3_colour, font = font, text="method 3")
		method3_label.place(width = tab_width, height = 75, y = sd_pos(6)+10, x = 5)
		self.method3_time = tk.Label(sidebar, bg = method3_colour, font = font, textvariable = self.t3)
		self.method3_time.place(width = tab_width, height = 75, y = sd_pos(7)+10, x = 5)
		self.method3_distance = tk.Label(sidebar, bg = method3_colour, font = font, textvariable = self.d3)
		self.method3_distance.place(width = tab_width, height = 75, y = sd_pos(8)+10, x = 5)


	#the method which generates randomly all the points in the plane
	def load_points(self, n):
		points = []
		for i in range(n):
			p = Point(r.randint(10, 1090), r.randint(10, 640))
			points.append(p)
		return points

	#the method which saves the points in the global variable "li" and prints them on the cartesian plane
	def show_points(self, n):
		global li
		li = self.load_points(n)

		self.cartesian.delete("all") #ensuring the plane is clear before printing the points 
		for i in li:
			x = i.x
			y = i.y
			self.cartesian.create_oval(x-1,y-1, x+1, y+1, fill = "black") #the points are represented by black circles which are generated by the oval function.\
		#clears all the labels displaying previous measuremnts 
		for i in self.dist_var:
			i.set("distance:\n{}".format(0))
		for j in self.time_var:
			j.set("time:\n{}s".format(0))
	#the method which connects the points with a line coloured appropriately and calculates the distance the salesman travels
	def connect(self, l, c, v):# l: the list of points, c: the line's colour, v: the method's position in the distance variable list 
		sumdis = 0
		try:
			t0 = dt.time()
			for i in range(len(l)-1):
				x1 = l[i].x
				y1 = l[i].y
				x2 = l[i+1].x
				y2 = l[i+1].y
				d = l[i].distance(l[i+1])
				sumdis +=d
				#print(sumdis)
				self.cartesian.create_line(x1,y1,x2,y2, fill = c)
			x1 = l[0].x
			y1 = l[0].y
			x2 = l[-1].x
			y2 = l[-1].y
			d = l[0].distance(l[-1])
			sumdis+=d
			sumdis = round(sumdis, 2)
			self.cartesian.create_line(x1,y1,x2,y2, fill = c)

			self.dist_var[v-1].set("distance:\n{}".format(sumdis))

		except:
			d = 0
			t = 0
			self.dist_var[v-1].set("distance:\n{}".format(d))
			self.time_var[v-1].set("time:\n{}s".format(t))
		#print("d:"+str(d))

	#the method which clears the plane and the labels displaying the measurments 

	def distance_calculator(self, l):
		sumdis = 0

		t0 = dt.time()
		for i in range(len(l)-1):
			x1 = l[i].x
			y1 = l[i].y
			x2 = l[i+1].x
			y2 = l[i+1].y
			d = l[i].distance(l[i+1])
			sumdis +=d
			#print(sumdis)
		x1 = l[0].x
		y1 = l[0].y
		x2 = l[-1].x
		y2 = l[-1].y
		d = l[0].distance(l[-1])
		sumdis+=d
		sumdis = round(sumdis, 2)

		return sumdis

	def clear(self):
		global li
		self.cartesian.delete("all")
		li = []
		for i in self.dist_var:
			i.set("distance:\n{}".format(0))
		for j in self.time_var:
			j.set("time:\n{}s".format(0))
	#the method executing method 1	
	def method_1(self):
		#creates a distance matrix that essentially is a list containing lists with the property where matrix[i][j] is the distance between point i and point j
		t0 = dt.time()#starts to time the method until its completion
		matrix = []
		meth1sol = []
		for i in li:
			r = []
			for j in li:
				r.append(i.distance(j))
			matrix.append(r)
		n = len(matrix)
		V = range(n)
		E = [(i,j) for i in V for j in V if i!=j]
		#the algorithm that eliminates invalid subtours
		pm.begin('subtour elimination')
		x = pm.var('x', E, bool)
		#minimizes the sum of the distances found in the matrix
		pm.minimize(sum(matrix[i][j]*x[i,j] for i,j in E), 'dist')
		for k in V:
			sum( x[k,j] for j in V if j!=k ) == 1
			sum( x[i,k] for i in V if i!=k ) == 1
			#calls the solver method and deactivates the result message 
			pm.solver(float, msg_lev = pm.glpk.GLP_MSG_OFF)
			pm.solver(int, msg_lev= pm.glpk.GLP_MSG_OFF)
			pm.solve()
		global subtourg
		#the function that creates subtours
		def subtourl(x):
			succ = 0
			subt = [succ] #start from node 0
			while True:
				succ=sum(x[succ,j].primal*j for j in V if j!=succ)
				if succ == 0: break #tour found
				subt.append(int(succ+0.5))
			return subt
		subtourg = subtourl
		while True:
			#a loop that creates subtours and keeps them if they are valid, terminating the programme in the process, or discards them if they are not
		   subt = subtourg(x)
		   if len(subt) == n:
		      #print("Optimal tour length: %g"%pm.vobj())
		      #print("Optimal tour:"); print(subt)
		      break
		   print("New subtour: %r"% subt)
		   if len(subt) == 1: break #something wrong
		   #now add a subtour elimination constraint:
		   nots = [j for j in V if j not in subt]
		   sum(x[i,j] for i in subt for j in nots) >= 1
		   pm.solve() #solve the IP problem again
		pm.end()
		#print(subt)
		#now the solution is added to a list that can be interpreted by the connect method
		for i in subt:
			meth1sol.append(li[i])
		print(len(meth1sol))
		self.connect(meth1sol, method1_colour, 1)
		t1 = dt.time()
		t = t1 - t0
		t = round(t, 2)#the required time is calculated and rounded for conviniency
		self.t1.set("time:\n{}s".format(t))
	#the Heinritz-Hsiao method
	def method_2(self,lib):
		

		liin = []#similarly to method 1 a distance matrix is created
		for i in lib:
			r = []
			for j in lib:
				r.append(i.distance(j))
			liin.append(r)
		#print("liin: {}".format(liin))
		liout=[]  #output cities
		for i in range(len(liin)):
			del liin[i][i]
			liin[i].insert(i,999999999)#the distance matrix is modified to not allow the algorithm to return to the same point
		#print("liin: {}".format(liin))
		z = 0
		for i in range(len(liin)):
			y=min(liin[z])#the method sends the salesman to the nearest point
			k=liin[z].index(y)
			del liin[k][z]
			liin[k].insert(z, 999999999)#the distance matrix is aditionally modified to prevent the salesman to return to the same city be making the distance of the city he just visited apparently really high
			liout.append(k)
			#print(z, k, liin[k][z], liin [z][k])
			for j in liin:
				j[z] = 999999999
			z = k
		#print(liout)
		meth2sol = []
		for i in liout:#now the solution is added to a list that can be interpreted by the connect method
			meth2sol.append(li[i])
		
		#print(len(meth2sol))
		#the required time is calculated and rounded for conviniency
		return meth2sol
		

	def method_b(self):
		t0 = dt.time()#timer start
		lib = li
		sol = self.method_2(lib)
		dsol = self.distance_calculator(sol)
		#print("dsol:{}".format(dsol))
		for s in range(len(lib)):
			for k in range(len(lib)-1):
				l = lib[0]
				lib.pop(0)
				lib.append(l)

			l2 = self.method_2(lib)
			d2 = self.distance_calculator(l2)
			#print("d2:{}".format(d2))
			if d2 < dsol:
				sol = l2
				dsol = d2
			#print("dsol:{}".format(dsol))
		self.connect(sol, method2_colour, 2)
		t1 = dt.time()
		t = t1 - t0
		t = round(t,2)	
		self.t2.set("time:\n{}s".format(t))



	def method_3(self):# this method just connects the points in the order they were generated
		t0 = dt.time()
		self.connect(li, method3_colour, 3)
		t1 = dt.time()
		t = t1 - t0
		t = round(t,2)
		self.t3.set("time:\n{}s".format(t))
root = tk.Tk()
a = Presentation(root)
root.mainloop()		