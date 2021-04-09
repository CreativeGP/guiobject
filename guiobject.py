#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class Direction(Enum):
    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3

class Dimension(Enum):
    WIDTH = 0
    HEIGHT = 1
    XPOS = 2
    YPOS = 3

class Object:
    typ = 0 # 0---
    anchor = set()
    size = (1,1)

    inner = []
    
    def __init__(self, typ, anchor, size):
        self.typ = typ
        self.anchor = anchor
        self.size = size

    def size_to_pixels(size, whole):
        if size == 1:
            return whole
        elif size == -1:
            return -1
        elif 0 < size and size < 1:
            return whole*size
        elif size > 1:
            return size

    def compute_inner_object_dimension(self):
        right_offset = 0
        left, right
        for i in inner:
            if size_to_pixels(i.size[WIDTH]) == -1:
                pass
            else:
                i.dim[WIDTH] = size_to_pixels(i.size[WIDTH], self.dim[WIDTH])

            if LEFT in i.anchor: left = i
            if RIGHT in i.anchor: right = i

        left.dim[XPOS] = 0
        right_offset = right.dim[WIDTH] = size_to_pixels(right.size[WIDTH])

        xpos = left.dim[WIDTH]
        for i in inner:
            if LEFT in i.anchor: continue
            
            if i.size[WIDTH] == 1:
                i.dim[XPOS] = self.dim[XPOS] * 1
            elif i.size[WIDTH] == -1:
                i.dim[XPOS] = self.dim[XPOS] + self.dim[WIDTH]*xpos
                i.dim[WIDTH] = self.dim[WIDTH]-xpos-right_offset
            elif 0 < i.size[WIDTH] and i.size[WIDTH] < 1:
                i.dim[XPOS] = self.dim[XPOS] + self.dim[WIDTH]*xpos
                xpos += i.size[WIDTH]
            elif i.size[WIDTH] > 1:
                i.dim[XPOS] = self.dim[XPOS] + self.dim[WIDTH]*xpos
                xpos = i.size[WIDTH] / self.dim[WIDTH]
        
    
    def new_object(self, obj):
        self.inner.append(obj)

    def onResize(self, new_size):
        pass

    def onRedraw(self, rect):
        pass



globalobject = Object(-1,{LEFT,RIGHT,TOP,BOTTOM},(1,1))

globalobject.new_object(Object(0,{TOP,LEFT,RIGHT},(1,30)))
globalobject.new_object(Object(0,{LEFT,BOTTOM},(0.2,-1)))
globalobject.new_object(Object(0,{RIGHT,BOTTOM},(0.8,-1)))

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
