"""


    Helper methods.

"""

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.config import REFERENCE_CATALOG

def getResearcherThemes(researcher):
    """
    Look all Programme contents which refer to this researcher. 
    
    
    Relationship Programme <-> Researcher is defined in Programme as::
    
      atapi.ReferenceField(
        name='researchers',
        widget=ReferenceBrowserWidget(
            label="Researchers",
            description="Researchers involved in this project",
            base_query={'object_provides': IResearcher.__identifier__ },
            allow_browse=0,
            show_results_without_query=1,
        ),
        multiValued=1,
        relationship="researchers_in_theme"
      ),

    
    @param researcher: Content item on the site
    
    """

    # Do acquisition look-up
    reference_catalog = getToolByName(researcher, REFERENCE_CATALOG)
    
    # relationship: field name used
    # Plone 4.1: objects=True argument to fetch full objects, not just index brains        
    references = reference_catalog.getBackReferences(researcher, relationship="researchers_in_theme")
    # Resolve Reference objects to full objects
    # Return a generator method which will yield all full objects
    return [ ref.getSourceObject() for ref in references ] 
    
    
    
    