#!/usr/bin/env python

class RobotOnMoonEasy(object):
    """ SRM 651 Div 2 250 """
 
    def isSafeCommand(self, board, cmds):
        H = len(board)
        W = len(board[0])

        for i in xrange(H):
            for j in xrange(W):
                if board[i][j] == 'S':
                    p = [i, j]
        
        for cmd in cmds:
            next_p = [p[0], p[1]]

            if cmd == 'U': 
                next_p[0] -= 1
            elif cmd == 'D':
                next_p[0] += 1
            elif cmd == 'R': 
                next_p[1] += 1
            elif cmd == 'L':
                next_p[1] -= 1
            else:
                raise ValueError('Invalid Command')

            if next_p[0] not in range(W) or next_p[1] not in range(H):
                return "Result: Died"

            val = board[next_p[0]][next_p[1]]
            if val == '.':
                p = next_p[:]

        return "Result: Alive"


if __name__ == '__main__':
    robot = RobotOnMoonEasy()

    boards = [
        [['....', '..#.', '..S#', '....'], 'URURUR'],
        [['.S', '..'], 'L'],
        [['.S', '..'], 'R'],
        [['....', '..#.', '..S#', '....'], 'LLUURRR'],
    ]

    for board, cmds in boards:
        print "\n>> Board:"
        print "\n".join(board)
        print "Commands:", cmds
        print robot.isSafeCommand(board, cmds)
