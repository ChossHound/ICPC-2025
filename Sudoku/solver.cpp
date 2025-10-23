#include "solver.hpp"
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>

/*

Possible bugs:
1) in the getFirstEmpty() function, if exit both loops, nothing is returned. 

*/
//Constructors
SudokuSolver::SudokuSolver(){
    //initialize all values on the grid to 0
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            this->grid[i][j] = 0;
        }
    }
}

SudokuSolver::SudokuSolver(std::array<std::array<int, N>, N> input){
    for(auto inIt = input.begin(), gridIt = this->grid.begin(); 
        inIt != input.end(); inIt++, gridIt++){
        
        *gridIt = *inIt;
    }
}   

SudokuSolver::SudokuSolver(std::ifstream &fin, std::string file){
    fin.open(file);
    std::string line, num;
    
    //read line in file
    for(int i = 0; i < N; i++){
        getline(fin, line, '\n');
        std::stringstream ss(line);
        
        //split the line
        for(int j = 0; j < N; j++){
            getline(ss, num, ' ');
            this->grid[i][j] = stoi(num);
        }
    }
}


//Destructor
SudokuSolver::~SudokuSolver(){}

//Getters && Setters
int SudokuSolver::getCell(int row, int col)const{ return this->grid[row][col]; }
int SudokuSolver::getCell(coords cell)const{ return this->grid[cell.first][cell.second];}
std::array<int, N> SudokuSolver::getRow(int row)const{ return this->grid[row]; }
std::array<int, N> SudokuSolver::getCol(int col)const{
    std::array<int, N> columnArr;
    for(int i = 0; i < N; i++){
        columnArr[i] = this->grid[i][col];
    }
    return columnArr;
}
std::array<std::array<int, N>, N> SudokuSolver::getGrid()const{ return this->grid; }

void SudokuSolver::setCell(int row, int col, int val){ this->grid[row][col] = val; }
void SudokuSolver::setCell(coords cell, int val){
    this->grid[cell.first][cell.second] = val;
}
void SudokuSolver::setRow(int row, std::array<int, N> arr){ this->grid[row] = arr; }
void SudokuSolver::setCol(int col, std::array<int, N> arr){
    for(int i = 0; i < N; i++){
        this->grid[i][col] = arr[i];
    }
}
void SudokuSolver::setGrid(std::array<std::array<int, N>, N> newGrid){ this->grid = newGrid; }

//Main Methods
void SudokuSolver::printGrid(){
    for(auto it : this->grid){
        for(auto jt : it){
            std::cout << jt << ' ';
        }
        std::cout << '\n';
    }
}

bool SudokuSolver::checkBoardValidity(){
    return false;
}

bool SudokuSolver::checkCellValidity(coords cell){
    //check if its already prefilled...
    int currentvalue = this->grid[cell.first][cell.second];
    int cell_Subsquare_X = cell.first / 3;
    int cell_SubSquare_Y = cell.second / 3;

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            //skip if cell (i, j) is the one your testing
            if(cell.first == i && cell.second == j){
                continue;
            }
            // std::cout << i << ", "<< j << '\n';

            //check row
            if(i == cell.first){
                if(this->grid[i][j] == currentvalue){
                    // std::cout << "row" << '\n';
                    return false;
                }
            }
            //check column
            else if(j == cell.second){
                if(this->grid[i][j] == currentvalue){
                    // std::cout << "col" << '\n';
                    return false;
                }
            }
            //check subsquare
            else if(i / 3 == cell_Subsquare_X && j / 3 == cell_SubSquare_Y){
                if(this->grid[i][j] == currentvalue){
                    // std::cout << "box" << '\n';
                    return false;
                     
                }
            }
        }
    }
    return true;
}

void SudokuSolver::solve(){
    //main function that starts the recursive solve function
    recursiveSolve(getFirstEmpty());
}

void SudokuSolver::recursiveSolve(coords currentCell){
    //Base case
        //return if board is solved
            if(this->solved){
                return;
            }
    //general case
        
    //loop through N possible digits until you find one that doesn't break board rules
    for(int i = 0; i < N; i++){
        //if current cell value doesnt break rules...
        setCell(currentCell, i+1);
        bool validCell = checkCellValidity(currentCell);
        
        if(validCell){
            //move to next cell
            recursiveSolve(findNextCell(currentCell));
            if(this->solved){
                return;
            }
            continue;
        } 
    }
    setCell(currentCell, 0);
    return;           
}


coords SudokuSolver::findNextCell(coords currentCell){
    coords nextCell = currentCell;

    //first make sure current cell isnt still empty
    if(this->grid[currentCell.first][currentCell.second] == 0){
        return currentCell;
    }

    //find the next empty cell
    do
    {
        //check if cell is the last in a row
        if(nextCell.second == N-1){
            if(nextCell.first == N-1){
                //reached the last cell and found a valid solution
                this->solved = true;
                return coords(-1, -1);
            }else{
                nextCell.first += 1;
                nextCell.second = 0;
            }
        }else{
            nextCell.second += 1;
        }
    } while (this->grid[nextCell.first][nextCell.second] != 0);
    return nextCell;
}

coords SudokuSolver::getFirstEmpty()const{
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(this->getCell(coords(i, j)) == 0){
                return coords(i, j);
            }
        }
    }
    // return coords(i, j);
}

void SudokuSolver::incrementValue(int row, int column){ this->grid[row][column]++; }
void SudokuSolver::incrementValue(coords cell){
    this->grid[cell.first][cell.second]++;
}