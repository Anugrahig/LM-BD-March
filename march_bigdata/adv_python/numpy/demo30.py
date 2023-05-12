# Floor Ceil and Round
import numpy as np
a=np.array([[1.5,2.5,3.5,4.5],[5.1,6.0,7.4,8.3],[9.3,10.7,11.5,12.3],[13.3,14.2,15.3,16.7]])
print(a)

# Floor : discard decimal part : convert to lowest integer
b=np.floor(a)
print(b)
# Ceil : convert to the highest integer
c=np.ceil(a)
print(c)
# Round : .5 below convert to lowest and above .5 convert to the highest number
# .5 is a exception case if the num is even then convert to lower , if the num is odd then convert to higher
d=np.round(a)
print(d)