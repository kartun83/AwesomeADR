from django import forms

class ADRForm(forms.Form):
    context  = forms.CharField(widget=forms.Textarea)
    #status   = forms.ForeignKey(Status, on_delete=forms.PROTECT),
    decision = forms.CharField(widget=forms.Textarea)
    effects  = forms.CharField(widget=forms.Textarea)  
    #affects  = forms.ForeignKey(System, on_delete=forms.PROTECT)  
    projectLink = forms.CharField(widget=forms.URLInput)