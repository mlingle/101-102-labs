#   Matthew Lingle
#  ​ CSCI 102 – Section C
#   Week 11 Lab
#   References: None
#   Time: 45 minutes
def to_hex(decimal):
    sixtenth=decimal//16
    ones=decimal%16
    list1=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    hex1=list1[sixtenth]
    hex2=list1[ones]
    return hex1+hex2
def rgb_to_hex(rgb):
    red_hex=to_hex(rgb[0])
    green_hex=to_hex(rgb[1])
    blue_hex=to_hex(rgb[2])
    return red_hex+green_hex+blue_hex


