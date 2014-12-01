"""Definition of the ProjectMigrationRequest content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from uwosh.itdocs import itdocsMessageFactory as _
from uwosh.itdocs.interfaces import IProjectMigrationRequest
from uwosh.itdocs.config import PROJECTNAME

from Products.ATContentTypes.configuration import zconf



ProjectMigrationRequestSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'Project',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Project Number"),
            description=_(u"Project reference(name or id)"),
        ),
        default=_(u""),
        required=True,
    ),

    atapi.TextField(
        'RequestMessage',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u'Request Message'),
            rows = 15,
            description=_(u'Migration request information'),
        ),
        default='',
    ),    
    

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

ProjectMigrationRequestSchema['title'].storage = atapi.AnnotationStorage()
ProjectMigrationRequestSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(ProjectMigrationRequestSchema, moveDiscussion=False)

class ProjectMigrationRequest(base.ATCTContent):
    """ProjectMigrationRequest Document"""
    implements(IProjectMigrationRequest)

    meta_type = "ProjectMigrationRequest"
    schema = ProjectMigrationRequestSchema
    


atapi.registerType(ProjectMigrationRequest, PROJECTNAME)
