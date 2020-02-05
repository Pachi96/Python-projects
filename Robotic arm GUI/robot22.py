from guizero import App, Box, Text, TextBox, PushButton, Slider, Picture

app = App(title="Robot 3000", bg=(140,140,140), layout="grid", height=355, width=439)

def call(opt,b_n,m_n,textboxn,c_slider_val_n):
	if opt == 1:
		b_n.repeat(100, increase_position, args=[m_n,textboxn,c_slider_val_n])
	elif opt == 2:
		b_n.repeat(100, decrease_position, args=[m_n,textboxn,c_slider_val_n])

def call_stop(opt,b_n):
	if opt == 1:
		b_n.cancel(increase_position)
	elif opt == 2:
		b_n.cancel(decrease_position)

def increase_position(motor,textbox_n, c_slider_val_n):
	if int(motor.get()) >= 0 and int(motor.get()) < 180 - int(StepSize.get()):
		acum=int(motor.get())+int(StepSize.get())
		motor.value = acum
		textbox_n.value = motor.value
		c_slider_val_n()

def decrease_position(motor,textbox_n, c_slider_val_n):
	if int(motor.get()) > 0 + int(StepSize.get()) and int(motor.get()) <= 180:
		acum=int(motor.get())-int(StepSize.get())
		motor.value = acum
		textbox_n.value = motor.value
		c_slider_val_n()

def slider_changed1(slider_value):
	textbox1.value = slider_value
	m1.value = slider_value
def slider_changed2(slider_value):
	textbox2.value = slider_value
	m2.value = slider_value
def slider_changed3(slider_value):
	textbox3.value = slider_value
	m3.value = slider_value

def c_slider_val_1():
	if str(textbox1.get()) == "":
		slider1.value = "0"
	else:
		slider1.value = textbox1.value
def c_slider_val_2():
	if str(textbox2.get()) == "":
		slider2.value = "0"
	else:
		slider2.value = textbox2.value
def c_slider_val_3():
        if str(textbox3.get()) == "":
                slider3.value = "0"
        else:
                slider3.value = textbox3.value

box1 = Box(app,border=True, grid=[0,0],layout="grid")
Text(box1, grid=[0,0],text="")

Text(box1, grid=[0,1], text="Motor 1")
m1 = TextBox(box1, grid=[1,1], text="90")
m1.bg=(190,220,249)

Text(box1, grid=[0,2], text="Motor 2")
m2 = TextBox(box1, grid=[1,2], text="90")
m2.bg=(190,220,249)

Text(box1, grid=[0,3], text="Motor 3")
m3 = TextBox(box1, grid=[1,3],text="45")
m3.bg=(190,220,249)

Text(box1, grid=[1,4],text="")
PushButton(box1, grid=[1,5], text="OK", width=2, height=1, align="right")

box_s = Box(app, grid=[1,0])
Text(box_s, text="  ")

box2 = Box(app, border=True,grid=[2,0], layout="grid")
Text(box2, grid=[0,0], text="     ")
one="one"

box3 = Box(app, grid=[2,2],border=True, align="left", layout="grid")
slider1=Slider(box3, grid=[0,0], end=180, command=slider_changed1)
Text(box3, grid=[0,1], text="Motor 1")
textbox1= TextBox(box3, grid=[0,2], text="90", command=c_slider_val_1)
textbox1.bg=(255,255,179)

slider2=Slider(box3, grid=[1,0], horizontal=False, start=180, end=0, command=slider_changed2)
Text(box3, grid=[1,1], text="Motor 2")
textbox2= TextBox(box3, grid=[1,2], text="90", command=c_slider_val_2)
textbox2.bg=(255,255,179)

slider3=Slider(box3, grid=[2,0],horizontal=False, start=180, end=0, command=slider_changed3)
Text(box3, grid=[2,1], text="Motor 3")
textbox3= TextBox(box3, grid=[2,2], text="45", command=c_slider_val_3)
textbox3.bg=(255,255,179)


# 1 es increase y 2 es decrease position

b_one = PushButton(box2, grid=[1,1], text="a", width=2, height=1)
b_one.when_left_button_pressed = lambda:call(2,b_one,m1,textbox1,c_slider_val_1)
b_one.when_left_button_released = lambda:call_stop(2,b_one)

b_two = PushButton(box2, grid=[2,0], text="b", width=2, height=1)
b_two.when_left_button_pressed = lambda:call(1,b_two,m2,textbox2,c_slider_val_2)
b_two.when_left_button_released = lambda:call_stop(1,b_two)

b_three = PushButton(box2, grid=[2,2], text="c", width=2, height=1)
b_three.when_left_button_pressed = lambda:call(2,b_three,m2,textbox2,c_slider_val_2)
b_three.when_left_button_released = lambda:call_stop(2,b_three)

b_four = PushButton(box2, grid=[3,1], text="d", width=2, height=1)
b_four.when_left_button_pressed = lambda:call(1,b_four,m1,textbox1,c_slider_val_1)
b_four.when_left_button_released = lambda:call_stop(1, b_four)

Text(box2, grid=[4,0], text="     ")

b_five = PushButton(box2, grid=[5,0], text="e", width=2, height=1)
b_five.when_left_button_pressed = lambda:call(1,b_five,m3,textbox3,c_slider_val_3)
b_five.when_left_button_released = lambda:call_stop(1,b_five)

b_six = PushButton(box2, grid=[5,2], text="f", width=2, height=1)
b_six.when_left_button_pressed = lambda:call(2,b_six,m3,textbox3,c_slider_val_3)
b_six.when_left_button_released = lambda:call_stop(2,b_six)

Text(box2, grid=[5,3], text="")
Text(box2, grid=[5,5], text="Step size")
StepSize=TextBox(box2, grid=[5,4], text="1")
StepSize.bg=(184,228,197)

box_ss = Box(app, grid=[2,1])
Text(box_ss, text="  ")

box_img = Box(app,grid=[0,2])
picture = Picture(box_img, image="dw.png")

app.after(1,c_slider_val_1)
app.after(1,c_slider_val_2)
app.after(1,c_slider_val_3)
app.display()
