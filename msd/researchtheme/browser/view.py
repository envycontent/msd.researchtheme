from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

class ResearchThemeView(BrowserView):
    
    
    def content_item_id(self):
        return self.context.getId()
    
    def hasFullText(self):
        strAddText = self.context.getText()
        
        if len(strAddText) > 0:
            return True   
        else:
            return False
            
    def hasLink(self):
        strLink = self.context.getRemoteUrl()
        
        #if blank then hasLink is false
        
        if len(strLink) == 0:
            return False
            
        #if the default string has been left untouched
            
        if strLink == 'http://':
            return False
            
        return True
        
    def linkCaption(self):
        strLinkCaption = self.context.getLinkCaption()
        
        if len(strLinkCaption) == 0:
            
            return self.context.getRemoteUrl()
            
        else:
            
            return strLinkCaption
            
    def relatedResearchers(self):
        
        res = ()
        catalog = getToolByName(self.context, 'portal_catalog')
        related = self.context.getRawResearchers()
        if not related:
            return ()
        brains = catalog(UID=related)
        if brains:
            # build a position dict by iterating over the items once
            positions = dict([(v, i) for (i, v) in enumerate(related)])
            # We need to keep the ordering intact
            res = list(brains)
            def _key(brain):
                return positions.get(brain.UID, -1)
            res.sort(key=_key)
        return res
     
            
