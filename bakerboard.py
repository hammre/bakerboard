#!/usr/bin/env python

from datetime import datetime
import random
import sys

VERSION = '0.0'

nao = datetime.now()
naostring = "%04d-%02d-%02d %02d:%02d" % ( nao.year, nao.month, nao.day, nao.hour, nao.minute )
naofile = "%04d%02d%02d%02d%02d" % ( nao.year, nao.month, nao.day, nao.hour, nao.minute )

game = sys.stdout
game.write( '\n'.join( ('title BakerBoard %s' % naostring,
                        'strict-trade',
                        'domestic-trade',
                        'num-players 4',
                        'sevens-rule 1',
                        'victory-points 10',
                        'num-roads 15',
                        'num-bridges 0',
                        'num-ships 0',
                        'num-settlements 5',
                        'num-cities 4',
                        'num-city-walls 3',
                        'resource-count 19',
                        'develop-road 2',
                        'develop-monopoly 2',
                        'develop-plenty 2',
                        'develop-chapel 1',
                        'develop-university 1',
                        'develop-governor 1',
                        'develop-library 1',
                        'develop-market 1',
                        'develop-soldier 13',
                        'desc Generated by BakerBoard version %s at %s.' % ( VERSION, naostring )) ) )

tiles = []
for i in xrange( 4 ): tiles.append( 't' ) #trees    (wood)
for i in xrange( 4 ): tiles.append( 'p' ) #pasture  (sheep)
for i in xrange( 4 ): tiles.append( 'f' ) #field    (wheat)
for i in xrange( 3 ): tiles.append( 'h' ) #hill     (brick)
for i in xrange( 3 ): tiles.append( 'm' ) #mountain (ore)
for i in xrange( 1 ): tiles.append( 'd' ) #desert
random.shuffle( tiles )

ports = [ 'w', 'g', 'l', 'o', 'b', '?', '?', '?', '?' ]
random.shuffle( ports )

chitorder = [ 0, 1, 2, 6, 11, 15, 18, 17, 16, 12, 7, 3, 4, 5, 10, 14, 13, 8, 9 ]
chits4p = [ 5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11 ]
chits = [0 for i in xrange( 19 )]

for i in chitorder:
    if tiles[i] != 'd': chits[i] = chits4p.pop( 0 )

chits = [i for i in chits if i != 0]

game.write( '\n'.join( ('',
                        'chits %s' % ','.join( [str(i) for i in chits] ),
                        'map',
                        '-,-,s%c5,s,s%c4,s,-' % ( ports[0], ports[1] ),
                        '-,s,%c0,%c1,%c2,s%c4,-' % ( tiles[0], tiles[1], tiles[2], ports[2] ),
                        '-,s%c0,%c3,%c4,%c5,%c6,s' % ( ports[3], tiles[3], tiles[4], tiles[5], tiles[6] ),
                        's,%c7,%c8,%c9,%c10,%c11,s%c3' % ( tiles[7], tiles[8], tiles[9], tiles[10], tiles[11], ports[4] ),
                        '-,s%c0,%c12,%c13,%c14,%c15,s' % ( ports[5], tiles[12], tiles[13], tiles[14], tiles[15] ),
                        '-,s,%c16,%c17,%c18,s%c2,-' % ( tiles[16], tiles[17], tiles[18], ports[6] ),
                        '-,-,s%c1,s,s%c2,s,-' % ( ports[7], ports[8] ),
                        '.') ) )

game.close()

