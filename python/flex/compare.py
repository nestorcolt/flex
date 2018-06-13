""" compare contains source and target comparing functions

*Module description*

:module: flex.compare
"""

# imports
from maya import cmds


def get_shapes_from_group(group):
    """ Gets all object shapes existing inside the given group

    :param group: maya transform node
    :type group: string

    :return: list of shapes objects
    :rtype: list str

    .. important:: only mesh shapes are returned for now
    """

    # checks if exists inside maya scene
    if not cmds.objExists(group):
        return None

    # gets shapes inside the given group
    shapes = cmds.ls(group, dagObjects=True, noIntermediate=True,
                     exactType=('mesh'))

    return shapes or None
