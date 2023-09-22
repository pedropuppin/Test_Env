from django import forms
from testando.models import PedidoPlaca


class PedidoFilterForm(forms.Form):
    status_choices = PedidoPlaca.STATUS  

    status_filter = forms.MultipleChoiceField(
        label='Status',
        choices=status_choices,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-inline'}),
        required=False,  # Allow no selection
    )
