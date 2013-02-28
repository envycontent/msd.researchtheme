"""Definition of the Research Theme content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

from Products.CMFPlone.interfaces import INonStructuralFolder
from msd.picturelink.content import picturelink
from msd.researchbase.content.researchschemas import SideBoxSchema


from msd.researchtheme import researchthemeMessageFactory as _
from msd.researchtheme.interfaces import IResearchTheme
from msd.researchtheme.config import PROJECTNAME

from msd.researchbase.interfaces import IResearcher

ResearchThemeSchema = picturelink.PictureLinkSchema.copy() + SideBoxSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    
    atapi.StringField(
        name='linkCaption',
        storage = atapi.AnnotationStorage(),
        required=False,
        #searchable=1,
        default = "Read more ...",
        #schemata ='default',
        widget=atapi.StringWidget(
            description = 'E.g.:"Read more ..." or "Personal Website", leave blank to show the link itself',
            label = _(u'label_url', default=u'Link Caption'),
        ),
        ),
     
     atapi.ReferenceField(
        name='researchers',
        widget=ReferenceBrowserWidget(
            label="Researchers",
            description="Researchers associated with this theme",
            base_query={'object_provides': IResearcher.__identifier__ },
            allow_browse=0,
            show_results_without_query=1,
        ),
        multiValued=1,
        relationship="researchers_in_theme"
),  

))


ResearchThemeSchema['remoteUrl'].widget.description = 'Website or page to link to, set to blank for no link'
ResearchThemeSchema.addField(schemata.relatedItemsField.copy())

schemata.finalizeATCTSchema(
    ResearchThemeSchema,
    moveDiscussion=False
)

class ResearchTheme(picturelink.PictureLink):
    """A researchtheme or short summary with image and link"""
    implements(IResearchTheme)

    meta_type = "ResearchTheme"
    schema = ResearchThemeSchema
    

    
    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    
    def getResearchThemeTitle(self):
        return self.Title()

atapi.registerType(ResearchTheme, PROJECTNAME)
