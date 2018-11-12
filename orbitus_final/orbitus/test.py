from orbitus import Main

d_user = Main()

def FE(name,mail):
	d_user.FullName = name
	d_user.EMAIL = mail

def UP(uname,passwd):
	d_user.Username = uname
	d_user.Password = passwd

def A(age):
	d_user.Age = age