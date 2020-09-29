from django import forms


# Language(코딩 언어)의 종류를 저장하는 Form class정의
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
    
    # 특정 선택 항목을 선택하기 위한 문자열 필드인 ChoiceField 사용
    image = forms.ChoiceField(
        required= True, #폼에서 빈칸 허용 여부
        label='운영체제(필수 항목) ', #HTML에서 필드를 렌더링할때 사용하는 레이블
        initial='none', #폼이 나타날 때 해당 필드의 초기 값.
        error_messages={'required':'Please enter language info', 'invalid choice': 'Please select a valid one'}, #해당 필드의 에러 메시지 목록.
        disabled=False, #해당 필드 편집 여부
        choices=img, #해당 필드의 선택 항목
    )

