#clousers and Decorators 
#funtion to return num+1.
def addplusone(num):
    return num+1
print(addplusone(1))
# num=1
#o/p -> 2

# passing function as a argument to another funtion . 
def fucntion_call (function): 
    input_num = 10
    return function(input_num)
print(fucntion_call(addplusone))
#o/p -> 11
#---------------------------------------------------------------------------------------------

#clousers
#returning function from a function  
def outerfuntion():
    def innerfunction():
        return 'I am innerfuntion'
    return innerfunction
print(outerfuntion())
#o/p -> function outerfuntion.<locals>.innerfunction at 0x000002147EDA6EE0
var = outerfuntion()
print(var())
# o/p -> I am innerfuntion

#Arugments can be passed to innerfuntion using outerfuction 
# i.e all the variables in the outerfunction scope can be accessible by innerfunction
def outerfuntion(outstring):
    print (f"This is variable on outerfuntion scope outstring = '{outstring}'")
    def innerfunction():
        return f"Inner funtion returned outstring '{outstring}'"
    return innerfunction()
print(outerfuntion('hi'))
#o/p->This is variable on outerfuntion scope outstring = 'hi'
#     Inner funtion returned outstring 'hi'
#---------------------------------------------------------------------------------------------

#Decorator function takes a function as an argument and returns a wrapper function 
useraccounts= {'foo':1234,
               'bar':5678
              }
def login_required_decorator(function):
    def wrapper_function(username,password):
        if useraccounts[username] == password:
            return function(username,password)
        else:
            return f'Not authorized'        
    return wrapper_function

def check_auth(username,passowrd):
    return f'{username} is authorized'

x = login_required_decorator(check_auth)
print(x('foo',1234))
#o/p using the variable assignment method -> foo is authorized

@login_required_decorator
def login(username,password):
    return f'{username} logged in'
print(login('bar',1234))
#o/p using @ symbol -> Not authorized
#------------------------------------------------------------------------------------------------------

#Multiple Decorators 
useraccounts= {'foo':1234,
               'bar':5678
              }

accontpermission = {'foo':True,
                    'bar':False
                    }

def login_required_decorator(function):
    def wrapper_function(username,password):
        if useraccounts[username] == password:
            return function(username,password) 
        else:
            return f'{username} loggin failed'    
    return wrapper_function

def permission_required_decorotor(function):
    def wrapper(*args):
        username,_= args
        if accontpermission[username]:
            return function(*args)
        else:
            return f"{username} logged in but not authorized"
    return wrapper

@login_required_decorator
@permission_required_decorotor
def login(username,password):
    return f'{username} logged in with permission'
print(login('bar',5678))
#o/p -> bar logged in but not authorized
#------------------------------------------------------------------------------------------------------

#Decorators with arguments 
useraccounts= {'foo':1234,
               'bar':5678
              }

accountpermission = {'foo':True,
                    'bar':False
                    }
def login_permissioncheck(permission=False):
    def login_required_decorator(function):
        def wrapper_function(username,password):
            if not permission:
                if useraccounts[username]==password:   
                    return function(username,password) 
                else:
                    return f'{username} authentication failed'
            if permission:
                if useraccounts[username]==password and accountpermission[username]:   
                    return function(username,password) 
                if useraccounts[username]==password and not accountpermission[username]:
                    return f"{username} authenticated but not authroized"
                else:
                    return f'{username} authentication failed'
        return wrapper_function
    return login_required_decorator

@login_permissioncheck(permission=True)
def login_permission(username,passowrd):
    return f'{username} Logged in Succesfully'

print(login_permission('bar',5678))
#o/p - >bar authenticated but not authroized

@login_permissioncheck(permission=False)
def only_login(username,passowrd):
    return f'{username} Logged in Succesfully'

print(only_login('bar',5678))
#o/p - >bar Logged in Succesfully
#------------------------------------------------------------------------------------------------------
