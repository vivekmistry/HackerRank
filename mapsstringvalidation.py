if __name__ == '__main__':
    s = input()

methods = [str.isalnum,  str.isalpha,  str.isdigit, str.islower, str.isupper]

for res in map( lambda m: any( map(m,s) ), methods):
    print(res)
