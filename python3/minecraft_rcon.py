#!/bin/env python

from enum import Enum
from time import sleep

# https://github.com/ttk1/py-rcon
from rcon import Console


console = Console(host='localhost', password='py-rcon')


class BlockType(Enum):
    STONE = 'minecraft:stone'
    AIR = 'minecraft:air'


def set_block(x, y, z, block_type):
    console.command(f'setblock {x} {y} {z} {block_type.value}')


for i in range(5):
    sleep(2)
    for x in range(10, 30):
        for y in range(5, 10):
            for z in range(-200, -180):
                set_block(x, y, z, BlockType.STONE)

    sleep(2)
    for x in range(10, 30):
        for y in range(5, 10):
            for z in range(-200, -180):
                set_block(x, y, z, BlockType.AIR)
