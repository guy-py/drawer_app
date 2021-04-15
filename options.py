from tkinter import*
win=Tk()
win.title('Drawer')
colour=['blue', 'black', 'orange', 'violet', 'red', 'yellow', 'purple', 'pink', 'white', 'coral']
colours=['MediumVioletRed', 'DeepPink', 'PaleVioletRed', 'HotPink', 'LightPink', 'Pink', 'DarkRed', 'Red', 'Firebrick', 'Crimson', 'IndianRed', 'LightCoral', 'Salmon', 'DarkSalmon', 'LightSalmon', 'OrangeRed', 'Tomato', 'DarkOrange', 'Coral', 'Orange', 'DarkKhaki', 'Gold', 'Khaki', 'PeachPuff', 'Yellow', 'PaleGoldenrod', 'Moccasin', 'PapayaWhip', 'LightGoldenrodYellow', 'LemonChiffon', 'LightYellow', 'Maroon', 'Brown', 'SaddleBrown', 'Sienna', 'Chocolate', 'DarkGoldenrod', 'Peru', 'RosyBrown', 'Goldenrod', 'SandyBrown', 'Tan', 'Burlywood', 'Wheat', 'NavajoWhite', 'Bisque', 'BlanchedAlmond', 'Cornsilk', 'DarkGreen', 'Green', 'DarkOliveGreen', 'ForestGreen', 'SeaGreen', 'Olive', 'OliveDrab', 'MediumSeaGreen', 'LimeGreen', 'Lime', 'SpringGreen', 'MediumSpringGreen', 'DarkSeaGreen', 'MediumAquamarine', 'YellowGreen', 'LawnGreen', 'Chartreuse', 'LightGreen', 'GreenYellow', 'PaleGreen', 'Teal', 'DarkCyan', 'LightSeaGreen', 'CadetBlue', 'DarkTurquoise', 'MediumTurquoise', 'Turquoise', 'Aqua', 'Cyan', 'Aquamarine', 'PaleTurquoise', 'LightCyan', 'Navy', 'DarkBlue', 'MediumBlue', 'Blue', 'MidnightBlue', 'RoyalBlue', 'SteelBlue', 'DodgerBlue', 'DeepSkyBlue', 'CornflowerBlue', 'SkyBlue', 'LightSkyBlue', 'LightSteelBlue', 'LightBlue', 'PowderBlue', 'Indigo', 'Purple', 'DarkMagenta', 'DarkViolet', 'DarkSlateBlue', 'BlueViolet', 'DarkOrchid', 'Fuchsia', 'Magenta', 'SlateBlue', 'MediumSlateBlue', 'MediumOrchid', 'MediumPurple', 'Orchid', 'Violet', 'Plum', 'Thistle', 'Lavender', 'MistyRose', 'AntiqueWhite', 'Linen', 'Beige', 'WhiteSmoke', 'LavenderBlush', 'OldLace', 'AliceBlue', 'Seashell', 'GhostWhite', 'Honeydew', 'FloralWhite', 'Azure', 'MintCream', 'Snow', 'Ivory', 'White', 'Black', 'DarkSlateGray', 'DimGray', 'SlateGray', 'Gray', 'LightSlateGray', 'DarkGray', 'Silver', 'LightGray', 'Gainsboro']
shapes = ['Eraser', 'Oval', 'Line', 'Triangle', 'Rectangle', 'Fill', 'Colour Copier']
c = Canvas(win, height=500, width=500)
c.pack()
def colll():
    if not varc.get() == 'Colour' and not varo.get() == 'Outline':
        if not x.test == 0:
            c.delete(x.test)
        x.test=c.create_rectangle(5, 5, 25, 25, fill=varc.get(), outline=varo.get())
