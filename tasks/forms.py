from django import forms


class TaskForm(forms.Form):
    text = forms.CharField(
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 
                'placeholder': 'Enter a todo task here, e.g. take out trash . . .', 
            }
        )
    )
