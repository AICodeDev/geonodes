# Node *White Noise Texture*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)
- geonodes name: `WhiteNoiseTexture`
- bl_idname: `ShaderNodeTexWhiteNoise`

```python
from geonodes import nodes

node = nodes.WhiteNoiseTexture(vector=None, w=None, noise_dimensions='3D')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)
- **w**: [Float](Float.md)

#### Node parameter arguments:

- **noise_dimensions** (str): default = '3D' in ('1D', '2D', '3D', '4D')

### Output sockets:

- **value** : [Float](Float.md)
- **color** : [Color](Color.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Texture](Texture.md)** |
| [WhiteNoise](Texture.md#WhiteNoise) | `@staticmethod`<br> `def WhiteNoise(vector=None, w=None, noise_dimensions='3D'):` |
| [WhiteNoise1D](Texture.md#WhiteNoise1D) | `@staticmethod`<br> `def WhiteNoise1D(w=None):` |
| [WhiteNoise2D](Texture.md#WhiteNoise2D) | `@staticmethod`<br> `def WhiteNoise2D(vector=None):` |
| [WhiteNoise3D](Texture.md#WhiteNoise3D) | `@staticmethod`<br> `def WhiteNoise3D(vector=None):` |
| [WhiteNoise4D](Texture.md#WhiteNoise4D) | `@staticmethod`<br> `def WhiteNoise4D(vector=None, w=None):` |

<sub>Go to [top](#node-White-Noise-Texture) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

