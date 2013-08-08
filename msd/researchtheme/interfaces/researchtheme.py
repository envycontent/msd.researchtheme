from zope import schema
from zope.interface import Interface


from msd.researchtheme import researchthemeMessageFactory as _

class IResearchTheme(Interface):
    """A research theme with image and link"""
    
    # -*- schema definition goes here -*-
    # 

class IResearchThemeFolderView(Interface):
    """A marker interface for a folder full of research themes"""


