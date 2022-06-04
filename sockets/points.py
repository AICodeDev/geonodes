import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Points

class Points(Geometry):
    """ Class Points
    

    | Inherits from: Geometry 
    

    Methods
    =======
    - instance_on_points : instances (Instances) 
    - to_vertices        : mesh (Mesh) 
    - to_volume          : volume (Volume) 
    

    Stacked methods
    ===============
    - set_radius : Points 
    """


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """Call node InstanceOnPoints (GeometryNodeInstanceOnPoints)

        Sockets arguments
        -----------------
            points         : Points (self)
            selection      : Boolean
            instance       : Geometry
            pick_instance  : Boolean
            instance_index : Integer
            rotation       : Vector
            scale          : Vector

        Returns
        -------
            Instances
        """

        return nodes.InstanceOnPoints(points=self, selection=selection, instance=instance, pick_instance=pick_instance, instance_index=instance_index, rotation=rotation, scale=scale).instances

    def to_vertices(self, selection=None):
        """Call node PointsToVertices (GeometryNodePointsToVertices)

        Sockets arguments
        -----------------
            points         : Points (self)
            selection      : Boolean

        Returns
        -------
            Mesh
        """

        return nodes.PointsToVertices(points=self, selection=selection).mesh

    def to_volume(self, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT'):
        """Call node PointsToVolume (GeometryNodePointsToVolume)

        Sockets arguments
        -----------------
            points         : Points (self)
            density        : Float
            voxel_size     : Float
            voxel_amount   : Float
            radius         : Float

        Parameters arguments
        --------------------
            resolution_mode: 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

        Returns
        -------
            Volume
        """

        return nodes.PointsToVolume(points=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, radius=radius, resolution_mode=resolution_mode).volume


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_radius(self, selection=None, radius=None):
        """Call node SetPointRadius (GeometryNodeSetPointRadius)

        Sockets arguments
        -----------------
            points         : Points (self)
            selection      : Boolean
            radius         : Float

        Returns
        -------
            self

        """

        return self.stack(nodes.SetPointRadius(points=self, selection=selection, radius=radius))


