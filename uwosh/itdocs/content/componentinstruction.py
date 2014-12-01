"""Definition of the Component Instruction content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from uwosh.itdocs import itdocsMessageFactory as _
from uwosh.itdocs.interfaces import IComponentInstruction
from uwosh.itdocs.config import PROJECTNAME

from Products.ATContentTypes.configuration import zconf


ComponentInstructionSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.StringField(
        'Project',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Component"),
            description=_(u"Component name or label"),
        ),
        default=_(''),
    ),   
    
    atapi.TextField(
        'questions',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Function"),
            description=_(u"Describe the function of the component"),
            rows=10,
        ),
        default='',
    ),
    
# run instructions need to be implemented
    
    atapi.TextField(
        'questions',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label=_(u"Additional Information"),
            description=_(u"ex: Information for the system is in the document: _SystemInfo.doc"),
            rows=20,
        ),
        default='',
    ),    
    
))


# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ComponentInstructionSchema['title'].storage = atapi.AnnotationStorage()
ComponentInstructionSchema['description'].storage = atapi.AnnotationStorage()


class ComponentInstruction(base.ATCTContent):
    """ComponentInstruction Document"""
    implements(IComponentInstruction)

    meta_type = "ComponentInstructio"
    schema = ComponentInstructionSchema    


atapi.registerType(ComponentInstruction, PROJECTNAME)



