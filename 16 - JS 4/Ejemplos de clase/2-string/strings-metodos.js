/******************* STRINGS - MÁS MÉTODOS */

var cad= "Aprendiendo JavaScript "
document.write("<b>", cad, "</b>")
document.write("<br><br>")

/*.repeat(n) : Devuelve el texto de la variable repetido n veces.*/
document.write("REPEAT <br>")
document.write(cad.repeat(4)) // repite 4 veces
document.write("<br>")
document.write("*".repeat(10)) // repite 10 veces un string
document.write("<br>")
var guion = "- "
document.write(guion.repeat(5)) // repite 5 veces un string
document.write("<br><br>")

/*.toLowerCase(): Devuelve el texto de la variable en minúsculas.
  .toUpperCase(): Devuelve el texto de la variable en mayúsculas.*/

document.write("TOLOWERCASE: ")
document.write(cad.toLowerCase()) // pasa a minúsculas
document.write("<br>")
document.write("TOUPPERCASE: ")
document.write(cad.toUpperCase()) // pasa a mayúsculas
document.write("<br><br>")

/*.trim(): Devuelve el texto sin espacios a la izquierda y derecha.*/
console.log("********* TRIM *********")

var cad2= "       Texto de ejemplo     "
document.write("TRIM (ver consola) <br> <br>")
console.log(cad2 + "mas texto") //cadena de texto
console.log(cad2.trim() + " mas texto")

/*.replace(str, newstr): Reemplaza la primera aparición del texto str por newstr.*/
document.write("REPLACE <br>")
document.write(cad.replace("JavaScript", "Python"))
document.write("<br><br>")

/*.substr(ini, len): Devuelve el subtexto desde la posición ini hasta ini+len. (en desuso)*/
document.write("SUBSTR <br>")
document.write(cad.substr(12, 4)) //Inicia en 12 y desde allí muestra 4 caracteres
document.write("<br><br>") //Método en desuso, se aconsehja usar substring

/*.substring(ini, end): Devuelve el subtexto desde la posición ini hasta end.*/
document.write("SUBSTRING <br>") 
document.write(cad.substring(1, 4)) //Desde 1 hasta 4 (no inclusive)
document.write("<br><br>")