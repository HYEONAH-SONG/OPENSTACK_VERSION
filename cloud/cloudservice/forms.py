from django import forms

class Resource(forms.Form):
    img=[
        ('Ubuntu Linux 32-bit', 'Ubuntu Linux 32-bit'),
        ('Ubuntu Linux 64-bit', 'Ubuntu Linux 64-bit'),
        ('Windows 32-bit', 'Windows 32-bit'),
        ('Windows 64-bit', 'Windows 64-bit'),
        ('mac OS 32-bit', 'mac OS 32-bit'),
        ('mac OS 64-bit', 'mac OS 64-bit'),
        ('CentOS 7 x86-32', 'CentOS 7 x86-32'),
        ('CentOS 7 x86-64', 'CentOS 7 x86-64'),
        ('Red Hat 32-bit', 'Red Hat 32-bit'),
        ('Red Hat 64-bit', 'Red Hat 64-bit'),
        ('Oracle Linux 32-bit', 'Oracle Linux 32-bit'),
        ('Oracle Linux 64-bit', 'Oracle Linux 64-bit'),   
    ]
    

    image = forms.ChoiceField(\
        required= True,\
        label='운영체제(필수 항목) ',\
        initial='none',\
        error_messages={'required':'Please enter language info', 'invalid choice': 'Please select a valid one'},\
        disabled=False,
        choices=img,
    )