t = Button(text='Test', command=colll)
t.pack()
varc = StringVar()
varc.set('Colour')
colour = OptionMenu(win, varc, *colours )
varsd = StringVar()
varsd.set('Eraser Size')
sizes = [10, 20, 30, 40, 50]
size = OptionMenu(win, varsd, *sizes )
varo = StringVar()
varo.set('Outline')
outline = OptionMenu(win, varo, *colours )
varsh = StringVar()
varsh.set('Tool')
shape = OptionMenu(win, varsh, *shapes )
colour.pack()
outline.pack()
shape.pack()
size.pack()
def save():
    x.l = []
    how = 0
    for i in x.listt:
        h = c.coords(i[0])
        if x.shs[how] == 'r':
            h = c.coords(i[0])
            o = c.coords(i[1])
            print(len(i))
            x.l.append(str(h[0])+'^'+str(h[1])+'^'+str(h[2])+'^'+str(h[3])+'^'+str(h[4])+'^'+str(h[5])+'^'+str(o[4])+'^'+str(o[5])+'$'+str(x.fil[how])+'$'+str(x.out[how])+'$'+x.shs[how])
        elif x.shs[how] == 'l':
            x.l.append(str(h[0])+'^'+str(h[1])+'^'+str(h[2])+'^'+str(h[3])+'$'+str(x.fil[how])+'$'+str(x.out[how])+'$'+x.shs[how])
        elif x.shs[how] == 'o':
            x.l.append(str(h[0])+'^'+str(h[1])+'^'+str(h[2])+'^'+str(h[3])+'$'+str(x.fil[how])+'$'+str(x.out[how])+'$'+'o')
        elif x.shs[how] == 't':
            x.l.append(str(h[0])+'^'+str(h[1])+'^'+str(h[2])+'^'+str(h[3])+'^'+str(h[4])+'^'+str(h[5])+'$'+str(x.fil[how])+'$'+str(x.out[how])+'$'+x.shs[how])
        how+=1
    gag()
def key(event):
    if event.keycode == 65651:
        save()
    elif event.keycode == 458872:
        load()
    elif event.keycode == 393338:
        butt()
c.bind_all('<Key>', key)
def cir(xa, y):
    x.stringbar.append(c.create_oval(xa - 5, y - 5, xa + 5, y + 5, fill='blue', outline='light blue'))
def dell():
    for i in x.stringbar:
        c.delete(i)
    x.stringbar = []
def butt():
    if not x.listt == []:
        for i in x.listt[len(x.listt) - 1]:
            c.delete(i)
        del x.listt[len(x.listt) - 1]
