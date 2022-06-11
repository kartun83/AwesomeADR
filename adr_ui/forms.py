from django import forms
from .models import Status, System, ADR,InfluenceADR

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ADRForm(forms.ModelForm):
    class Meta:
        model = ADR
        fields = [ 'context','status','decision',
                  'effects','affects','projectLink','influence']
    adrCreatedAt = forms.DateTimeField(disabled=True, widget=forms.DateTimeInput) 
    context   = forms.CharField(widget=forms.Textarea)
    status    = forms.ModelChoiceField(queryset = Status.objects.all())
    decision  = forms.CharField(widget=forms.Textarea)
    effects   = forms.CharField(widget=forms.Textarea)  
    affects   = forms.ModelMultipleChoiceField(blank= False, 
                                              widget=forms.SelectMultiple, 
                                              queryset = System.objects.all())  
    projectLink = forms.CharField(required=False, widget=forms.URLInput)
    #statusChangedAt = forms.DateTimeField(disabled=True, widget=forms.DateTimeInput) 
    influence = forms.ModelChoiceField(queryset = InfluenceADR.objects.all())

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
        
    #     self.helper.form_id = 'id-newADRForm'
    #     self.helper.form_class = 'blueForms'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = '/adr_ui/new_adr/'

    #     self.helper.add_input(Submit('submit', 'Submit'))