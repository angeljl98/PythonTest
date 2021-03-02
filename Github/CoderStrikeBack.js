/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/


// game loop
potencia=90
time1=0
bool1=true
d1=0
d2=0
ct1=0
lap1=0
lap2=0
bool2=true
bool3=true
boost1=0
boost2=0
boost3=0
boost4=0
boost5=0
boost6=0
miArray = [1,2,3];
miArray[1]=55;

while (true) {
    var inputs = readline().split(' ');
    const x = parseInt(inputs[0]);
    const y = parseInt(inputs[1]);
    const nextCheckpointX = parseInt(inputs[2]); // x position of the next check point
    const nextCheckpointY = parseInt(inputs[3]); // y position of the next check point
    const nextCheckpointDist = parseInt(inputs[4]); // distance to the next checkpoint
    const nextCheckpointAngle = parseInt(inputs[5]); // angle between your pod orientation and the direction of the next checkpoint
    var inputs = readline().split(' ');
    const opponentX = parseInt(inputs[0]);
    const opponentY = parseInt(inputs[1]);

    // Write an action using console.log()
    // To debug: console.error('Debug messages...');
    inc_x = 1000
    inc_y = 0
    // Retorna un entero aleatorio entre min (incluido) y max (excluido)
    // ¡Usando Math.round() te dará una distribución no-uniforme!
    function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min)) + min;
    }
        function CalcDistance(x, y) {
        return Math.sqrt(Math.pow(x-nextCheckpointX,2)+Math.pow(y-nextCheckpointY,2));
    }
    function LadderAnd(z1,z2) {
        if ((z1==true)&&(z2==true)){z3=true}else{z3=false}
        return z3;
    }
    function LadderOr(z1,z2) {
        if ((z1==true)||(z2==true)){z3=true}else{z3=false}
        return z3;
    }
        function Laps(d) {
        if (d!=d1){
            d1=d;
            ct1+=1;
            }
        return ct1;
    }
    function getMaxOfArray(numArray) {
        return Math.max.apply(null, numArray);
        }

    function Turbo(pot,d,lap,alt) {
        lap_int1=lap;
        if ((boost1==0)&&(boost2==0)&&(boost3==0)&&(boost4==0)&&(boost5==0)) {
            boost1=1
            stage=1
            }
        if ((lap>3)&&(boost1==1)&&(boost2==0)&&(boost3==0)&&(boost4==0)&&(boost5==0)) {
            boost1=0;
            boost2=1;
            stage=2;
            }
        if ((pot==100)&&(d>8000)&&(boost1==0)&&(boost2==1)&&(boost3==0)&&(boost4==0)&&(boost5==0)) {
            boost2=0;
            boost3=1;
            stage=3;
            }
        if ((alt==20)&&(boost1==0)&&(boost2==0)&&(boost3==1)&&(boost4==0)&&(boost5==0)){
            boost3=0;
            boost4=1;
            stage=4;
            }
        if ((boost1==0)&&(boost2==0)&&(boost3==0)&&(boost4==1)&&(boost5==0)) {
            boost4=0;
            boost5=1;
            stage=5;
            }

        return stage;
        }

    const min_rand_x = getRandomInt(0,100);
    const min_rand_y = getRandomInt(0,100);
    if ((min_rand_x >= 0)&&(x>nextCheckpointX)) {
        inc_x = 300;
        } else {
        inc_x = -300;
        }
    nextCheckpointX_print=nextCheckpointX+inc_x
    if ((min_rand_y >= 0)&&(y>nextCheckpointY)) {
        inc_y = 200;
        } else {
        inc_y = -200;
        }
    nextCheckpointY_print=nextCheckpointY+inc_y
    actual_distance=Math.round(CalcDistance(x,y))
    pct_distance=Math.round(100*actual_distance/18357)

    if (pct_distance<10) {
            multiplicador1 = 1
            alternativa1=20
        } else {
            multiplicador1 = 0
            alternativa1=0
        }
    if ((nextCheckpointAngle>90)||(nextCheckpointAngle<-90)) {
            potencia=0
        } else if ((nextCheckpointAngle>80)||(nextCheckpointAngle<-80)) {
            potencia=45
        } else if ((nextCheckpointAngle>70)||(nextCheckpointAngle<-70)) {
            potencia=55
        } else if ((nextCheckpointAngle>60)||(nextCheckpointAngle<-60)) {
            potencia=65
        } else if ((nextCheckpointAngle>50)||(nextCheckpointAngle<-50)) {
            potencia=75
        } else if ((nextCheckpointAngle>40)||(nextCheckpointAngle<-40)) {
            potencia=85
        } else if ((nextCheckpointAngle>30)||(nextCheckpointAngle<-30)) {
            potencia=95
        } else {
            potencia=100
        }
        time1 += 1;
        CtLaps=Laps(nextCheckpointX);
        multiplicador2=Turbo(potencia,nextCheckpointDist,CtLaps,alternativa1)
        if (multiplicador2==3){
            potencia_print="BOOST";
        } else {
            potencia_print=(1-multiplicador1)*potencia+alternativa1
        }
        //potencia_print=80+multiplicador2
        //potencia_print=var7
    //potencia_print=Math.abs(nextCheckpointAngle/2)
    // You have to output the target position
    // followed by the power (0 <= thrust <= 100) or "BOOST"
    // i.e.: "x y thrust"
    console.log(nextCheckpointX_print + ' ' + nextCheckpointY_print + ' '+ potencia_print);
}
