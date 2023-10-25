/******************* STRINGS - MÉTODOS *******************/
var cad= "hola como estas"
document.write(cad)
document.write("<br> <br>")
//Para saber el largo de una cadena de texto
document.write("Largo de la cadena: ", cad.length)
document.write("<br> <br>")


// .charAt(pos): Devuelve el carácter en la posición pos de la variable.
document.write(cad.charAt(0)) // devuelve "h"
document.write("<br>")
var pos1= cad[1]
var pos2= cad[20]
document.write(pos1) //devuelve o
document.write("<br>")
document.write(pos2) //indefinido
document.write("<br> <br>")


//.concat(str1, str2...): Devuelve el texto de la variable unido a str1, a str2...
document.write("CONCAT <br>")
var nombre = "Luis"
var apellido = "Pérez"
document.write(cad.concat(" ",nombre," ", apellido,". ¿todo bien?")) 
document.write("<br> <br>")

/*.indexOf(str): Devuelve la primera posición del valor indicado.
  .indexOf(str, from): Idem al anterior, partiendo desde la posición from.
  .lastIndexOf(str, from): Idem al anterior, pero devuelve la última posición.*/

document.write("INDEXOF <br>")
document.write(cad, "<br>")
document.write("Posición de a: ", cad.indexOf("a")) // 3
document.write("<br>")
document.write("Posición de a (desde pos 4): ", cad.indexOf("a",4)) //13
document.write("<br> <br>")

document.write("LASTINDEXOF <br>")
document.write("Posición de o: ", cad.lastIndexOf("o")) //8
document.write("<br>")
document.write("Posición de o (desde pos 7): ", cad.lastIndexOf("o", 7)) //6 (de 7 para atrás)