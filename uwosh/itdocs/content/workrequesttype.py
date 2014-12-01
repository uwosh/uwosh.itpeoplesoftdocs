"""Definition of the WorkRequestType content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from uwosh.itdocs import itdocsMessageFactory as _
from uwosh.itdocs.interfaces import IWorkRequestType
from uwosh.itdocs.config import PROJECTNAME

from Products.ATContentTypes.configuration import zconf



WorkRequestTypeSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'Project',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Project"),
            description=_(u"Work request number"),
        ),
        default=_(u"WR_"),
        required=True,
    ),

    atapi.TextField(
        'usercontact',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label='User Contact Information',
            description='Enter User Name and/or Department along with email and/or phone number',
            rows = 3,),
        default='Name: \nPhone: \nemail: ',
        required=True,
    ),
    
    atapi.StringField(
        'itcontact',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label = 'IT Contact',
            description = 'Enter the IT personel you are working with',
            rows = 1,),
        default='',
        required=True,
    ),
    
    atapi.TextField(
        'purpose',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u'Purpose'),
            rows = 20,
            description=_(u'Describe the purpose of the request'),
        ),
        default='',
        required=True,
    ),           
    
    atapi.TextField(
        'additionalinformation',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u'Additional Information'),
            rows = 15,
            description=_(u'Add any necessary additional information'),
        ),
        default='',
    ),    
    

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

WorkRequestTypeSchema['title'].storage = atapi.AnnotationStorage()
WorkRequestTypeSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(WorkRequestTypeSchema, moveDiscussion=False)

class WorkRequestType(base.ATCTContent):
    """Work Request Document"""
    implements(IWorkRequestType)

    meta_type = "WorkRequestType"
    schema = WorkRequestTypeSchema
    


atapi.registerType(WorkRequestType, PROJECTNAME)
