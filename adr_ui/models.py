from django.db import models
from django.utils.translation import gettext as _
#from django.utils.translation import gettext_lazy as _

# Create your models here.

class Status(models.Model):
    description = models.TextField()

    def __str__(self):
        return f'{self.description}'

class System(models.Model):
    createdAt = models.DateTimeField('date created'),
    name      = models.TextField()

    def __str__(self):
        return f'{self.name}'

class ADR(models.Model):
    createdAt = models.DateTimeField(auto_now=False, 
                                    null=True,
                                    help_text=_('Required. First date of consideration'),
                                    verbose_name = _('When ADR was created'),
                                    name=_('When ADR was created'),
                                    db_column='createdAt')
    context  = models.TextField(blank = False,
                                    default='',
                                    help_text=_('Required. Describe what circumstances lead you to this point.'),
                                    verbose_name = _('Decision context'),
                                    name=_('Decision context'),
                                    db_column='context')
    status   = models.ForeignKey(to=Status, 
                                    on_delete=models.PROTECT, 
                                    help_text=_('Required. Current status of the decision. Could be changed over time'),
                                    verbose_name = _('Decision context'),
                                    name=_('Decision context'),
                                    db_column='context'),
    decision = models.TextField(help_text=_('Required. Describe how do you overcome the obstracle.'),
                                    verbose_name = _('Decision'),
                                    name=_('Decision'),
                                    db_column='decision'),
    effects  = models.TextField(help_text=_('Required. Describe either effects on previous or future decisions'),
                                    verbose_name = _('Effects. Both positive and negative'),
                                    name=_('Effects'),
                                    db_column='effects'),  
    affects  = models.ManyToManyField(System, #on_delete=models.PROTECT,
                                    help_text=_('Required. Affected systems. Could be ALL, None or some in between'),
                                    verbose_name = _('Affected solutions'),
                                    name=_('Affected solutions'),
                                    db_column='affects')  
    projectLink = models.TextField( blank=True, 
                                    help_text=_('Optional. Link to jira project'),
                                    verbose_name = _('Project Link'),
                                    name=_('Project Link'),
                                    db_column='projectLink')
    statusChangedAt = models.DateTimeField(auto_now=True, 
                                    null=True,
                                    help_text=_('When status was changed'),
                                    verbose_name = _('When status was changed'),
                                    name=_('When status was changed'),
                                    db_column='statusChangedAt')

    def __str__(self):
        return f'ADR-{self.id}'