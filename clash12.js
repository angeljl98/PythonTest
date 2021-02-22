// # he game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
// # 01 Test 1
// # Input
// # Expected output
// # 1
// # F 3
// # FFFFFF
// # 2
//
// # 02 Test 2
// # Input
// # Expected output
// # 2
// # F 3
// # A 4
// # FFFFFFAAAAAA
// # 3
// # 03 Test 3
// # Input
// # Expected output
// # 5
// # R 2
// # E 1
// # F 9
// # A 7
// # S 3
// # SEFRAREFASSREAFRAESRFARSERAFRASEARFFFF
// # 14
// # 04 Test 4
// # Input
// # Expected output
// # 26
// # A 8
// # B 2
// # C 4
// # D 3
// # E 2
// # F 1
// # G 2
// # H 6
// # I 5
// # J 4
// # K 3
// # L 9
// # M 5
// # N 6
// # O 7
// # P 8
// # Q 4
// # R 3
// # S 2
// # T 4
// # U 5
// # V 6
// # W 3
// # X 2
// # Y 1
// # Z 8
// # IMAGINEWASYOUREMOVALRAISINGGRAVITYUNSATIABLEUNDERSTOODOREXPRESSIONDISSIMILARSOSUFFICIENTITSPARTYEVERYHEARDANDEVENTGAYADVICEHEINDEEDTHINGSADIEUSINNUMBERSOUNEASYTOMANYFOURFACTINHEFAILMYHUNGITQUITNEXTDOOFITFIFTEENCHARMEDBYPRIVATESAVINGSITMRFAVOURABLECULTIVATEDALTERATIONENTREATIESYETMETSYMPATHIZEFURNITUREFORFEITEDSIROBJECTIONPUTCORDIALLYCONTINUEDSPORTSMEN
// # 108

t=[]
for(n=readline();n--;)
{
    [a,b]=readline().split` `
    t.push(a.repeat(b))
}
q=[...readline()].sort().join``
z=0
t.map(x=>z+=-1+q.split(x).length)
print(z)
