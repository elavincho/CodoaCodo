/************** METODOS DE ORDENACION PARA ARRAYS *****************/

var frutas = ["Banana", "Naranja", "Manzana", "Mango", "Kiwi", "Pera"]
document.write("ARRAY ORIGINAL:", "<br>")
document.write(frutas, "<br>")
document.write("<br>", "ARRAY INVERTIDO:", "<br>")
document.write(frutas.reverse())
document.write("<br>")
document.write("<br>", "ARRAY ORDENADO:", "<br>")
document.write(frutas.sort())
document.write("<br>")
document.write("<br>", "ARRAY ORDENADO (Z-A):", "<br>")
document.write(frutas.reverse(frutas.sort()), "<br>")
document.write("<br><br>")

var edades = [23,45,19,40,78,52,30,90]
document.write("ARRAY ORIGINAL:", "<br>")
document.write(edades, "<br>")
document.write("<br>", "ARRAY INVERTIDO:", "<br>")
document.write(edades.reverse())
document.write("<br>")
document.write("<br>", "ARRAY ORDENADO:", "<br>")
document.write(edades.sort())
document.write("<br>")
document.write("<br>", "ARRAY ORDENADO (descendente):", "<br>")
document.write(edades.reverse(edades.sort()), "<br>")