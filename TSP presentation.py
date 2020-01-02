import tkinter as tk
import random as r
import time as dt
import pymprog as pm
def bt_pos(n):
	r = 50+n*(tab_width + 5)
	return r
def sd_pos(n):
	r = 5+n*(75)
	return r


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



bar_colour = "yellow"
square_colour = "gray"
button_colour = square_colour
method1_colour = "blue"
method2_colour = "red"
method3_colour = "green"




tab_height = 75
tab_width = 145


meth1sol = [] # method 1 solution 
class Presentation():
	''' The window in which the presentation is housed'''
	def __init__(self, root):
		root.title("Presentation")
		root.wm_geometry("1000x1000")
		self.variables()
		self.widgets()

	def variables(self):
		self.t1 = tk.StringVar()
		self.t1.set("time:\n0")
		self.d1 = tk.StringVar()
		self.d1.set("distance\n0")

		self.t2 = tk.StringVar()
		self.t2.set("time:\n0")
		self.d2 = tk.StringVar()
		self.d2.set("distance\n0")

		self.t3 = tk.StringVar()
		self.t3.set("time:\n0")
		self.d3 = tk.StringVar()
		self.d3.set("distance\n0")

		self.time_var = [self.t1, self.t2, self.t3]
		self.dist_var = [self.d1, self.d2, self.d3]

	def widgets(self):
#Frames
		bar = tk.Frame(root, bg = bar_colour)
		bar.place(relwidth = 1, height = 100, x = 0, y = 0)
		sidebar = tk.Frame(root, bg = square_colour)
		sidebar.place(width = 155, relheight = 1, x = 0, y = 100)
		square = tk.Frame(root, bg = square_colour)
		square.place(x= 155, y = 100, relheight = 1, relwidth = 1)
#Canvas
		self.cartesian = tk.Canvas(square)
		self.cartesian.place(width = 1100, height = 650, x = 50, y = 50)
#bar Buttons
		method1 = tk.Button(bar, bd = 0, bg = button_colour, text = "method 1", command = lambda: self.method_1())
		method1.place(height = tab_height, width = tab_width, y = 25, x = bt_pos(0))
		method2 = tk.Button(bar, bd = 0, bg = button_colour, text = "method 2", command = self.method_2)
		method2.place(height = tab_height, width = tab_width, y = 25, x = bt_pos(1))
		method3 = tk.Button(bar, bd = 0, bg = button_colour, text = "method 3", command =lambda: self.connect(li, method3_colour, 3))
		method3.place(height = tab_height, width = tab_width, y = 25, x = bt_pos(2))
		gen10 = tk.Button(bar, bd = 0, bg = button_colour, text = "generate 10 points",command = lambda: self.show_points(10))
		gen10.place(height = tab_height, width = tab_width, y = 25, x = bt_pos(3))
		gen20 = tk.Button(bar, bd= 0, bg = button_colour, text = "generate 20 points",command = lambda: self.show_points(10))
		gen20.place(height = tab_height, width = tab_width, y = 25, x = bt_pos(4))

		clear = tk.Button(bar, bd = 0,  bg = button_colour, text = "clear", command = self.clear)
		clear.place(height = tab_height, width = tab_width, y = 25, x = bt_pos(5))
