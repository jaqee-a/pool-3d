from mesh import Mesh
from triangle import Triangle



class ObjParser:



    @staticmethod
    def parse(file_path: str) -> Mesh:
        verts = []
        triangles = []
        with open(file_path) as f:
            for line in f.readlines():
                if line.startswith('v '):
                    verts.append(
                        [*map(float,line[2:].split()),]
                    )

                elif line.startswith('f '):
                    i1, i2, i3 = [*map(int,line[2:].split()),]
                    
                    triangles.append(
                        Triangle(
                            verts[i1-1],
                            verts[i2-1],
                            verts[i3-1]
                        )
                    )


        out = Mesh(pos=[0, 0, 15])
        out.triangles = triangles

        return out