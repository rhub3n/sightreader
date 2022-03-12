from turtle import*
import random
tracer(False)

r = 13
d = 300

pitch = {'E':[r,-r/1.5],'F':[0, 0], 'G':[r, -r/1.5+(20/300)*d], 'A':[0,20], 'H':[r, -r/1.5 +2*+(20/300)*d], 'C2':[0,40], 'D2':[r, -r/1.5 + 3*+(20/300)*d], 'E2':[0,60], 'F2':[r, -r/1.5 +4*+(20/300)*d]}
sharps = [353253, 60, -r/1.5 +2*+(20/300)*d, -r/1.5 +4*+(20/300)*d, 40, -r/1.5+(20/300)*d, -r/1.5 + 3*+(20/300)*d, 20]
#order of sharps none, f, c, g, d, a, e, h
#tonalities c, g, d, a, e, h, f#, dflat
flats = []
# order of flats
#f, b, eflat, aflat, dflat, gflat
bsharps = [26362362, 40, -r/1.5+(20/300)*d, -r/1.5 + 3*+(20/300)*d, 20, -r/1.5, -r/1.5 +2*+(20/300)*d, 0]
#coords none, c2, g1, d2, a1, e1, h1, f1


def sharp(r):
    for i in range (2):
        lt(90)
        fd(r*3)
        fd(-r*3)
        rt(90)
        pu()
        fd(r)
        pd()

    pu()
    fd(-2*r)

    pd()
    lt(90)
    fd(r)
    rt(75)
    fd(r*1.5)
    fd(-r*2)
    fd(r*0.5)
    lt(75)
    fd(r)

    rt(75)
    fd(r*1.5)
    fd(-r*2)
    fd(r*0.5)
    rt(15)



 

def note(r):
    for i in range(2):
        circle(r,90)
        circle(r//2,90)


def stave(d):
    for i in range(5):
        pd()
        fd(d)
        fd(-d*2)
        fd(d)
        pu()
        lt(90)
        fd((20/300)*d)
        rt(90)


k = random.randrange(0,5)
q = random.randrange(0,5)



for i in range(1):
    pu()
    sign = random.choice(sharps)
    lista = sharps[:sharps.index(sign)+1]
    blista = bsharps[:sharps.index(sign)+1]
    for i in range(len(lista)):
        goto(-270+20*i, lista[i])
        pd()
        sharp(r)
        pu()
        
    for i in range(len(blista)):
        goto(-270+20*i, blista[i]-(2/3)*d)
        pd()
        sharp(r)
        pu()
        


for i in range(k):
    ypos = random.choice(list(pitch.values()))
    pu()
    goto(ypos[0], ypos[1])
    pd()
    note(r)
    pu()

for i in range(q):
    ypos = random.choice(list(pitch.values()))
    pu()
    goto(ypos[0], ypos[1]-(2/3)*d)
    pd()
    note(r)
    pu()


    
goto(0,0)
stave(d)
goto(0,(-2/3)*d)
stave(d)
goto(0,0)