def click(event):
    if varsh.get() != 'Tool' and varc.get() != 'Colour':
        if varsh.get() == 'Oval' and not varo == 'Outline':
            if len(x.x) == 0:
                x.x.append(event.x)
                x.y.append(event.y)
                cir(event.x, event.y)
            elif len(x.x) == 1:
                x.listt.append([c.create_oval(x.x[0], x.y[0], event.x, event.y, fill=varc.get(), outline=varo.get())])
                x.shs.append('o')
                x.out.append(varo.get())
                x.fil.append(varc.get())
                dell()
                x.x=[]
                x.y=[]
        if varsh.get() == 'Rectangle' and not varo == 'Outline' and not varc.get() == 'Colour':
            if len(x.x) == 0:
                x.x.append(event.x)
                x.y.append(event.y)
                cir(event.x, event.y)
            elif len(x.x) == 1:
                x.x.append(event.x)
                x.y.append(event.y)
                cir(event.x, event.y)
            elif len(x.x) == 2:
                x.x.append(event.x)
                x.y.append(event.y)
                cir(event.x, event.y)
            elif len(x.x) == 3:
                x.listt.append([c.create_polygon(x.x[0], x.y[0], x.x[1], x.y[1], x.x[2], x.y[2], fill=varc.get(), outline=varc.get()), c.create_polygon(x.x[1], x.y[1], x.x[2], x.y[2], event.x, event.y, fill=varc.get(), outline=varc.get()), c.create_line(x.x[0], x.y[0], x.x[1], x.y[1], fill=varo.get()), c.create_line(x.x[1], x.y[1], event.x, event.y, fill=varo.get()), c.create_line(x.x[2], x.y[2], event.x, event.y, fill=varo.get()), c.create_line(x.x[0], x.y[0], x.x[2], x.y[2], fill=varo.get())])
                x.shs.append('r')
                x.out.append(varo.get())
                x.fil.append(varc.get())
                dell()
                x.x=[]
                x.y=[]
        if varsh.get() == 'Line':
            if len(x.x) == 0:
                x.x.append(event.x)
                x.y.append(event.y)
                cir(event.x, event.y)
            elif len(x.x) == 1:
                x.listt.append([c.create_line(x.x[0], x.y[0], event.x, event.y, fill=varc.get())])
                x.shs.append('l')
                x.out.append(varo.get())
                x.fil.append(varc.get())
                dell()
                x.x=[]
                x.y=[]
        if varsh.get() == 'Triangle' and not varo.get() == 'Outline' and not varc.get() == 'Colour':
            if len(x.x) == 0:
                x.x.append(event.x)
                x.y.append(event.y)
                cir(event.x, event.y)
            elif len(x.x) == 1:
                x.x.append(event.x)
                x.y.append(event.y)
                cir(event.x, event.y)
            elif len(x.x) == 2:
                x.listt.append([c.create_polygon(x.x[0], x.y[0], x.x[1], x.y[1], event.x, event.y, fill=varc.get(), outline=varo.get())])
                x.shs.append('t')
                x.out.append(varo.get())
                x.fil.append(varc.get())
                dell()
                x.x=[]
                x.y=[]
        if varsh.get() == 'Fill' and not varc.get() == 'Colour' and not varo.get() == 'Outline':
            how = 0
            for i in x.listt:
                if x.shs[how] == 'o':
                    if (c.coords(i)[0] < event.x and c.coords(i)[2] > event.x):
                        if (c.coords(i)[1] < event.y and c.coords(i)[3] > event.y):
                            x.listt.append([c.create_oval(c.coords(i)[0], c.coords(i)[1], c.coords(i)[2], c.coords(i)[3], fill=varc.get(), outline=varo.get())])
                            x.shs.append('o')
                            x.out.append(varo.get())
                            x.fil.append(varc.get())
                            break
                if x.shs[how] == 'l':
                    if (c.coords(i)[0] < event.x and c.coords(i)[2] > event.x):
                        if (c.coords(i)[1] < event.y and c.coords(i)[3] > event.y):
                            x.listt.append([c.create_line(c.coords(i)[0], c.coords(i)[1], c.coords(i)[2], c.coords(i)[3], fill=varc.get(), outline=varo.get())])
                            x.shs.append('l')
                            x.out.append(varo.get())
                            x.fil.append(varc.get())
                            break
                how =+ 1
    if varsh.get() == 'Eraser' and varsd.get() != 'Eraser Size':
            if len(x.x) == 0:
                s = int(varsd.get()) / 2
                x.listt.append([c.create_oval(event.x - s, event.y - s, event.x + s, event.y + s, fill='white', outline='white')])
                x.shs.append('o')
                x.out.append(varo.get())
                x.fil.append(varc.get())
                x.x=[]
                x.y=[]
    if varsh.get() == 'Colour Copier':
        how = 0
        for i in x.listt:
            if x.shs[how] == 'o':
                if (c.coords(i)[0] < event.x and c.coords(i)[2] > event.x):
                    if (c.coords(i)[1] < event.y and c.coords(i)[3] > event.y):
                        varc.set(x.fil[how])
                        varo.set(x.out[how])
                        break
            if x.shs[how] == 'l':
                if (c.coords(i)[0] < event.x and c.coords(i)[2] > event.x):
                    if (c.coords(i)[1] < event.y and c.coords(i)[3] > event.y):
                         varc.set(x.fil[how])
                         varo.set(v.out[how])
                         break
            how =+ 1
c.bind('<Button-1>', click)
def gag():
    x.xy = Tk()
    x.xy.title('Name File')
    x.xy.geometry('200x200')
    ihou = open('mem.py', 'r').read()
    x.ddonee = Button(x.xy, text='Done', command=ask)
    x.lailai = Text(x.xy, height=1, width=20)
    x.lailai.pack()
    x.ddonee.pack()
