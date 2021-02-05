function dist(a,b) {
    return Math.pow((Math.pow((a.x -b.x),2)+Math.pow((a.y -b.y),2)),0.5)
};
let entidad=class{
    constructor(id,tipo,x,y,arg1,arg2,arg3,arg4) {
        this.id=id;
        this.tipo=tipo;
        this.x=x;
        this.y=y;
        this.arg1=arg1;
        this.arg2=arg2;
        this.arg3=arg3;
        this.arg4=arg4;
    }
};
var n=0;
while (n<2) { //true
    n=n+1;
    const myShipCount = 1 //parseInt(readline()); // the number of remaining ships
    const entityCount = 2 //parseInt(readline()); // the number of entities (e.g. ships, mines or cannonballs)
    let arrayObjetos = []; //objeto vacío
    let arrayBarcos = []; //objeto vacío barcos
    for (let i = 0; i < entityCount; i++) {
        //var inputs = readline().split(' ');
        const entityId = "1"; //parseInt(inputs[0]); // Id del objeto
        const entityType = "SHIP"; //inputs[1]; // Tipo
        const x = 10; //parseInt(inputs[2]);  // Eje x
        const y = 10; //parseInt(inputs[3]);  // Eje y
        const arg1 = 4; //parseInt(inputs[4]); //Rotación
        const arg2 = 2; //parseInt(inputs[5]); //Velocidad
        const arg3 = 100; //parseInt(inputs[6]);   //Rums
        const arg4 = 1; //parseInt(inputs[7]);   // 1 - si es mio 0 - boss
        let Obj = new entidad(entityId,entityType,x,y,arg1,arg2,arg3,arg4);
        if ((entityType=="SHIP")&&(arg4==1)) {
          let
        }
        let NueObj = arrayObjetos.push(Obj);
        //let entidad = Entity(entityId,entityType,x,y,arg1,arg2,arg3,arg4);
        //let nuevoObjeto=arrayObjetos.push(entidad);
    }
    for (let i = 0; i < myShipCount; i++) {
        for (let j = 0; j<entityCount;j++){
          var Ordenado = arrayObjetos {
          arrayObjetos.sort((a,b)=>{
            var m = a[2]*a[3];
            var n = b[2]*b[3];
            return m - n;
            });
          }
        }
        console.log('MOVE 11 10'); // Any valid action, such as "WAIT" or "MOVE x y"
        console.log(arrayObjetos);
        console.log(n);
    }
}
