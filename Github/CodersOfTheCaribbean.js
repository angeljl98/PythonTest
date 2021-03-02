// Coders of the caribbean
/** CLASES
 **/
let Entity=class{
    constructor(id,x,y) {
        this.x=x;
        this.y=y;
        this.id=id;
    }
};
// game loop
while (true) {
    const myShipCount = parseInt(readline()); // the number of remaining ships
    const entityCount = parseInt(readline()); // the number of entities (e.g. ships, mines or cannonballs)
    barriles=[];
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
        }
    }
    for (let i = 0; i < myShipCount; i++) {
        barril=barriles[0];
        console.log("MOVE "+barril.x+" "+barril.y);
        //console.log('MOVE 11 10'); // Any valid action, such as "WAIT" or "MOVE x y"
    }
}
