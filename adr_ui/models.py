from pydoc import describe
from django.db import models
from django.utils.translation import gettext as _
from numpy import unique
#from django.utils.translation import gettext_lazy as _

# Create your models here.

class Status(models.Model):
    description = models.TextField( db_column = 'description', 
                                    verbose_name = _('Description'))
    # https://github.com/qywx/PlantUML-colors
    color = models.CharField(max_length=20, 
                             db_column = 'color', 
                             verbose_name = _('Coloring for puml'),
                             default='')
    mark  = models.CharField(max_length=1,  
                             verbose_name = _('Header mark for puml'),
                             db_column = 'mark', 
                             default='')

    def __str__(self):
        return f'{self.description}'

class System(models.Model):
    createdAt = models.DateTimeField('date created'),
    name      = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Influence(models.Model):
    createdAt   = models.DateTimeField(auto_now_add=True,db_column='createdAt')
    description_fwd = models.TextField(help_text=_('Required. Description on influence .'),
                                    verbose_name = _('Influence Forward'),
                                    name=_('description_fwd'),
                                    db_column='influence_fwd')
    description_back = models.TextField(help_text=_('Required. Description on influence .'),
                                    verbose_name = _('Influence Backward'),
                                    name=_('description_back'),
                                    db_column='influence_back')
    def __str__(self):
        return f'{str(self.description_fwd)}'

class ADR(models.Model):
    adrCreatedAt = models.DateTimeField(auto_now_add=True, 
                                    null=True,
                                    help_text=_('Required. First date of consideration'),
                                    verbose_name = _('When ADR was created'),
                                    name=_('adrCreatedAt'),
                                    db_column='createdAt')
    context  = models.TextField(blank = False,
                                    default='',
                                    help_text=_('Required. Describe what circumstances lead you to this point.'),
                                    verbose_name = _('Decision context'),
                                    name=_('decContext'),
                                    db_column='context')
    status   = models.ForeignKey(to=Status, 
                                    default='',
                                    on_delete=models.PROTECT, 
                                    help_text=_('Required. Current status of the decision. Could be changed over time'),
                                    verbose_name = _('Decision status'),
                                    name=_('decStatus'),
                                    db_column='status')
    decision = models.TextField(blank = False,
                                    default='',
                                    help_text=_('Required. Describe how do you overcome the obstracle111.'),
                                    verbose_name = _('Decision'),
                                    name=_('decision'),
                                    db_column='decision')
    effects  = models.TextField(blank = False,
                                    default='',
                                    help_text=_('Required. Describe either effects on previous or future decisions'),
                                    verbose_name = _('Effects. Both positive and negative'),
                                    name=_('effects'),
                                    db_column='effects')  
    affects  = models.ManyToManyField(to=System, #on_delete=models.PROTECT,
                                    help_text=_('Required. Affected systems. Could be ALL, None or some in between'),
                                    verbose_name = _('Affected solutions'),
                                    name=_('affectedSolutions'),
                                    db_column='affects')  
    projectLink = models.TextField( blank=True, 
                                    help_text=_('Optional. Link to jira project'),
                                    verbose_name = _('Project Link'),
                                    name=_('projectLink'),
                                    db_column='projectLink')
    statusChangedAt = models.DateTimeField(auto_now=True, 
                                    null=True,
                                    help_text=_('When status was changed'),
                                    verbose_name = _('When status was changed'),
                                    name=_('statusChangedAt'),
                                    db_column='statusChangedAt')
    influence = models.ManyToManyField(to="self", through='InfluenceADR')

    def __str__(self):
        return f'ADR-{self.id} {self.decision}'

class InfluenceADR(models.Model):
    src_adr    = models.ForeignKey(to=ADR, 
                                   null=True,
                                   on_delete=models.PROTECT, 
                                   db_column='src_adr',
                                   related_name='src_adr',
                                   verbose_name = _('Source ADR')) 
    influence  = models.ForeignKey(to=Influence, 
                                  on_delete=models.PROTECT)                                   
    inf_adr    = models.ForeignKey(to=ADR, 
                                   on_delete=models.PROTECT,
                                   db_column='inf_adr',
                                   related_name='inf_adr',
                                   verbose_name = _('Affected ADR')) 
    changedAt   = models.DateTimeField(auto_now_add=True,db_column='changedAt')  

    def __str__(self):
        return f'{self.influence.description_fwd[:50]}'    

    # TODO :: Fix this
    # class Meta:
    #     unique_together = [['src_adr','influence', 'inf_adr']]
      