var cualquierCadena="Brave new world";
var longitud=cualquierCadena.length
console.log("El carácter en el índice 0 es '" + cualquierCadena.charAt(0) + "'")

function vocal(a) {
    if ((a=="a")||((a)=="e")||((a)=="i")||((a)=="o")||((a)=="u")) {
      var v=true;
    } else if ((a=="A")||(a=="E")||(a=="I")||(a=="O")||(a=="U")) {
      var v=true;
    } else {
      var v=false;
    }
    return v
}
function contarvocal(b) {
var contador=0;
for (var i = 0; i < b.length; i++) {
  var temp1=b.charAt(i)
  if (vocal(temp1)==true) {
    contador+=1;
  } else {
    contador=contador;
  }
}
  return contador
}

console.log(contarvocal("hola"))

function espacio(a) {
    if (a==" ") { var a=true} else { var a= false}
    return a
}
function removespace(b) {
    var salida="";
    for (var i = 0; i < (b.length-1); i++) {
        var temp1=b.charAt(i);
        var temp2=b.charAt(i+1);
        if ((espacio(temp1)==true)&&(espacio(temp2)==true)) {
            salida=salida+"";
        } else {salida=salida+temp1}
    }
    salida=salida+b.charAt(b.length)
    return salida
}

// Write your code here
function espacio(a) {
    if (a==" ") { var a=true} else { var a= false}
    return a
}
function removespaceandpoint(b) {
    var salida="";
    for (var i = 0; i < (b.length-1); i++) {
        var temp1=b.charAt(i);
        var temp2=b.charAt(i+1);
        if (((espacio(temp1)==true)&&(espacio(temp2)==true))||(temp1==".")) {
            salida=salida+"";
        } else {salida=salida+temp1}
    }
    if (b.charAt(b.length)==".") {salida=salida} else {salida=salida+b.charAt(b.length)}
    return salida
}

// Ejecución del código
process.stdin.resume();
process.stdin.setEncoding("utf-8");
var stdin_input = "";

process.stdin.on("data", function (input) {
    stdin_input += input;                               // Reading input from STDIN
});

process.stdin.on("end", function () {
   main(stdin_input);
});

function main(input) {
    process.stdout.write(removespaceandpoint(input));       // Writing output to STDOUT
}
