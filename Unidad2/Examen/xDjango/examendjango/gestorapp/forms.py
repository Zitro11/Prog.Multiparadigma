from django.forms import ModelForm
from gestorapp.models import Estudiante
from gestorapp.models import Gerentes
class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class GerenteForm(ModelForm):
    class Meta:
        model = Gerentes
        fields = '__all__'