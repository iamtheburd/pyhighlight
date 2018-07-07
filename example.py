# example.py (c) 2018 Tyler Burdsall

import pyhighlight as ph

# Assuming we want to highlight buildings A, B, and C
# from the example image
points = {
    'A': [[45, 156], [155, 50], [156, 160]],
    'B': [[37, 253], [206, 253], [206, 276], [90, 276], [90, 297], [206, 297],
         [206, 330], [90, 330], [90, 352], [210, 352], [210, 386], [37, 386]],
    'C': [[352, 57], [518, 57], [518, 128], [410, 128], [410, 190], [352, 190]]
}

test = ph.pyhighlight('example_buildings.png')
test.highlight(points['A'])
test.highlight(points['B'], color='red', transparency=0.5)
test.highlight(points['C'], color='green')

test.save('example.png')