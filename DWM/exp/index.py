import numpy as np
 
class CPageRank(object):
    def __init__(self):
        self.PR = []
 
    def GetPR(self, IOS, alpha, max_itrs, min_delta):
        N = np.shape(IOS)[0]
        e = np.ones(shape=(N, 1))
        L = [np.count_nonzero(e) for e in IOS.T]
        helps_efunc = lambda ios,l:ios/l
        helps_func  = np.frompyfunc(helps_efunc, 2, 1)
        helpS = helps_func(IOS, L)
        A = alpha*helpS + ((1-alpha)/N)*np.dot(e, e.T)
        for i in range(max_itrs):
            if 0 == np.shape(self.PR)[0]:
                self.PR = np.full(shape=(N,1), fill_value=1.0/N)
            print('Initial PR value table:', self.PR)
            old_PR = self.PR
            self.PR = np.dot(A, self.PR)
            D = np.array([old-new for old,new in zip(old_PR, self.PR)])
            ret = [e < min_delta for  e in D]
            if ret.count(True) == N:
                print('Number of iterations: %d, succeed PR:\n'%(i+1), self.PR)
                break
        return self.PR
 
def CPageRank_manual():
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
  
    print("Enter the entries in a single line (separated by space): ")
    entries = list(map(int, input().split()))
    matrix = np.array(entries).reshape(R, C)
    '''
    IOS = np.array([[0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                    [0, 1, 1, 1, 0]], dtype=float)
    '''
    IOS = np.array(matrix, dtype = float)
    print('Directed Graph Matrix: ')
    print(matrix)
    pg = CPageRank()
    ret = pg.GetPR(IOS, alpha=0.85, max_itrs=100, min_delta=0.0001)
    print('Final PR value:\n', ret)
if __name__=='__main__':
    CPageRank_manual()