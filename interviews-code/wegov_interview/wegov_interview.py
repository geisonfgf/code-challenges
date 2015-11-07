# SECTION ONE

class MultiplicationGenerator(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_helper(self):
        return Result(self.a * self.b)

class Result(object):
    def __init__(self, data):
        self.data = data

def get_helper_data(some_object):
    '''Returns the data from an object's "helper".
    Returns None if the object doesn't have a "helper".
    '''
    try:
        some_object_helper = some_object.get_helper()
        interesting_value = some_object_helper.data
    except AttributeError:
        # Object doesn't have a get_helper method.
        interesting_value = None
    return interesting_value

assert get_helper_data(MultiplicationGenerator(2, 3)) == 6
assert get_helper_data("hello world") == None


# SECTION TWO

class Calculation(object):
    def calculate_value(self):
        raise NotImplementedError('subclasses should implement this')

class Multiplication(Calculation):
    def __init__(self, a):
        self.a = a

    def calculate_value(self, b):
        # We don't like negative values.
        if b < 0:
            raise ValueError('negative values not supported')
        return self.a * b

def get_calculated_value(some_object, other_value):
    '''Given an object with a calculate_value method, pass a value to that
    method. If the object indicates that it doesn't support that value, then
    return the value provided.'''
    assert hasattr(some_object, 'calculate_value'), 'object needs to have calculate_value method'

    try:
        return some_object.calculate_value(other_value)
    except Exception:
       # The object doesn't support working with this value.
       return other_value
    
assert get_calculated_value(Multiplication(2), 3) == 6
assert get_calculated_value(Multiplication(2), -1) == -1

# SECTION THREE

# Old style.
def POST(self, request, entity, action):
    if not request.allowed(entity, action):
        raise request.response_no_permission()

class Request(object):
    def allowed(self, entity, action):
        for control_func in self.control_functions:
            if not control_func(entity, action):
                return False
        return True

# This is the "locked" control function.
def reject_because_locked(entity, action):
    # If the entity supports locking, and is locked...
    if getattr(entity, 'locked', False):
        # ... and the action is not read-only...
        if not action.readonly:
            # Then they cannot do it.
            return False
    return True



# Needs change?
def POST(self, request, entity, action):
    # If we are not allowed to perform the action because the entity is locked,
    # then unlock it and try again.
    #
    # 1) Call request.allowed(entity, action)
    # 2) If not allowed, determine whether it is because we are unlocked.
    # 3) If that is the case, call entity.unlock()
    # 4) Then try and get permission again.
    
    if not request.allowed(entity, action):
        raise request.response_no_permission()
