# Answer.py
# A solution algorithm using Gaussian elimination method

import random


class Answer:
    Base = []   # Ax=b (Solving a system of linear equations)

    def __init__(self, scale, rule):
        """
        Generate a matrix of specific scales and rules
        :param scale: scale
        :param rule: rule
        """
        self.scale = scale
        self.rule = rule

    @staticmethod
    def dist(x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

    def mat(self, i):
        """
        The i-th element and its surrounding matrix with rule
        :param i: The i-th element
        :return:
        mi: Base matrix
        """
        mi = []
        for x in range(self.scale):
            for y in range(self.scale):
                if self.dist((x, y), (i // self.scale, i % self.scale)) <= self.rule:
                    mi.append(1)
                else:
                    mi.append(0)
        return mi

    def gen_mat(self):
        """
        Generate the base matrix corresponding to each element
        :return: Add each base matrix to self.Base
        """
        for item in range(self.scale ** 2):
            self.Base.append(self.mat(item))

    def add(self, m1, m2):
        """
        Defining Matrix Addition
        :param m1: Matrix 1
        :param m2: Matrix 2
        :return:
        The new matrix after addition
        """
        new_m = []
        for i in range(self.scale ** 2):
            new_m.append((m1[i] + m2[i]) % 2)
        return new_m

    def prt(self):
        """
        Format output Gaussian elimination process
        :return:
        """
        for i in range(self.scale ** 2):
            for j in range(len(self.Base)):
                print(self.Base[j][i], end=' ')
                if j == self.scale ** 2 - 1:
                    print("|", end='')
            print()

    def row_add(self, i, j, mode=1):
        """
        Line transformation, add the i-th line to the j-th line
        :param i: i-th line
        :param j: j-th line
        :param mode: mode=1 is the augmented matrix, and 0 is the coefficient matrix
        :return:
        Perform a row transformation on the jth row of self.Base 
        """
        for x in range(self.scale ** 2 + mode):
            self.Base[x][j] = (self.Base[x][j] + self.Base[x][i]) % 2

    def row_change(self, i, j, mode=1):
        """
        Row swap, i, j row swap
        :param i: i-th line
        :param j: j-th line
        :param mode: mode=1 is the augmented matrix, and 0 is the coefficient matrix
        :return:
        Perform a row swap on the jth row of self.Base 
        """
        for x in range(self.scale ** 2 + mode):
            mid = self.Base[x][i]
            self.Base[x][i] = self.Base[x][j]
            self.Base[x][j] = mid

    def row_simplified(self, mode=1):
        """
        Gaussian elimination method for simplification
        :param mode: mode=1 is the augmented matrix, and 0 is the coefficient matrix
        :return:
        self.Base is the simplified discrimination matrix
        """
        for j in range(self.scale ** 2):
            position = []  # Position of 1 in column j
            for i in range(self.scale ** 2):
                if self.Base[j][i] == 1:
                    position.append(i)
            c_pos = -1  # The first non-zero element greater than or equal to j
            for f in position:
                if f >= j:
                    c_pos = f
                    break
            # print(c_pos)
            # print(position)
            if c_pos == -1:
                continue
            elif len(position) > 1:
                for p in position:
                    if p != c_pos:
                        self.row_add(c_pos, p, mode)
                if c_pos != j:
                    self.row_change(j, c_pos, mode)
            else:
                if c_pos != j:
                    self.row_change(j, c_pos, mode)
            # prt()
            # print('----------------------------------')

    def exam(self):
        """
        Check if the stepped discriminant matrix is full rank
        :return:
        Yes/No
        """
        flag = True
        for i in range(self.scale ** 2):
            if self.Base[i][i] == 0:
                flag = False
                break
            else:
                continue
        if not flag:
            # self.prt()
            # print("Dissatisfaction rank")
            return False
        else:
            return True

    def det(self):
        """
        Determine if there is a solution
        :return:
        Yes/No
        """
        det = True
        for j in range(self.scale ** 2):
            if self.Base[self.scale ** 2][j] == 1 and self.Base[j][j] == 0:
                # print("unsolvable")
                det = False
                break
        return det

    def answer(self, init, target):
        """
        Calculate answers
        :param init: Initial state
        :param target: Target state
        :return:
        asw: Answer List
        """
        self.Base = []      # Initialize discrimination matrix
        self.gen_mat()      # Generate discrimination matrix
        det_s = self.add(init, target)      # Addition of initial and final states
        self.Base.append(det_s)     # Add to the augmented column of the discrimination matrix (b)
        self.row_simplified()       # Simplification using Gaussian elimination method
        self.prt()          # Output elimination results
        asw = []
        if self.exam() or self.det():
            for i in range(self.scale ** 2):
                if self.Base[self.scale ** 2][i] == 1:
                    asw.append(i + 1)
            if self.exam():
                print("Full rank, there must be a unique solution")
            else:
                print("Not satisfied with rank, but with a solution")
        else:
            print("unsolvable")
        return asw

    def sol_sys(self):
        """
        Solution system, describing all possible solutions through a random linear combination of base matrices
        :return:
        Generate random feasible solutions
        """
        self.Base = []
        self.gen_mat()
        seq = [0 for x in range(self.scale ** 2)]
        for i in range(self.scale ** 2):
            if random.randint(0, 1) == 1:
                seq = self.add(seq, self.Base[i])
        return seq

    @classmethod
    def sol_list(cls, *scale_range):
        """
        View full rank solutions for all scenarios
        :param scale_range: Designated scale (default to 3-9)
        :return:
        Rules that enable a specific scale to have a full rank solution
        Default output [[3, 1], [4, 2], [5], [6, 1, 3], [7, 1, 3], [8, 1], [9]]
        """
        f_sol = []
        if len(scale_range) == 0:
            default_a = 3
            default_b = 10
        elif len(scale_range) > 1:
            default_a = scale_range[0]
            default_b = scale_range[1]
        else:
            default_a = scale_range[0]
            default_b = scale_range[0]
        for f_j in range(default_a, default_b):
            f_s = [f_j]
            for i in range(1, f_j):
                f_a = Answer(f_j, i)
                f_a.Base = []
                f_a.gen_mat()
                f_a.row_simplified(0)
                if f_a.exam():
                    f_s.append(i)
            f_sol.append(f_s)
        print(f_sol)


if __name__ == '__main__':
    # Answer.sol_list(3, 10)       # [[3, 1], [4, 2], [5], [6, 1, 3], [7, 1, 3], [8, 1], [9]]
    x1 = [random.randint(0, 1) for x in range(4 * 4)]
    x2 = [random.randint(0, 1) for x in range(4 * 4)]
    a = Answer(4, 2)
    Asw = a.answer(x1, x2)
    print(Asw)
