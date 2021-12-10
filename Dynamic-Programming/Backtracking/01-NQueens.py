

class QueensProbblem:
    
    def __init__(self, n):
        self.n = n # num of queens
        self.chess_table = [[ 0 for i in range(n)] for j in range(n)]
        
    def solve_n_queens(self):
        
        # we start with the first queen (w/ index 0)
        if self.solve(0):
            self.print_queens()
        else:
            # considered all possible configurations w/o success
            # meaning there's no solution (3x3 with 3 queens)
            print("There's no solution to the prob...")
            
    # col_idx is the same as the index of the queen
    def solve(self, col_idx):
        
        # problem solved - base case
        if col_idx == self.n:
            return True # solved n queens prob
        
        # find a position for queen (col_idx) within a given col
        for row_idx in range(self.n):
            # 1 means theres is a queen at location
            if self.is_place_valid(row_idx, col_idx):
                self.chess_table[row_idx][col_idx] = 1
                
            # call same func with next itr (col_idx + 1) to find location of next queen in the next col
            if self.solve(col_idx + 1):
                return True 
            
            # Backtrack
            self.chess_table[row_idx][col_idx] = 0
        
        # when all rows considered w/o finding a valid cell    
        return False
    
    def is_place_valid(self, row_idx, col_idx):
        
        # check rows(if given queens can attack eachother horizontally)
        for i in range(self.n):
            if self.chess_table[row_idx][i] == 1:
                return False
         
        # check diagonal
        # from top-left to bottom-right   
        j = col_idx
        for i in range(row_idx, -1, -1):
            if i > 0 or j < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            
            j = j - 1
            
        # from top-right to bottom-left
        j = col_idx
        for i in range(row_idx, self.n):
            if j < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            
            j = j - 1
            
        return True
            
        
    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print('  Q  ', end='')
                else:
                    print(' - ', end='')
            print('\n')
                    


if __name__ == '__main__':
    queens = QueensProbblem(4)
    queens.solve_n_queens()