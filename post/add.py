#比较numpy的计算能力更加高效
import timeit
sum_by_for="""
for d in data:
    s+=d
"""
sum_by_num="""
sum(data)
"""
sum_by_numpy_sum="""
import numpy
numpy.sum(data)
"""
def timeit_using_list(n,loops):
    list_setup="""
data=[1]*{} 
s=0   
""".format(n)
    print('list result:')
    print(timeit.timeit(sum_by_for,list_setup,number = loops))
    print(timeit.timeit(sum_by_num, list_setup, number=loops))
    print(timeit.timeit(sum_by_numpy_sum, list_setup, number=loops))
def timeit_using_array(n,loops):
    array_setup="""
import array
data=array.array('L',[1]*{}) 
s=0   
""".format(n)
    print('array result:')
    print(timeit.timeit(sum_by_for,array_setup,number = loops))
    print(timeit.timeit(sum_by_num, array_setup, number=loops))
    print(timeit.timeit(sum_by_numpy_sum,array_setup, number=loops))
def timeit_using_numpy(n,loops):
    numpy_setup="""
import numpy
data=numpy.array([1]*{}) 
s=0   
""".format(n)
    print('array result:')
    print(timeit.timeit(sum_by_for,numpy_setup,number = loops))
    print(timeit.timeit(sum_by_num,numpy_setup, number=loops))
    print(timeit.timeit(sum_by_numpy_sum,numpy_setup, number=loops))
if __name__ == '__main__':
    timeit_using_list(30000,500)
    timeit_using_array(30000,500)
    timeit_using_numpy(30000,500)