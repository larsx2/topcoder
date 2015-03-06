class TaroGrid(object):
    """ http://community.topcoder.com/stat?c=problem_statement&pm=13394 """

    def getNumber(self, grid):
        grid = [list(r) for r in grid]
 
        h = {i: { 'B': 0, 'W': 0 } for i in enumerate(xrange(grid))}
        print h
        for i, _ in enumerate(grid):
            for j, _ in enumerate(grid[i]):
                if j in x:
                	x[j].append(grid[i][j])
                else:
                	x[j] = [grid[i][j]]
        
        print x


if __name__ == '__main__':
    params = [
        [
            'BWW',
            'BBB',
            'BWB'
        ],
    ]

    taro = TaroGrid()
    for param in params: 
        print "{} = {}".format(param, taro.getNumber(param))
