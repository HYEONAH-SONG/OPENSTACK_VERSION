from django import forms

class Resource(forms.Form):
    img=[
        ('Ubuntu Linux 32-bit', 'Ubuntu Linux 32-bit'),
        ('Ubuntu Linux 64-bit', 'Ubuntu Linux 64-bit'),
        ('Windows 32-bit', 'Windows 32-bit'),
        ('Windows 64-bit', 'Windows 64-bit'),
        ('mac OS 32-bit', 'mac OS 32-bit'),
        ('mac OS 64-bit', 'mac OS 64-bit'),
        ('CentOS 32-bit', 'CentOS 32-bit'),
        ('CentOS 64-bit', 'CentOS 64-bit'),
        ('Red Hat 32-bit', 'Red Hat 32-bit'),
        ('Red Hat 64-bit', 'Red Hat 64-bit'),
        ('Oracle Linux 32-bit', 'Oracle Linux 32-bit'),
        ('Oracle Linux 64-bit', 'Oracle Linux 64-bit'),   
    ]

    # lan=[
    #     ('C', 'C'),
    #     ('C++', 'C++'),
    #     ('Java', 'Java'),
    #     ('Javascript', 'Javascript'),
    #     ('Python', 'Python'),
    # ]
  
    # flav=[
    #     ('m1.tiny', 'm1.tiny'),
    #     ('m1.small', 'm1.small'),
    #     ('m1.medium', 'm1.medium'),
    #     ('m1.large', 'm1.large'),
    #     ('m1.xlarge', 'm1.xlarge'),
    # ]

    # flavor = forms.ChoiceField(\
    #     required= True,\
    #     label='학생 수 Flavor 'ㄴ,\
    #     initial='none',\
    #     error_messages={'required':'Please enter language info', 'invalid choice': 'Please select a valid one'},\
    #     disabled=False,
    #     choices=flav,
    # )

    image = forms.ChoiceField(\
        required= True,\
        label='운영체제(필수 항목) ',\
        initial='none',\
        error_messages={'required':'Please enter language info', 'invalid choice': 'Please select a valid one'},\
        disabled=False,
        choices=img,
    )

    # language = forms.ChoiceField(\
    #     required= True,\
    #     label='Language ',\
    #     initial='none',\
    #     error_messages={'required':'Please enter language info', 'invalid choice': 'Please select a valid one'},\
    #     disabled=False,
    #     choices=lan,
    # )
    
    
    
