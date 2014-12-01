"""Definition of the RunInstruction content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from uwosh.itdocs import itdocsMessageFactory as _
from uwosh.itdocs.interfaces import IRunInstruction
from uwosh.itdocs.config import PROJECTNAME

from Products.ATContentTypes.configuration import zconf

import time
from DateTime import DateTime

RunInstructionSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

     atapi.StringField(
        'program',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label="Program/Report",
            description="Program name",
        ),
        default="",
        required=True
    ),     

     atapi.DateTimeField(
        'revision',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label='Revision',
            description='The date of the last revision',
            format='%d, %m, %Y',
            show_hm=False,
            starting_year=time.localtime()[0],
        ),    
        required=True,
    ),

     atapi.StringField(
        'title',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label="Title",
            description="",
        ),
        default="",
        required=True,
    ),

    atapi.TextField(
        'function',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label='Function',
            description='Function of instruction',
            rows = 5,
            ),
        default='',
        required=True,
    ),

      atapi.StringField(
        'operation',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label="Operation",
            description="How to run the instruction",
            size=50,
        ),
        default=_(u"Home >  >  >"),
        required=True,
    ),
     
        atapi.TextField(
        'additional',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label="Additional Information",
            description="Other information that may be of use",
            rows=10
        ),
        default="",       
    ),

         

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

RunInstructionSchema['title'].widget.label = _(u'Project Title')


class RunInstruction(folder.ATFolder):
    """Describes Run Instrcuction for Administrative Computing"""
    implements(IRunInstruction)

    meta_type = "RunInstruction"
    schema = RunInstructionSchema


    fields_that_i_want = ['program', 'revision', 'title', 'function', 'operation', 'additional']

    def getInterestedFields(self):
       return [f for f in self.schema.fields() if f.__name__ in self.fields_that_i_want]

    
atapi.registerType(RunInstruction, PROJECTNAME)
