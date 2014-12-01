"""Definition of the Meeting Notes content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from uwosh.itdocs import itdocsMessageFactory as _
from uwosh.itdocs.interfaces import IMeetingNotes
from uwosh.itdocs.config import PROJECTNAME

from Products.ATContentTypes.configuration import zconf

import time

MeetingNotesSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.StringField(
        'Project',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Project"),
            description=_(u"Work request number"),
        ),
        default=_(u"WR_"),
    ),
    
    atapi.DateTimeField(
        'meetingdate',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label='Meeting Date',
            description='The date of the meeting',
            format='%d, %m, %Y',
            show_hm=False,
            starting_year=time.localtime()[0],
        ),
        default='',
        required=True,
    ),
    
    atapi.TextField(
        'present',
        storage=atapi.AnnotationStorage(),
        widget=atapi.TextAreaWidget(
            label='Participants',
            description='List the names of those present',
            rows = 3,),
        default='',
        required=True,
    ),
    
    atapi.TextField(
        'requirements',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label='Requirements and Decisions',
            description='Note any necessary requirements and/or decisions made',
            rows=20,
        ),
        default='',
    ),
    
    atapi.TextField(
        'questions',
        storage=atapi.AnnotationStorage(),
        widget=atapi.RichWidget(
            label='Questions and Problems',
            description='Note questions or problems that arose',
            rows=20,
        ),
        default='',
    ),
    
    


))


# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

MeetingNotesSchema['title'].storage = atapi.AnnotationStorage()
MeetingNotesSchema['description'].storage = atapi.AnnotationStorage()


class MeetingNotes(base.ATCTContent):
    """Meeting Notes Document"""
    implements(IMeetingNotes)

    meta_type = "MeetingNotes"
    schema = MeetingNotesSchema    


atapi.registerType(MeetingNotes, PROJECTNAME)


