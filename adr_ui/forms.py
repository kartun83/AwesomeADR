from django import forms

class ADRForm(forms.Form):
    context  = forms.CharField(widget=forms.Textarea)
    status   = forms.ComboField(Status),
    decision = forms.CharField(widget=forms.Textarea)
    effects  = forms.CharField(widget=forms.Textarea)  
    affects  = forms.MultiValueField(System)  
    projectLink = forms.CharField(widget=forms.URLInput)