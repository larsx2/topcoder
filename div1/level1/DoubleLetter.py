class DoubleLetter(object):

    def ableToSolve(self, s):
        if len(s) % 2 != 0:
            return 'Impossible'

        s = list(s)
        
        found = True 
        while found:
            found = False

            for i in range(len(s)-1):
                if s[i] == s[i+1]:
                    found = True
                    del s[i:i+2]
                    break

        if len(s):
            return 'Impossible'

        return 'Possible'


if __name__ == '__main__':
    
    double = DoubleLetter()

    params = [
        'aabccb',
        'aabccbb',
        'abcddcba',
        'abab',
        'aaaaaaaaaa',
        'aababbabbaba',
        'zzxzxxzxxzzx'
    ]

    for param in params:
        print '"{}" = {}'.format(param, double.ableToSolve(param))
