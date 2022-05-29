import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Volume

class Volume(gn.Mesh):
    """ Data socket Volume

    Methods
    -------
        to_mesh                   : mesh         (Mesh)
    """

    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_mesh(self, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID'):
        """Call node VolumeToMesh (GeometryNodeVolumeToMesh)

        Sockets arguments
        -----------------
            volume         : Volume (self)
            voxel_size     : Float
            voxel_amount   : Float
            threshold      : Float
            adaptivity     : Float

        Parameters arguments
        --------------------
            resolution_mode: 'GRID' in [GRID, VOXEL_AMOUNT, VOXEL_SIZE]

        Returns
        -------
            Mesh
        """

        return nodes.VolumeToMesh(volume=self, voxel_size=voxel_size, voxel_amount=voxel_amount, threshold=threshold, adaptivity=adaptivity, resolution_mode=resolution_mode).mesh


