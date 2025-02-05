# Node *Voronoi Texture*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)
- geonodes name: `VoronoiTexture`
- bl_idname: `ShaderNodeTexVoronoi`

```python
from geonodes import nodes

node = nodes.VoronoiTexture(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexVoronoi.webp)

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)
- **w**: [Float](Float.md)
- **scale**: [Float](Float.md)
- **smoothness**: [Float](Float.md)
- **exponent**: [Float](Float.md)
- **randomness**: [Float](Float.md)

#### Node parameter arguments:

- **distance** (str): default = 'EUCLIDEAN' in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
- **feature** (str): default = 'F1' in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
- **voronoi_dimensions** (str): default = '3D' in ('1D', '2D', '3D', '4D')

### Output sockets:

- **distance** : [Float](Float.md)
- **color** : [Color](Color.md)
- **position** : [Vector](Vector.md)
- **w** : [Float](Float.md)
- **radius** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Texture](Texture.md)** |
| [Voronoi](Texture.md#Voronoi) | `@staticmethod`<br> `def Voronoi(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):` |
| [Voronoi1D](Texture.md#Voronoi1D) | `@staticmethod`<br> `def Voronoi1D(w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):` |
| [Voronoi2D](Texture.md#Voronoi2D) | `@staticmethod`<br> `def Voronoi2D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):` |
| [Voronoi3D](Texture.md#Voronoi3D) | `@staticmethod`<br> `def Voronoi3D(vector=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):` |
| [Voronoi4D](Texture.md#Voronoi4D) | `@staticmethod`<br> `def Voronoi4D(vector=None, w=None, scale=None, smoothness=None, exponent=None, randomness=None, distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D'):` |

<sub>Go to [top](#node-Voronoi-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

