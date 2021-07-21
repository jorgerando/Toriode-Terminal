# Toroide en el terminal por jorge rando ^^
import time
import math

class Pantalla :

    def __init__ (self, ancho , largo ) :

        self.ancho = ancho
        self.largo = largo
        self.pixels = []
        self.iniciarPixeles()

    def iniciarPixeles(self) :
        for i in range(self.ancho) :
            self.pixels.append([])
            for j in range(self.largo) :
                self.pixels[i].append(" ")

    def verPantalla(self) :
        string = ""
        for x in range (self.ancho):
            string = ""
            for y in range(self.largo):
                string = string + self.pixels[x][y]
            print(string)

    def resetear(self)  :
        for x in range (self.ancho):
            for y in range(self.largo):
                if x != 0 and y != 0 and x != self.ancho -1 and y != self.largo -1:
                  self.pixels[x][y] = " "
                else :
                  self.pixels[x][y] = " "

    def pixel(self , caracter , x ,y ) :
            if not (x >= self.ancho -1 or x < 0 or y < 0 or y >= self.largo -1 ):
             self.pixels[x][y] = caracter

    def dibujar(self , punto ) :

        self.pixel(punto.caracter, int( punto.X *0.6 ) + self.ancho // 2 , int(punto.Y )+ self.largo // 2 )

class Punto :

    def __init__(self, x , y , z , caracter):

       self.x = x
       self.y = y
       self.z = z

       self.X = 1
       self.Y = 1
       self.caracter = caracter

    def proyectar (self) :

        #if self.z != 0 :
         # self.X = self.x / self.z
          #self.Y = self.y / self.z
        #else :
         # self.X = self.x
          #self.Y = self.y

        self.X = self.x
        self.Y = self.y

        #self.X = 0.707 *(self.x - self.y)
        #self.Y = (0.82 * self.z )- 0.41 * ( self.x + self.y)

    def rotarX (self,angulo , px = 0 , py = 0 , pz = 0) :

        x = self.x
        y = self.y
        z = self.z

        self.x = ( x )
        self.y = ( y * math.cos(angulo) - z * math.sin(angulo ) )
        self.z = ( y * math.sin(angulo) + z * math.cos( angulo ) )

    def rotarY (self,angulo) :

        x = self.x
        y = self.y
        z = self.z

        self.x = x * math.cos(angulo)  + z * math.sin(angulo )
        self.y = y
        self.z = x * (-1) * math.sin(angulo) + z * math.cos( angulo )

    def rotarZ(self, angulo)     :

        x = self.x
        y = self.y
        z = self.z

        self.x = x * math.cos(angulo ) - y * math.sin(angulo)
        self.y = y * math.sin(angulo ) + y * math.cos(angulo)
        self.z = z

    def transladar(self ,px,py,pz ) :
        self.x = self.x + px
        self.y =  self.y + py
        self.z = self.z + pz

    def verCoordenadas(self):
        print ("X : " , self.x , "Y : ", self.y , "Z : " , self.z )

class Toride :

     def __init__ (self , radio_mayor , radio_menor) :

         self.R = radio_mayor
         self.r = radio_menor

     def CalcularToride(self,angulo,pantalla):

         puntos = []

         incr_alfa = 0.1
         incr_beta = 0.1

         alfa = 0
         beta = 0

         while ( alfa < 2 * math.pi ) :
             alfa = alfa + incr_alfa
             beta = 0
             while ( beta < 2 * math.pi ) :

                    x = (self.R + self.r * math.cos(alfa) ) * math.cos(beta)
                    y = (self.R + self.r * math.cos(alfa) ) * math.sin(beta)
                    z =  self.r * math.sin(alfa)

                    normal = self.vectorNormal(alfa,beta)
                    b = self.brillo(normal[0], normal[1] , normal[2] , 1 , 1 , 1)

                    Pi = Punto( x , y , z ,b)
                    Pi.rotarX(angulo)
                    Pi.rotarY(angulo)
                    #Pi.rotarZ(angulo)


                    puntos.append( Pi )

                    beta = beta + incr_beta

         for punto in puntos :
            punto.proyectar()
            pantalla.dibujar(punto)

     def CalcularCorazon(self,angulo,pantalla):
         puntos = []

         incr_alfa = 0.01


         alfa = 0


         while ( alfa < 2 * math.pi ) :
                    alfa = alfa + incr_alfa

                    x = 16*(math.sin(alfa)**3)
                    y = 13*math.cos(alfa) -5*math.cos(2*alfa) -2*math.cos(3*alfa)-math.cos(4*alfa)
                    z = 5

                    Pi = Punto( -y*2 , x*2 , z ,"#")
                    Pi.rotarX(angulo)

                    puntos.append( Pi )


         for punto in puntos :
            punto.proyectar()
            pantalla.dibujar(punto)


     def dibujarCirculo(self,R,giro,angulo,pantalla):
         incr_alfa = 0.01
         puntos = []
         alfa = 0
         while ( alfa < 2 * math.pi ) :
                 alfa = alfa + incr_alfa

                 x =  R * math.cos(alfa)
                 y =  R * math.sin(alfa)

                 if  giro ==  "X" :
                     puntos.append(Punto(x,y,0,"@"))
                 elif giro == "Y" :
                     puntos.append(Punto(0,x,y,"&"))
                 else :
                     puntos.append(Punto(x,0,y,"#"))

         for punto in puntos :

             if  giro ==  "X"  :
                 punto.rotarX(angulo)
             elif  giro == "Y"  :
                 punto.rotarY(angulo)
             else :
                 punto.rotarZ(angulo)

             punto.proyectar()
             pantalla.dibujar(punto)






     def vectorNormal(self,alfa,beta):
         x = math.cos(alfa) * math.cos(beta)
         y = math.sin(alfa) * math.sin(beta)
         z = math.sin(beta)
         return [ x ,  y  , z ]


     def brillo(self , n_x , n_y ,n_z , rx ,ry , rz ) :

       pr_p = (n_x * rx ) + (n_y * ry ) + (n_z * rz )
       pr_p = 1 - math.fabs(pr_p)

       if pr_p < 0.1 :
          return "·"
       elif pr_p < 0.2 :
          return  "-"
       elif pr_p < 0.3 :
          return  ":"
       elif pr_p < 0.4 :
           return "+"
       elif pr_p < 0.5 :
         return  "o"
       elif pr_p < 0.6 :
          return  "%"
       elif pr_p < 0.7 :
          return "$"
       elif pr_p < 0.8:
           return "0"
       elif pr_p < 0.9 :
          return "@"
       else :
           return  "#"

       return brillo

ancho = 50
largo = 150

def main () :
    pantalla = Pantalla(ancho , largo )
    t = Toride(20,10 )

    angulo = 0

    while True :

       t.CalcularToride(angulo,pantalla);
       pantalla.verPantalla()
       pantalla.resetear()

       angulo = angulo + 0.1

       time.sleep(0.1)

main()
