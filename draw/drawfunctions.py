#!/usr/bin/env python

import python_libs.hollowtext as hollowtext

def draw_text(surface, text, position, align="none", font="", color=(0, 255, 0), outline=True, outline_color=(1, 1, 1)):	
	label = font.render(text, 1, color)
	if position[0] == "right":
		x = screensize[0]
	elif position[0] == "left":
		x = 0
	else:
		x = position[0]		
	if position[1] == "top":
		y = 0
	elif position[1] == "bottom":
		y = screensize[1]-font.get_height()
	else:
		y = position[1]
	if align == "left":
		x = x
	elif align == "right":
		x = x-label.get_width()
	elif align == "center":
		x = x-(label.get_width()/2)		
	pos = (x, y)
	if outline == True:
		text = hollowtext.textOutline(font, text, color, outline_color)
		surface.blit( text, (pos[0], pos[1]))
	else:
		surface.blit( label, (pos[0], pos[1]))

def draw_image(surface, img, position, align="none"):
	x = position[0]
	y = position[1]
	if align == "right":
		x = x-img.get_width()
	elif align == "center":
		x = x-(img.get_width()/2)
	surface.blit(img, (x, y))
