import py5
import primitif.line
import primitif.basic
import primitif.utility
import primitif.transformasiv2
import math
import numpy as np
import config

margin = 25
x, y = (50,150)

def setup():
    py5.size(500,500)
    primitif.basic.draw_kartesian(py5.width,py5.height,25, c=[0,0,0,255])
    primitif.basic.draw_margin(py5.width,py5.height,25, c=[0,0,0,255])
    xo, yo = primitif.utility.convert_to_cartesian(x,y, py5.width, py5.height, margin)
    xc,yc = (xo+x, yo-y)
    
    # persegi    
#     persegi = primitif.basic.persegi(xo,yo,100)
#     primitif.basic.draw_bentuk(persegi)
#     tm = primitif.transformasiv2.rotate2D(45, 0, 0)
#     print(tm)
#     tm = primitif.transformasiv2.scale2D(.5,.5, 0, 0, tm)
#     print(tm)
#     tm = primitif.transformasiv2.shear2D(.5,.5, 0, 0, tm)
#     print(tm)
#     tm = primitif.transformasiv2.translate2D(200,0, tm)
#     print(tm)
#     persegi2 = primitif.transformasiv2.transformPoints2D(persegi,tm)
#     primitif.basic.draw_bentuk(persegi2)
#     
    # persegi panjang
    persegipanjang = primitif.basic.persegi_panjang(xo,yo,100,50)
    primitif.basic.draw_bentuk(persegipanjang)
    tm = primitif.transformasiv2.rotate2D(45, 0, 0)
    print(tm)
    tm = primitif.transformasiv2.scale2D(.5,.5, 0, 0, tm)
    print(tm)
    tm = primitif.transformasiv2.shear2D(.5,.5, 0, 0, tm)
    print(tm)
    tm = primitif.transformasiv2.translate2D(xc-100,0, tm)
    print(tm)
    persegipanjang2 = primitif.transformasiv2.transformPoints2D(persegipanjang,tm)
    primitif.basic.draw_bentuk(persegipanjang2)
# 
#     # segitiga siku-siku
#      segitigasiku = primitif.basic.segitiga_siku(xo,yo,100,50)
#      primitif.basic.draw_bentuk(segitigasiku)
#      tm = primitif.transformasiv2.rotate2D(45, 0, 0)
#      print(tm)
#      tm = primitif.transformasiv2.scale2D(.5,.5, 0, 0, tm)
#      print(tm)
#      tm = primitif.transformasiv2.shear2D(.5,.5, 0, 0, tm)
#      print(tm)
#      tm = primitif.transformasiv2.translate2D(xc-100,0, tm)
#      print(tm)
#      segitigasiku2 = primitif.transformasiv2.transformPoints2D(segitigasiku,tm)
#      primitif.basic.draw_bentuk(segitigasiku2)
# 
#     # trapesium siku-siku    
#      trapesiumsiku = primitif.basic.trapesium_siku(xo,yo,50,100,100)
#      primitif.basic.draw_bentuk(trapesiumsiku)
#      tm = primitif.transformasiv2.rotate2D(45, 0, 0)
#      print(tm)
#      tm = primitif.transformasiv2.scale2D(.5,.5, 0, 0, tm)
#      print(tm)
#      tm = primitif.transformasiv2.shear2D(.5,.5, 0, 0, tm)
#      print(tm)
#      tm = primitif.transformasiv2.translate2D(xc-100,0, tm)
#      print(tm)
#      trapesiumsiku2 = primitif.transformasiv2.transformPoints2D(trapesiumsiku,tm)
#      primitif.basic.draw_bentuk(trapesiumsiku2)
# 
#     # lingkaran    
#      lingkaran = primitif.basic.lingkaran(xo+50,yo+25,50)
#      primitif.basic.draw_bentuk(lingkaran)
#      tm = primitif.transformasiv2.rotate2D(45, 0, 0)
#      print(tm)
#      tm = primitif.transformasiv2.scale2D(.5,.5, 0, 0, tm)
#      print(tm)
#      tm = primitif.transformasiv2.shear2D(.5,.5, 0, 0, tm)
#      print(tm)
#      tm = primitif.transformasiv2.translate2D(xc-100,0, tm)
#      print(tm)
#      lingkaran2 = primitif.transformasiv2.transformPoints2D(lingkaran,tm)
#      primitif.basic.draw_bentuk(lingkaran2)
#     
#     # ellips
#     ellips = primitif.basic.ellipseMidpoint(xo+50,yo+25,100,50)
#     primitif.basic.draw_bentuk(ellips)
#     tm = primitif.transformasiv2.rotate2D(45, 0, 0)
#     print(tm)
#     tm = primitif.transformasiv2.scale2D(.5,.5, 0, 0, tm)
#     print(tm)
#     tm = primitif.transformasiv2.shear2D(.5,.5, 0, 0, tm)
#     print(tm)
#     tm = primitif.transformasiv2.translate2D(xc-100,0, tm)
#     print(tm)
#     ellips2 = primitif.transformasiv2.transformPoints2D(ellips,tm)
#     primitif.basic.draw_bentuk(ellips2)

def draw():
    pass

py5.run_sketch()