#Results
	#method 1
		method1_label = tk.Label(sidebar, bg = method1_colour, text="mehtod 1")
		method1_label.place(width = tab_width, height = 75, y = sd_pos(0), x = 5)
		self.method1_time = tk.Label(sidebar, bg = method1_colour, textvariable = self.t1)
		self.method1_time.place(width = tab_width, height = 75, y = sd_pos(1), x = 5)
		self.method1_distance = tk.Label(sidebar, bg = method1_colour, textvariable = self.d1)
		self.method1_distance.place(width = tab_width, height = 75, y = sd_pos(2), x = 5)
	#method 2
		method2_label = tk.Label(sidebar, bg = method2_colour, text="mehtod 2")
		method2_label.place(width = tab_width, height = 75, y = sd_pos(3), x = 5)
		self.method2_time = tk.Label(sidebar, bg = method2_colour, textvariable = self.t2)
		self.method2_time.place(width = tab_width, height = 75, y = sd_pos(4), x = 5)
		self.method2_distance = tk.Label(sidebar, bg = method2_colour,textvariable = self.d2)
		self.method2_distance.place(width = tab_width, height = 75, y = sd_pos(5), x = 5)
	#method 3
		method3_label = tk.Label(sidebar, bg = method3_colour, text="method 3")
		method3_label.place(width = tab_width, height = 75, y = sd_pos(6), x = 5)
		self.method3_time = tk.Label(sidebar, bg = method3_colour, textvariable = self.t3)
		self.method3_time.place(width = tab_width, height = 75, y = sd_pos(7), x = 5)
		self.method3_distance = tk.Label(sidebar, bg = method3_colour, textvariable = self.d3)
		self.method3_distance.place(width = tab_width, height = 75, y = sd_pos(8), x = 5)


	def load_points(self, n):
		points = []
		for i in range(n):
			p = Point(r.randint(10, 1090), r.randint(10, 640))
			points.append(p)
		return points
	def show_points(self, n):
		global li
		li = self.load_points(n)

		self.cartesian.delete("all")
		for i in li:
			x = i.x
			y = i.y
			self.cartesian.create_oval(x-1,y-1, x+1, y+1, fill = "black")
	def connect(self,l, c, v):
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
				self.cartesian.create_line(x1,y1,x2,y2, fill = c)
			x1 = l[0].x
			y1 = l[0].y
			x2 = l[-1].x
			y2 = l[-1].y
			d = l[0].distance(l[-1])
			sumdis+=d
			d = round(d, 2)
			t = dt.time() - t0
			t = round(t, 2)
			self.cartesian.create_line(x1,y1,x2,y2, fill = c)

			self.dist_var[v-1].set("distance:\n{}".format(d))
			self.time_var[v-1].set("time:\n{}".format(t))

		except:
			d = 0
			t = 0
			self.d3.set("distance:\n{}".format(d))
			self.t3.set("time:\n{}".format(t))
		print("d:"+str(d))
	def clear(self):
		global li
		self.cartesian.delete("all")
		li = []

	def method_1(self):
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
		pm.begin('subtour elimination')
		x = pm.var('x', E, bool)
		pm.minimize(sum(matrix[i][j]*x[i,j] for i,j in E), 'dist')
		for k in V:
			sum( x[k,j] for j in V if j!=k ) == 1
			sum( x[i,k] for i in V if i!=k ) == 1
			pm.solver(float, msg_lev = pm.glpk.GLP_MSG_OFF)
			pm.solver(int, msg_lev= pm.glpk.GLP_MSG_OFF)
			pm.solve()
		global subtourg
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
		   subt = subtourg(x)
		   if len(subt) == n:
		      print("Optimal tour length: %g"%pm.vobj())
		      print("Optimal tour:"); print(subt)
		      break
		   print("New subtour: %r"% subt)
		   if len(subt) == 1: break #something wrong
		   #now add a subtour elimination constraint:
		   nots = [j for j in V if j not in subt]
		   sum(x[i,j] for i in subt for j in nots) >= 1
		   pm.solve() #solve the IP problem again
		pm.end()
		for i in subt:
			meth1sol.append(li[i])
		self.connect(meth1sol, method1_colour, 1)
		
	def method_2(self):
		liin = []
		for i in li:
			r = []
			for j in li:
				r.append(i.distance(j))
			liin.append(r)
		print("liin: {}".format(liin))
		liout=[]  #output cities
		for i in range(len(liin)):
			del liin[i][i]
			liin[i].insert(i,99999999)
		print("liin: {}".format(liin))
		z = 0
		for i in range(len(liin)):
			y=min(liin[z])
			k=liin[z].index(y)
			del liin[k][z]
			liin[k].insert(z, 999999999)
			liout.append(k)
			print(z, k, liin[k][z], liin [z][k])
			for j in liin:
				j[z] = 9999999
			z = k
		print(liout)
		meth2sol = []
		for i in liout:
			meth2sol.append(li[i])
		self.connect(meth2sol, method2_colour, 2)


root = tk.Tk()
a = Presentation(root)
root.mainloop()

		