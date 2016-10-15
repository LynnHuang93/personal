def convert_to_post_order(input_string):
	stack = []
	postfix = []
	num = ['0','1','2','3','4','5','6','7','8','9']
	for char in input_string:
	    if char in num :
	        postfix.append(char)
	    else:
	        if len(stack) == 0:
	            stack.append(char)
	        else:
	            if char == '*':
	                stack.append(char)
	            else:
	                while len(stack) != 0:
	                    if stack[-1] == "+":
	                        break
	                    postfix.append(stack.pop())
	                stack.append(char)
	                
	while len(stack) != 0:
	    postfix.append(stack.pop())
	return "".join(postfix)

def main():
	test = "2*4*3+9*3+5"
	print(convert_to_post_order(test))

if __name__ == "__main__":
	main()