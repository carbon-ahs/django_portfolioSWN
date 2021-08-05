from django import forms
from .models import contractContent
class contractContentForm(forms.ModelForm):
    class Meta:
        model = contractContent
        fields = '__all__'


'''
from .models import ModelName
class ModelNameForm(ModelForm):
    class Meta:
        model = ModelName
        fields = '__all__'
'''