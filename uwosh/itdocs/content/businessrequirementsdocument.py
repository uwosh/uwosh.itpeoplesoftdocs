"""Definition of the BusinessRequirementsDocument content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from uwosh.itdocs import itdocsMessageFactory as _
from uwosh.itdocs.interfaces import IBusinessRequirementsDocument
from uwosh.itdocs.config import PROJECTNAME

from Products.ATContentTypes.configuration import zconf

BusinessRequirementsDocumentSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.TextField('businessworkflow',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'Business Workflow'), rows = 25,
                                  description=_(u''),),
                    default='Example created in MS Visio',
    ),

    atapi.TextField('businessrequirements',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'Business Requirements'), rows = 25,
                                  description=_(u''),),
                    default='',
    ),

    atapi.TextField('prerequisites',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'Prerequisites'), rows = 25,
                                  description=_(u''),),
                    default='<ol><li>&lt;enter each system setup or prerequisite that must be done first – general descriptions only&gt;</li></ol>',
    ),

    atapi.TextField('rules',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'Rules'), rows = 25,
                                  description=_(u''),),
                    default='<ol><li>&lt;enter each business rule or requirement – general descriptions only&gt;</li></ol>',
    ),

    atapi.TextField('process',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'Process'), rows = 25,
                                  description=_(u''),),
                    default='<ol><li>&lt;provide process steps and descriptions as outlined in the workflow above – general descriptions only, details as necessary&gt;</li></ol>',
    ),

    atapi.TextField('navigations',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'Navigations'), rows = 25,
                                  description=_(u''),),
                    default='See &lt;WORKREQUEST&gt;_BusReq.doc.',
    ),

    atapi.TextField('testscenarios',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'Test Scenarios'), rows = 25,
                                  description=_(u''),),
                    default='<p><table class="plain" width="482.4" cellspacing="0" cellpadding="0"> <tbody> <tr> <td > <p ><b>Test Scenario</b></p> </td> <td  > <p >&lt;Everything is fine in system&gt;</p> </td> </tr> <tr> <td  > <p ><b>Test Step</b></p> </td> <td  > <p ><b>Success Indicator</b></p> </td> </tr> <tr> <td  > <p >&lt;Step 1&gt;</p> </td> <td  > <p >&lt;success indicator&gt;</p> </td> </tr> <tr> <td  > <p >&lt;Step <span ><i>..n</i></span>&gt;</p> </td> <td  > <p >&lt;success indicator&gt;</p> </td> </tr> </tbody> </table> <p> <table class="plain" width="482.4" cellspacing="0" cellpadding="0" > <tbody> <tr> <td  > <p ><b>Test Scenario</b></p> </td> <td  > <p >&lt;anticipated issue or workflow branch 1&gt;</p> </td> </tr> <tr> <td  > <p ><b>Test Step</b></p> </td> <td  > <p ><b>Success Indicator</b></p> </td> </tr> <tr> <td  > <p >&lt;Step 1&gt;</p> </td> <td  > <p >&lt;success indicator&gt;</p> </td> </tr> <tr> <td  > <p >&lt;Step <span ><i>..n</i></span>&gt;</p> </td> <td  > <p >&lt;success indicator&gt;</p> </td> </tr> </tbody> </table> <p> <table class="plain" width="482.4" cellspacing="0" cellpadding="0" > <tbody> <tr> <td  > <p ><b>Test Scenario</b></p> </td> <td  > <p >&lt;anticipated issue or workflow branch ..<em>n</em>&gt;</p> </td> </tr> <tr> <td  > <p ><b>Test Step</b></p> </td> <td  > <p ><b>Success Indicator</b></p> </td> </tr> <tr> <td  > <p >&lt;Step 1&gt;</p> </td> <td  > <p >&lt;success indicator&gt;</p> </td> </tr> <tr> <td  > <p >&lt;Step <span ><i>..n</i></span>&gt;</p> </td> <td  > <p >&lt;success indicator&gt;</p> </td> </tr> </tbody> </table> <p> ',
    ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

BusinessRequirementsDocumentSchema['title'].widget.label = _(u'Project Title')

schemata.finalizeATCTSchema(
    BusinessRequirementsDocumentSchema,
    folderish=True,
    moveDiscussion=False
)


class BusinessRequirementsDocument(folder.ATFolder):
    """Describes business requirements for UW Oshkosh Administrative Computing"""
    implements(IBusinessRequirementsDocument)

    meta_type = "BusinessRequirementsDocument"
    schema = BusinessRequirementsDocumentSchema


atapi.registerType(BusinessRequirementsDocument, PROJECTNAME)
