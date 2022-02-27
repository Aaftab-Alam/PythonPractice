

def aadil_func(n=None):
	print("abc,",n)
func_dict={"aadil":aadil_func}
command=input()
func_dict[command]()