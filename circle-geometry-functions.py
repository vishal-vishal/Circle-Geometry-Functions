from math import pi
import math

def getCircumference(r):
    """function should calculate and return the circumference (perimeter) of this circle."""
    circumference = (2 * pi) * r
    return circumference


def getArea(r):
    """function should calculate and return the area of this circle."""
    area = pi * (r ** 2)
    return area


def getArcLength(r, a):
    """ function should calculate and return the length of this arc"""
    leng_arc = 2 * pi * r * (a / 360)
    return leng_arc


def getSectorPerimeter(r, a):
    """function should calculate and return the perimeter of this sector.. """
    per = (2*pi*r*(a/360)+2*r)
    return per


def getSectorArea(radius, angle):
    """function should calculate and return the area of this sector.."""
    area_sector = pi * (radius**2) * (angle/360)
    return area_sector


def getChordLength(radius, angle):
    """function should calculate and return the length of this chord.."""
    chord = 2 * radius * math.sin(angle/2)
    return chord


def getSegmentPerimeter(radius, angle):
    """function should calculate and return the area of this segment.."""
    seg_peri = ((2*pi * radius) * (angle/360)) + ((2 * radius) * math.sin(angle/2))
    return seg_peri

def getSegmentArea(radius, angle):
    """ function should calculate and return the area of this segment.."""
    segment_area = (radius**2)*(pi*(angle/360)-1/2*math.sin(angle))
    return segment_area


if __name__ == "__main__":
    r = 5
    a = 60
    circum = getCircumference(r)
    print(f"Circumference: {circum}")
    area = getArea(r)
    print(f"Area : {area}")
    length_arc = getArcLength(r, a)
    print(f"Arc length: {length_arc}")
    perimeter = getSectorPerimeter(r, a)
    print(f"Sector Perimeter : {perimeter}")
    sector_area = getSectorArea(r, a)
    print(f"Area of Sector: {sector_area}")
    chord_length = getChordLength(r, a)
    print(f"Chord : {chord_length}")
    segment_perimeter =  getSegmentPerimeter(r, a)
    print(f"Perimeter of Segment: {segment_perimeter}")
    area_segment = getSegmentArea(r, a)
    print(f"Area of Segment : {area_segment}")

