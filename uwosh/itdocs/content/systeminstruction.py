"""Definition of the SystemInstruction content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from uwosh.itdocs import itdocsMessageFactory as _
from uwosh.itdocs.interfaces import ISystemInstruction
from uwosh.itdocs.config import PROJECTNAME

from Products.ATContentTypes.configuration import zconf



SystemInstructionSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'system',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"System"),
            description=_(u"System type"),
        ),
        default=_(u""),
        required=True,
    ),

    atapi.TextField(
        'function',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u'Function'),
            rows = 10,
            description=_(u'Function description'),
        ),
        default='',
    ),    
    
    #operation instructions

    atapi.TextField(
        'additionInformation',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u'Addition Information'),
            rows = 10,
            description=_(u'Additional information about the system instruction'),
        ),
        default='',
    ),    
    

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

SystemInstructionSchema['title'].storage = atapi.AnnotationStorage()
SystemInstructionSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(SystemInstructionSchema, moveDiscussion=False)

class SystemInstruction(base.ATCTContent):
    """System Instruction Document"""
    implements(ISystemInstruction)

    meta_type = "SystemInstruction"
    schema = SystemInstructionSchema
    


atapi.registerType(SystemInstruction, PROJECTNAME)
