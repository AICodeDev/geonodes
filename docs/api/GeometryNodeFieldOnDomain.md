# Node *Evaluate on Domain*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/v.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
- geonodes name: `EvaluateOnDomain`
- bl_idname: `GeometryNodeFieldOnDomain`

```python
from geonodes import nodes

node = nodes.EvaluateOnDomain(value=None, data_type='FLOAT', domain='POINT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldOnDomain.webp)

### Args:

#### Input socket arguments:

- **value**: **data_type** dependant

#### Node parameter arguments:

- **data_type** (str): default = 'FLOAT' in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- **domain** (str): default = 'POINT' in ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')

### Output sockets:

- **value** : ``data_type`` dependant

#### Shared sockets:

- Driving parameter : ``data_type`` in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
- Input sockets  : ['value']
- Output sockets : ['value']

<sub>Go to [top](#node-Evaluate-on-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

