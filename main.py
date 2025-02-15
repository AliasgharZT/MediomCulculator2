
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.dialog import MDDialog 
from kivy.properties import ObjectProperty
import math
from kivymd.toast import toast  
import numpy 
# from scipy.x_crate import quad
from kivy.core.window import Window
Window.size = (512, 421)

Builder.load_file('style.kv') 
# Builder.load_file('DataCalculator\\style.kv') 

class Style(MDAnchorLayout):
    txt=ObjectProperty()
    mn=ObjectProperty() 
    _fpl=ObjectProperty()
    _xy=ObjectProperty()
    _xyz=ObjectProperty() 
    _x_c=ObjectProperty()
    num1=''
    amal=''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_key_down=self.on_key_down)
    def on_key_down(self, window, key, scancode, codepoint, modifier):
        try:
            if codepoint.isdigit():
                self.txt.text += codepoint
        except:
            pass

    def mom(self):
        if len(self.txt.text)==0:
            self.txt.text='0.'
        elif len(self.txt.text)!=0:
            t=0
            for q in self.txt.text:
                if q=='0':
                    t+=1
            if t==len(self.txt.text):
                self.txt.text='0.'
            else:
                t2=0
                for q in self.txt.text:
                    if q=='.':
                        t2+=1
                if t2==1:
                    pass
                else:
                    self.txt.text+='.'
        else:pass  

    def clear1(self):
        if self.txt.text=='':
            pass
        else:
            t=[]
            for q in self.txt.text:
                t.append(q)
            t.pop()
            tt=''
            for q in t:
                tt+=q 
            self.txt.text=tt 
    def clear(self):
        self.txt.text = '' 
        self.num1=0

    def jam(self):
        self.amal='+'
        self.num1=self.txt.text 
        self.txt.text=''
    def kam(self):
        self.amal='-'
        self.num1=self.txt.text 
        self.txt.text=''
    def zar(self):
        self.amal='*'
        self.num1=self.txt.text 
        self.txt.text=''
    def tagh(self):
        self.amal='/'
        self.num1=self.txt.text 
        self.txt.text=''
    def result(self):
        try:
            if self.amal=='*':
                num2=self.txt.text
                self.txt.text=str(float(self.num1)*float(num2))
            elif self.amal=='/':
                num2=self.txt.text
                self.txt.text=str(float(self.num1)/float(num2))
            elif self.amal=='+':
                num2=self.txt.text
                self.txt.text=str(float(self.num1)+float(num2))
            elif self.amal=='-':
                num2=self.txt.text
                self.txt.text=str(float(self.num1)-float(num2))
            else:pass
        except:pass 
    def radic(self):
        try:
            t=math.sqrt(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 

    def cos(self):
        try:
            t=math.cos(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 
    def sin(self):
        try:
            t=math.sin(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 
    def tan(self):
        try:
            t=math.tan(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 
    def cot(self):
        try:
            t=math.tan(float(self.txt.text))
            tt=1/t
            self.txt.text=str(tt)
        except:pass 
    def cosh(self):
        try:
            t=math.cosh(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 
    def sinh(self):
        try:
            t=math.sinh(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 
    def tanh(self):
        try:
            t=math.tanh(float(self.txt.text))
            self.txt.text=str(t)
        except:pass 
    def coth(self):
        try:
            t=math.tanh(float(self.txt.text))
            tt=1/t
            self.txt.text=str(tt)
        except:pass 

    def mosman(self):
        try:
            q=float(self.txt.text)
            q*=-1
            self.txt.text=str(q)
        except:pass 

    def fpl(self):
        self.mn.current='fpl'
    def x_c(self):
        self.mn.current='x_c'
    def xy(self):
        self.mn.current='xy'
    def xyz(self):
        self.mn.current='xyz'

    def fact(self):
        try:
            q=int(self._fpl.text)
            self._fpl.text=''
            w= math.factorial(q)
            self._fpl.text=str(w)
        except:
            toast('fact= int\n>>123') 
    def power(self):
        try:
            q=self._fpl.text.split(',')
            w=math.pow(float(q[0]),float(q[1]))
            self._fpl.text=str(w)
        except:
            toast('pow= vlaue,power\n>>3,3')
    def loga(self):
        try:
            q=self._fpl.text.split(',')
            w=math.log(float(q[0]),float(q[1]))
            self._fpl.text=str(w)
        except:
            toast('log= vlaue,Base\n>>8,3') 
    def help_fpl(self):
            m=MDDialog()
            m.title='Factoriel<number>123\npower<value,pow>12,3\nlogaritm<value,base>8,3'
            m.open() 

    def solve_xy(self):
        try:
            q=self._xy.text.split(',')
            ab1=[float(q[0]),float(q[1])]
            ab2=[float(q[2]),float(q[3])]
            c12=[float(q[4]),float(q[5])]
            a=numpy.array([ab1,ab2])
            b=numpy.array(c12)
            r=numpy.linalg.solve(a,b)
            x=str(r[0])
            y=str(r[1])
            self._xy.text='x='+x[0:4]+'II y='+y[0:4]
        except:
            toast('\na1,b1,a2,b2,c1,c2\n')
    def help_xy(self):
        m=MDDialog()
        m.title='a1,b1,a2,b2,c1,c2\nExample: 1,2,3,5,7,9'
        m.open() 

    def solve_xyz(self):
        try:
            q=self._xyz.text.split(',')
            abz1=[float(q[0]),float(q[1]),float(q[2])]
            abz2=[float(q[3]),float(q[4]),float(q[5])]
            abz3=[float(q[6]),float(q[7]),float(q[8])]
            c123=[float(q[9]),float(q[10]),float(q[11])]
            a=numpy.array([abz1,abz2,abz3])
            b=numpy.array(c123)
            r=numpy.linalg.solve(a,b)
            x=str(r[0])
            y=str(r[1])
            z=str(r[2])
            self._xyz.text='x='+x[0:4]+'II y='+y[0:4]+'II z='+z[0:4]
        except:
            toast('\na1,b1,z1,a2,b2,z2,a3,b3,z3,c1,c2,c3\n')
    def help_xyz(self):
        m=MDDialog()
        m.title='a1,b1,z1,a2,b2,z2,a3,b3,z3,c1,c2,c3\nExample: 1,2,3,4,5,7,9,8,7,1,0,3'
        m.open()

    def phrase(self,text): 
        s=text
        l=len(s) 
        o=['+','-','/','*']
        i=0
        z=[] 
        for q in range(l) :
            if q==0:pass 
            elif q==l-1:
                a=s[i:q+1] 
                z.append(a)  
                z.append(s[i]) 
            else:
                if s[q] in o and s[q-1] not in o:
                    a=s[i:q]
                    z.append(a) 
                    i=q+1 
                    z.append(s[q])
        z.pop() 
        return z      
    def x_value(self,list_text):
        zx=0 
        v=list_text

        for q in range(len(v)):
            if q==1:
                if v[q]=='+':
                    v1=v[q-1]
                    v1=v1[0:-1]
                    if v1=='':
                        v1=float(1) 
                    elif v1=='-':
                        v1=float(-1)
                    elif v1[0]=='-':
                        v1=float(v1[1:])*-1 
                    else:
                        v1=float(v1)

                    v2=v[q+1] 
                    v2=v2[0:-1]
                    if v2=='':
                        v2=float(1) 
                    elif v2=='-':
                        v2=float(-1)
                    elif v2[0]=='-':
                        v2=float(v2[1:])*-1 
                    else:
                        v2=float(v2)
                    zx=v1+v2
                elif v[q]=='-':
                    v1=v[q-1]
                    v1=v1[0:-1]
                    if v1=='':
                        v1=float(1) 
                    elif v1=='-':
                        v1=float(-1)
                    elif v1[0]=='-':
                        v1=float(v1[1:])*-1 
                    else:
                        v1=float(v1)

                    v2=v[q+1] 
                    v2=v2[0:-1]
                    if v2=='':
                        v2=float(1) 
                    elif v2=='-':
                        v2=float(-1)
                    elif v2[0]=='-':
                        v2=float(v2[1:])*-1 
                    else:
                        v2=float(v2)
                    zx=v1-v2 
                else:pass
            else:
                if v[q]=='+':
                    v1=zx 

                    v2=v[q+1] 
                    v2=v2[0:-1]
                    if v2=='':
                        v2=float(1) 
                    elif v2=='-':
                        v2=float(-1)
                    elif v2[0]=='-':
                        v2=float(v2[1:])*-1 
                    else:
                        v2=float(v2)
                    zx=v1+v2
                elif v[q]=='-':
                    v1=zx 

                    v2=v[q+1] 
                    v2=v2[0:-1]
                    if v2=='':
                        v2=float(1) 
                    elif v2=='-':
                        v2=float(-1)
                    elif v2[0]=='-':
                        v2=float(v2[1:])*-1 
                    else:
                        v2=float(v2)
                    zx=v1-v2 
                else:pass 

        r=str(zx)+'x'
        return r 
    def solve_x_c(self):
        try:
            x=self._x_c.text.split('=') 
            self._x_c.text='' 
            lx=self.phrase(x[0])
            v=self.x_value(lx)
            m=v[0:-1]
            m=float(m) 
            zc=x[-1]
            zc=float(zc) 
            r=zc/m
            r='x= '+str(r) 
            self._x_c.text=r  
        except:
            toast('\n1.2x+-5x+234x=456756.563\n')
    def help_x_c(self):
        m=MDDialog()
        m.title='Example : 1.2x+-5x+234x=456756.563'
        m.open()


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'
        self.title='Advanced Calculator'

        return Style()

MainApp().run()
