class Rectangle:
    def __init__(self, w,h):
      self.w, self.h = w,h

    # Define set_h to set h      
    def set_h(self, h):
      self.h = h
      
    # Define set_w to set w          
    def set_w(self, w):
      self.w = w
      
      
class Square(Rectangle):
    def __init__(self, w):
      self.w, self.h = w, w 

    # Define set_h to set w and h
    def set_h(self, h):
      self.h = h
      self.w = h

    # Define set_w to set w and h      
    def set_w(self, w):
      self.w = w
      self.h = w
      