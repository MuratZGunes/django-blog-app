from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,label = 'Kullanıcı Adı')
    password = forms.CharField(max_length=20,label = 'Şifre',widget = forms.PasswordInput)

    # clean metoduna gerek yok çünkü otomatik olarak formun doğruluğunu kontrol ediyor


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label = 'Kullanıcı Adı')
    password = forms.CharField(max_length=20,label = 'Şifre',widget = forms.PasswordInput)
    confirm_password = forms.CharField(max_length=20,widget = forms.PasswordInput,label = 'Şifre Tekrarı')
    
    def clean(self):       # formun doğruluğunu kontrol etmek için clean metodunu override ettik
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Şifreler eşleşmiyor')
        
        values = {                  # sözlük olarak değerleri döndürüyoruz
            'username':username,
            'password':password
        }
        
        return values