import py5
import primitif.line
import primitif.basic
import primitif.utility
import primitif.transformasiv2
import math
import numpy as np
import config

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER) 
    py5.background(191)
    primitif.basic.draw_kartesian(py5.width,py5.height,25, c=[0,0,0,255])
    primitif.basic.draw_margin(py5.width,py5.height,25, c=[0,0,0,255])
     
def draw():
    for x in [-1, 1]:
        for y in [-1, 1]:
            # Convert x and y to cartesian coordinates
            cartesian_coords = primitif.utility.convert_to_cartesian(x*200, y*100, py5.width, py5.height, 25)
 
            # persegi            
            persegi = primitif.basic.persegi(cartesian_coords[0], cartesian_coords[1], 80)
            primitif.basic.draw_dotted(persegi)
            
            # persegi panjang
            persegi_panjang = primitif.basic.persegi_panjang(cartesian_coords[0], cartesian_coords[1], 120, 70)
            primitif.basic.draw_dotted(persegi_panjang)
            
            # segitiga siku-siku
            segitiga_siku = primitif.basic.segitiga_siku(cartesian_coords[0], cartesian_coords[1], 100, 50)
            primitif.basic.draw_dotted(segitiga_siku)
             
            # trapesium siku-siku                   
            trapesium_siku = primitif.basic.trapesium_siku(cartesian_coords[0], cartesian_coords[1], 50, 50, 50)
            primitif.basic.draw_dotted(trapesium_siku)
            
            # lingkaran
            lingkaran = primitif.basic.lingkaran(cartesian_coords[0], cartesian_coords[1], 50)
            primitif.basic.draw_dotted(lingkaran)
             
            # Ellipse
            ellipseMidPoint = primitif.basic.ellipseMidpoint(cartesian_coords[0], cartesian_coords[1], 100, 50)
            primitif.basic.draw_dotted(ellipseMidPoint)
            
    pass

py5.run_sketch()