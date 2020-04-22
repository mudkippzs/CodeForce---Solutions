GEO_DICT = {
    'Tetrahedron': 4,
    'Cube': 6,
    'Octahedron': 8,
    'Dodecahedron': 12,
    'Icosahedron': 20
}

inp = int(input())
faces = 0
for i in range(0, inp):
    faces += GEO_DICT[input()]
print(faces)