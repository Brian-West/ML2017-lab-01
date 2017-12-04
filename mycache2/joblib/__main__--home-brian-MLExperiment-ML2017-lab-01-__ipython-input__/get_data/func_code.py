# first line: 1
@mem.cache
def get_data():
    data=load_svmlight_file('../data/australian_scale')
    return data[0],data[1]
