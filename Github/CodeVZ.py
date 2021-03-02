#/**
# * Save humans, destroy zombies!
# * https://www.codingame.com/ide/puzzle/code-vs-zombies
# **/

spartanSpeed = 1000
zombieSpeed = 400
killingDistance = 2000
speedDifferenceMultiplier = spartanSpeed / zombieSpeed

def getDistance(pointA, pointB):
    return ((pointA.x - pointB.x)**2-(pointA.y - pointB.y)**2)**0.5

#game loop
while (true):
    humans = []
    zombies = []
    spartanCoordinates = readline().split(' ')
    class human:
        def__init__(self,id,x,y,distance,alive)
            self.id=id
            self.x=x
            self.y=y
            self.nextX=0
            self.nextY=0
    masterChief = {'x': spartanCoordinates[0],'y': spartanCoordinates[1],'nextX': 0, 'nextY': 0}
    print('Master Chief 😎: ', masterChief)
    print('*********** New Turn Starts ⚔️ ************')
    humanCount = readline()
    for i in range(humanCount):
        zombieCount = readline()
        inputs = readline().split(' ')
        class human:
            def__init__(self,id,x,y,distance,alive)
                self.id=id
                self.x=x
                self.y=y
                self.distance=distance
                self.alive=alive
        human=getDistance(masterChief, human)
        humans_add=humans.append(human)
        humans = humans.sort() # necessary?
        ryan = "" # ryan or nemo?
    zombieCount = readline()
    for j  in range(zombieCount):
        inputs = readline().split(' ')
    // if we already have a ryan/nemo, skip the rest of the zombies
    if (ryan) continue;
    const zombie = {
      id: parseInt(inputs[0]),
      x: parseInt(inputs[1]),
      y: parseInt(inputs[2]),
      nextX: parseInt(inputs[3]),
      nextY: parseInt(inputs[4])
    };
    console.error(`Zombie #${zombie.id} vs humans: `, zombie);
    // can Master Chief reach any of the humans before this zombie? find nemo!
    let ryans = humans.filter(h => {
      console.error('---');
      console.error('Human: ', h);
      const hDistance = getDistance(zombie, h);
      console.error('Distance (zombie to human): ', hDistance);
      const isSpartanCloser = h.distance - killingDistance < hDistance;
      console.error('Is Master Chief Closer?: ', isSpartanCloser);
      return isSpartanCloser;
    });
    console.error('Ryans: ', ryans);
    // any ryans so far?
    if (ryans.length > 0) {
      // found a ryan!
      ryans = ryans.sort((a, b) => a.distance - b.distance);
      console.error(`Ryans: `, ryans);
      ryan = ryans[0];
      console.error(
        '- Cortana: Master Chief, we found Nemo! 🚨 RESCUE RYAN! 🚨'
      );
      // (this metaphor is out of control... 😅)
    }

    zombies.push(zombie); // do I need to store zombies?
    console.error('-----------------------------------------');
  }

  const next = ryan || humans[0];
  masterChief.nextX = next.x;
  masterChief.nextY = next.y;

  // Write an action using console.log()
  // To debug: console.error('Debug messages...');

  console.log(`${masterChief.nextX} ${masterChief.nextY}`); // Your destination coordinates
}
