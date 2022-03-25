import sys
import sharpen as sh
import boxblur as bb
import edge as e

print("1) Sharpen")
print("2) Box Blur")
print("3) Edge Detection")

op=int(input("Indica una opción de procesamiento -> "))
if op==1:
    sh.sharpen("Kendall.jpg")
if op==2:
    bb.boxblur("Kendall.jpg")
if op==3:
    e.edge("relieve.jpeg")
