/** CLASES
 **/
let Entity=class{
    constructor(id,x,y) {
        this.x=x;
        this.y=y;
        this.id=id;
    }
}
function dist(a,b) {
    return Math.pow((Math.pow((a.x -b.x),2)+Math.pow((a.y -b.y),2)),0.5)
};
// game loop
while (true) {
    const myShipCount = parseInt(readline()); // the number of remaining ships
    const entityCount = parseInt(readline()); // the number of entities (e.g. ships, mines or cannonballs)
    barriles=[];
    misBarcos=[];
    otrosBarcos=[];

    for (let i = 0; i < entityCount; i++) {
        var inputs = readline().split(' ');
        const entityId = parseInt(inputs[0]);
        const entityType = inputs[1];
        const x = parseInt(inputs[2]);
        const y = parseInt(inputs[3]);
        const arg1 = parseInt(inputs[4]);
        const arg2 = parseInt(inputs[5]);
        const arg3 = parseInt(inputs[6]);
        const arg4 = parseInt(inputs[7]);
        entidad=new Entity(entityId,x,y);
        if (entityType=="BARREL"){
            barriles[0]=entidad;
            } else if ((entityType=="SHIP")&&(arg4==1)) {
            misBarcos[0]=entidad;
            } else if ((entityType=="SHIP")&&(arg4==0)) {
            otrosBarcos[0]=entidad;
            }
        }
    for (let i = 0; i < myShipCount; i++) {
        barriles.sort((a,b)=>{
            var m = a[2]*a[3];
            var n = b[2]*b[3];
            return m - n;
        });
        misBarcos.sort((a,b)=>{
            var m = a[2]*a[3];
            var n = b[2]*b[3];
            return m - n;
        });
        otrosBarcos.sort((a,b)=>{
            var m = a[2]*a[3];
            var n = b[2]*b[3];
            return m - n;
        });

        try{
            barril=barriles[0];
            miBarco1=misBarcos[0];
            otroBarco1=otrosBarcos[0];
            dist_Bo1=dist(miBarco1,otroBarco1);
            dist_Ba1=dist(miBarco1,barril);
        if (dist_Bo1<=4) {
            console.log("FIRE "+otroBarco1.x+" "+otroBarco1.y);
            } else if (true) {
            console.log("MOVE "+barril.x+" "+barril.y);
            } else {
            console.log("MOVE "+barril.x+" "+barril.y);
            }
        } catch (error) {
            //console.log("WAIT");
            console.log("MOVE 10 10")
        }
    }
}
