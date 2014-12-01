"""Definition of the QueryInstructions content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from uwosh.itdocs import itdocsMessageFactory as _
from uwosh.itdocs.interfaces import IQueryInstructions
from uwosh.itdocs.config import PROJECTNAME

from Products.ATContentTypes.configuration import zconf

QueryInstructionsSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.TextField('operation',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.LabelWidget(label=_(u'Operation'), rows = 25,
                                  description=_(u'How to run this query'),),
                    default='',
    ),

    atapi.TextField('parameters',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'Parameters'), rows = 25,
                                  description=_(u'Parameters to enter for this query'),),
                    default='',
    ),

     atapi.TextField('additionalinfo',
         storage=atapi.AnnotationStorage(),
         default_output_type = 'text/x-html-safe',
         widget=atapi.RichWidget(label=_(u'Additional Information'), rows = 25,
                                   description=_(u''),),
                     default='Information for the system is in the document:  _SystemInfo.doc',
     ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

QueryInstructionsSchema['title'].widget.label = _(u'Query Name')

#QueryInstructionsSchema['description'].widget.label = _(u'Purpose')
QueryInstructionsSchema['description'].widget.description=_(u'Query Function')
QueryInstructionsSchema['description'].default=''
QueryInstructionsSchema['description'].visible = {'view':'visible', 'edit':'visible'}

schemata.finalizeATCTSchema(
    QueryInstructionsSchema,
    folderish=True,
    moveDiscussion=False
)


class QueryInstructions(folder.ATFolder):
    """Instructions for running a PeopleSoft query (UW Oshkosh Administrative Computing)"""
    implements(IQueryInstructions)

    meta_type = "QueryInstructions"
    schema = QueryInstructionsSchema

    
atapi.registerType(QueryInstructions, PROJECTNAME)
