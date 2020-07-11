type C struct {
    row, col int
}

func solve(board [][]byte)  {
    totalRows := len(board)
    if totalRows==0{
        return
    }
    totalCols := len(board[0])
    
    //nonSurrounds := make(map[C]bool)
    visited := make(map[C]bool)
    var stretch func(cor C)
    stretch = func(cor C) {
        //nonSurrounds[cor] = true
        //fmt.Println("visiting",cor)
        visited[cor]=true
        for _, delCor := range []C{C{0,-1},C{0,1},C{1,0},C{-1,0}}{
            //fmt.Println("Adding",delCor,"to",cor)
            nextCor := C{cor.row+delCor.row,cor.col+delCor.col}
            //fmt.Println(nextCor)
            if 0<=nextCor.row && nextCor.row<totalRows && 0<=nextCor.col && nextCor.col<totalCols && visited[nextCor]==false && board[nextCor.row][nextCor.col]=='O'{
                stretch(nextCor)
            }
        }
    }
    for i:=0;i<totalRows;i++{
        if board[i][0]=='O' && visited[C{i,0}]==false{
            stretch(C{i,0})
        }
        if board[i][totalCols-1]=='O'&& visited[C{i,totalCols-1}]==false{
            stretch(C{i,totalCols-1})
        }
        
    }
    for j:=0;j<totalCols;j++{
        if board[0][j]=='O'&& visited[C{0,j}]==false{
            stretch(C{0,j})
        }
        if board[totalRows-1][j]=='O'&& visited[C{totalRows-1,j}]==false{
            stretch(C{totalRows-1,j})
        }
    }
    for i:=0;i<totalRows;i++{
        for j:=0;j<totalCols;j++{
            if board[i][j]=='O' && visited[C{i,j}]==false{
                board[i][j]='X'
            }
        }
    }
    
}