"""
Python program to find the largest element and its location.
"""

def largest_element(a, loc = False):
    """ Return the largest element of a sequence a.
    """
    try:
        maxval = a[0]
        location = 0
        for (i,e) in enumerate(a):
            if e > maxval:
                maxval = e
                location = i
        if loc == True:
            return maxval, location
        else:
            return maxval
    except ValueError:
        return "Value Error"
    except TypeError:
        return "Type error, my dude. You can't compare those."
    except:
        return "Unforseen error! What did you do?"


if __name__ == "__main__":

    a = ["a","b","c",2,1]
    print("Largest element is {:}".format(largest_element(a, loc=True)))
