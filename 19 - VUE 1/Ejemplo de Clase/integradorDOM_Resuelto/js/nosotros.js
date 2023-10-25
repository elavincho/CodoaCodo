let nosotros=`
`
for(let elemento of fotos){
    nosotros = nosotros + ` <img src= ${elemento} alt=""> `
}

document.querySelector("main").innerHTML=nosotros