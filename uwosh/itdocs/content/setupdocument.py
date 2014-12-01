"""Definition of the SetupDocument content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from uwosh.itdocs import itdocsMessageFactory as _
from uwosh.itdocs.interfaces import ISetupDocument
from uwosh.itdocs.config import PROJECTNAME

from Products.ATContentTypes.configuration import zconf

SetupDocumentSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

#     atapi.StringField('purpose',
#         storage=atapi.AnnotationStorage(),
#         widget=atapi.StringWidget(label=_(u'Purpose'),
#                                   description=_(u'Purpose of document'),
#                                   size=80,),
#                       default=_(u"This document provides a quick reference for setting up [Project XXX]"),
#     ),

    atapi.StringField('audience',
        widget=atapi.StringWidget(label=_(u'Audience'),
                                  description=_(u'The audience for this document'),
                                  size=80,),
                      default=_(u"[XXX], Administrative Computing staff"),
    ),

#     atapi.TextField('appliesto',
#         storage=atapi.AnnotationStorage(),
#         default_output_type = 'text/x-html-safe',
#         widget=atapi.RichWidget(label=_(u'Applies to'), rows = 25,
#                                   description=_(u'Projects and business process owners this document applies to'),
#                                 allow_file_upload = zconf.ATDocument.allow_document_upload,),
#                     default='<table class="grid listing"> <tbody> <tr> <td>Projects</td> <td>Business Process Owner</td> </tr> <tr> <td>&lt;WORK REQUEST></td> <td>&lt;business owner></td> </tr> </tbody> </table> <p><br /> <br /> <br /><br /></p>',
#     ),

    atapi.TextField('navigations',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'Navigations'), rows = 25,
                                  description=_(u'Pages, components, persons responsible, and navigations'),),
                    default='<table class="grid listing"> <tbody> <tr> <td class="td1"> <p class="p1"><strong>Page</strong></p> </td> <td class="td2"> <p class="p1"><strong>Component</strong></p> </td> <td class="td3"> <p class="p1"><strong>Who</strong></p> </td> <td class="td4"> <p class="p1"><strong>Navigation</strong></p> </td> </tr> <tr> <td class="td5"> <p class="p2">&lt;Component Lable></p> </td> <td class="td6"> <p class="p3">&lt;Component Name></p> </td> <td class="td7"> <p class="p3">&lt;responsible person></p> </td> <td class="td8"> <p class="p2">&lt;PS Portal Navigation></p> </td> </tr> <tr> <td class="td5"> <p class="p4">Example:</p> <p class="p4">Test Component Table</p> </td> <td class="td6"> <p class="p4">PS Delivered</p> </td> <td class="td7"> <p class="p4">Julie</p> </td> <td class="td8"> <p class="p5"><span class="s1"><a href="https://titanadmin3.uwosh.edu/psc/titanadm_pgm/EMPLOYEE/HRMS/s/WEBLIB_PTPP_SC.HOMEPAGE.FieldFormula.IScript_AppHP?scname=PT_PTPP_PORTAL_ROOT&amp;pt_fname=PT_PTPP_PORTAL_ROOT&amp;PortalCacheContent=true&amp;PSCache-Control=role%2cmax-age%3d60">Main Menu</a></span><span class="s2"> >&nbsp;<a href="https://titanadmin3.uwosh.edu/psc/titanadm_pgm/EMPLOYEE/HRMS/s/WEBLIB_PTPP_SC.HOMEPAGE.FieldFormula.IScript_AppHP?scname=HCCC_DESIGN_STUDENT_ADMINISTRA&amp;secondary=true&amp;fname=HCCC_DESIGN_STUDENT_ADMINISTRA&amp;pt_fname=HCCC_DESIGN_STUDENT_ADMINISTRA&amp;PortalCacheContent=true&amp;PSCache-Control=role%2cmax-age%3d60"><span class="s1">Set Up SACR</span></a> >&nbsp;<a href="https://titanadmin3.uwosh.edu/psc/titanadm_pgm/EMPLOYEE/HRMS/s/WEBLIB_PTPP_SC.HOMEPAGE.FieldFormula.IScript_AppHP?scname=HCCC_SETUP_PRODUCT_RELATED&amp;secondary=true&amp;fname=HCCC_SETUP_PRODUCT_RELATED&amp;pt_fname=HCCC_SETUP_PRODUCT_RELATED&amp;PortalCacheContent=true&amp;PSCache-Control=role%2cmax-age%3d60"><span class="s1">Product Related</span></a> >&nbsp;<a href="https://titanadmin3.uwosh.edu/psc/titanadm_pgm/EMPLOYEE/HRMS/s/WEBLIB_PTPP_SC.HOMEPAGE.FieldFormula.IScript_AppHP?scname=HCCC_DESIGN_ADMISSIONS&amp;secondary=true&amp;fname=HCCC_DESIGN_ADMISSIONS&amp;pt_fname=HCCC_DESIGN_ADMISSIONS&amp;PortalCacheContent=true&amp;PSCache-Control=role%2cmax-age%3d60"><span class="s1">Recruiting and Admissions</span></a> >&nbsp;Test Component Table</span></p> </td> </tr> </tbody> </table>',
    ),

    atapi.TextField('setup',
        storage=atapi.AnnotationStorage(),
        default_output_type = 'text/x-html-safe',
        widget=atapi.RichWidget(label=_(u'Setup'), rows = 25,
                                  description=_(u'Describe each setup step or requirement, including screen shots'),),
                    default='<ol> <li>&lt;enter each setup step or requirement with screen shots to help></li> <li>Example Add a  Test Component Table entries</li></ol> <p>&nbsp;</p> <p>&nbsp;</p>',
    ),

#     atapi.TextField('formattingkey',
#         storage=atapi.AnnotationStorage(),
#         default_output_type = 'text/x-html-safe',
#         widget=atapi.RichWidget(label=_(u'Formatting Key'), rows = 25,
#                                   description=_(u'??? Notes, topic, and description'),),
#                     default='<table class="grid listing"> <tbody> <tr> <td>Notes</td> </tr> <tr> <td>Topic</td> </tr> <tr> <td>Description</td> </tr> </tbody> </table> <p><br /><br /><br /><br /></p>',
#     ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

SetupDocumentSchema['title'].widget.label = _(u'Project Title')

#SetupDocumentSchema['description'].widget.label = _(u'Purpose')
SetupDocumentSchema['description'].widget.description=_(u'Purpose of document')
SetupDocumentSchema['description'].default="This document provides a quick reference for setting up [Project XXX]"
SetupDocumentSchema['description'].visible = {'view':'visible', 'edit':'visible'}

schemata.finalizeATCTSchema(
    SetupDocumentSchema,
    folderish=True,
    moveDiscussion=False
)


class SetupDocument(folder.ATFolder):
    """UW Oshkosh Administrative Computing document for setup"""
    implements(ISetupDocument)

    meta_type = "SetupDocument"
    schema = SetupDocumentSchema

    
atapi.registerType(SetupDocument, PROJECTNAME)