def g():
    x.xy = Tk()
    x.xy.title('Choose Color')
    x.xy.geometry('200x200')
    ihou = open('mem.py', 'r').read()
    x.ddonee = Button(x.xy, text='Done', command=make)
    x.lailai = Text(x.xy, height=1, width=20)
    x.lailai.pack()
    x.files = Text(x.xy, height=1, width=20)
    x.files.pack()
    x.ddonee.pack()
def make():
    if not x.lailai.get("1.0",'end-1c') == '':
        ihou = colours
        if x.lailai.get("1.0",'end-1c') in ihou:
            if not x.files.get("1.0",'end-1c') == '':
                ihou = colours
                if x.files.get("1.0",'end-1c') in ihou:
                    varc.set(x.lailai.get("1.0",'end-1c'))
                    varo.set(x.files.get("1.0",'end-1c'))
                    x.xy.destroy()
class x:
    l = []
    mem = []
    x=[]
    y=[]
    stringbar = []
    listt = []
    shs = []
    out = []
    fil = []
    test = 0
    files = 0
    ddonee = 0
    xy = None
    lailai = None
def load():
    x.xy = Tk()
    x.xy.title('file')
    x.xy.geometry('200x200')
    ihou = open('mem.py', 'r').read()
    p = StringVar()
    x.files = OptionMenu(x.xy, p, *eval(ihou) )
    x.files.pack()
    x.ddonee = Button(x.xy, text='Done', command=sure)
    x.lailai = Text(x.xy, height=1, width=20)
    x.lailai.pack()
    x.ddonee.pack()
    x.files.mainloop()
def sure():
    if not x.lailai.get("1.0",'end-1c') == '':
        ihou = eval(open('mem.py', 'r').read())
        if x.lailai.get("1.0",'end-1c') in ihou:
            lload()
def lload():
    o = open(x.lailai.get("1.0",'end-1c'), 'r')
    x.mem = eval(o.read())
    o.close()
    for i in x.listt:
        butt()
    butt()
    l = []
    for i in x.mem:
        l.append(i)
    x.mem = l
    l = []
    for i in x.mem:
        l = i.split('^')
        huj = l[len(l) - 1]
        huj = huj.split('$')
        del l[len(l) - 1]
        l.append(huj[0])
        del huj[0]
        numbers = l
        if len(huj) == 1:
            fill = huj[0]
        else:
            fill = 0
        outline = huj[1]
        shape = huj[len(huj) - 1]
        if shape == 'r':
            x.listt.append([c.create_polygon(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], fill=fill, outline=fill), c.create_polygon(numbers[2], numbers[3], numbers[4], numbers[5], numbers[6], numbers[7], fill=fill, outline=fill), c.create_line(numbers[0], numbers[1], numbers[2], numbers[3], fill=outline), c.create_line(numbers[2], numbers[3], numbers[6], numbers[7], fill=outline), c.create_line(numbers[4], numbers[5], numbers[6], numbers[7], fill=outline), c.create_line(numbers[0], numbers[1], numbers[4], numbers[5], fill=outline)])
            x.shs.append(shape)
            x.out.append(outline)
            x.fil.append(fill)
        elif shape == 'o':
            x.listt.append([c.create_oval(numbers[0], numbers[1], numbers[2], numbers[3], fill=fill, outline=outline)])
            x.shs.append(shape)
            x.out.append(outline)
            x.fil.append(fill)
        elif shape == 'l':
            x.listt.append([c.create_line(numbers[0], numbers[1], numbers[2], numbers[3], fill=fill)])
            x.shs.append(shape)
            x.out.append(outline)
            x.fil.append(fill)
        elif shape == 't':
            x.listt.append([c.create_polygon(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], fill=fill, outline=outline)])
            x.shs.append(shape)
            x.out.append(outline)
            x.fil.append(fill)
    x.xy.destroy()
cac = Button(text='Choose Color', command=g)
cac.pack()
def ask():
    i = x.lailai.get("1.0",'end-1c')+'.py'
    o = open(i, 'w')
    o.write(str(x.l))
    o.close()
    x.l = str(open('mem.py', 'r').read())
    x.l = eval(x.l)
    x.l.append(i)
    k = open('mem.py', 'w')
    k.write(str(x.l))
    k.close()
    x.xy.destroy()
