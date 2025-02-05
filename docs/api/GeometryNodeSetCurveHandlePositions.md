# Node *Set Handle Positions*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)
- geonodes name: `SetHandlePositions`
- bl_idname: `GeometryNodeSetCurveHandlePositions`

```python
from geonodes import nodes

node = nodes.SetHandlePositions(curve=None, selection=None, position=None, offset=None, mode='LEFT')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetCurveHandlePositions.webp)

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)
- **position**: [Vector](Vector.md)
- **offset**: [Vector](Vector.md)

#### Node parameter arguments:

- **mode** (str): default = 'LEFT' in ('LEFT', 'RIGHT')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[ControlPoint](ControlPoint.md)** |
| [set_handle_positions](ControlPoint.md#set_handle_positions) | `def set_handle_positions(self, position=None, offset=None, mode='LEFT'):` |
| [set_left_handle_positions](ControlPoint.md#set_left_handle_positions) | `def set_left_handle_positions(self, position=None, offset=None):` |
| [set_right_handle_positions](ControlPoint.md#set_right_handle_positions) | `def set_right_handle_positions(self, position=None, offset=None):` |
| [left_handle_positions](ControlPoint.md#left_handle_positions) | `@left_handle_positions.setter
`<br> `def left_handle_positions(self, attr_value):` |
| [right_handle_positions](ControlPoint.md#right_handle_positions) | `@right_handle_positions.setter
`<br> `def right_handle_positions(self, attr_value):` |
| [left_handle_offset](ControlPoint.md#left_handle_offset) | `@property`<br> `def left_handle_offset(self):` |
| [left_handle_offset](ControlPoint.md#left_handle_offset) | `@left_handle_offset.setter
`<br> `def left_handle_offset(self, attr_value):` |
| [right_handle_offset](ControlPoint.md#right_handle_offset) | `@property`<br> `def right_handle_offset(self):` |
| [right_handle_offset](ControlPoint.md#right_handle_offset) | `@right_handle_offset.setter
`<br> `def right_handle_offset(self, attr_value):` |

<sub>Go to [top](#node-Set-Handle-Positions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

