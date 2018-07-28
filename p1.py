from math import acos
import turtle


def testif(b, testname, msgOK="", msgFailed=""):
    """Function used for testing. 
    param b: boolean, normally a tested condition: true if test passed, false otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True  ( test condition true)
    param msgFailed: string to be printed if param b==False
    returns b
    """
    if b:
        print("Success: "+ testname + "; " + msgOK)
    else:
        print("Failed: "+ testname + "; " + msgFailed)
    return b
        
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
    
def test_power():
    print("Power function of 7 to the 4th power: ", power(7,4))
    print("7 to the 4th power using ** operator: ", 7 ** 4)

def slice_sum(lst, b, e):
    if b == e:
        return lst[b]
    else:
        return slice_sum(lst, b+1, e) + lst[b]

def test_slice_sum():
    ls = [3,4,5,6,7,4,9,33]
    testif(slice_sum(ls,4,6),'PASS','FAIL')
    testif(slice_sum(ls,3,6),'PASS','FAIL')
   

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
def test_slice_sum_m():
    ls = [3,4,5,6,7,4,9,33]
    testif(slice_sum_m(ls,4,6),'PASS','FAIL')
    testif(slice_sum_m(ls,3,6),'PASS','FAIL')


    
        

binary_tree(160, 5)

ls = [3,4,5,6,7,4,9,33]
slice_sum_m(ls,2,6)
print(memo)
test_slice_sum()
test_slice_sum_m()


