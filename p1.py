from math import acos
import turtle

def binary_tree(depth, length, origin = (0,0) ):

	turtle.setposition(origin)
	if length == 0:
		return True
	turtle.right(30)
	turtle.pendown()
	turtle.forward(depth)
	right = turtle.pos()
	turtle.penup()
	turtle.bk(depth)

	turtle.right(120)
	turtle.pendown()
	turtle.forward(depth)
	turtle.penup()
	left = turtle.pos()
	turtle.bk(depth)

	turtle.left(150)

		
	binary_tree(depth/2, length-1, left) 
	binary_tree(depth/2, length-1, right) 

	return True

def power(x, n):
    if n==0:
        return 1
    elif n==1:
        return x
    elif n%2 == 1:
        return x * power(x, ((n-1)/2)) ** 2
    else:
        return power(x, n/2) ** 2

power(7,4)

def slice_sum(lst, b, e):
    if b == e:
        return lst[b]
    else:
        return slice_sum(lst, b+1, e) + lst[b]

memo={}
def slice_sum_m(lst, b, e):
    try:
        return memo[(b,e)]
    except: 
        if b == e:
            memo[(b,e)] = lst[b]
            return memo[(b,e)]
        else:
            memo[(b,e)]= slice_sum_m(lst, b+1, e) + lst[b]
            return memo[(b,e)]
        


#binary_tree(160, 5)
ls = [3,4,5,6,7,4,9,33]
slice_sum_m(ls,2,6)
print(memo)
        
