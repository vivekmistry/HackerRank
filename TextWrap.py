import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    return (wrapper.fill(text=string))

if __name__ == '__main__':
