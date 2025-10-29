#ifndef solver_HPP
#define solver_HPP
#include "array"
#include <fstream>
#include<iostream>
#define N 9

typedef std::pair<int, int> coords;

class SudokuSolver{
public:
    //Constructors
    SudokuSolver(); //default
    SudokuSolver(std::array<std::array<int, N>, N> input);   //parameterized
    SudokuSolver(std::ifstream &fin, std::string); //from stream

    //Destructor
    ~SudokuSolver();

    //Getters && Setters
    int getCell(int row, int col)const;
    int getCell(coords cell)const;
    std::array<int, N> getRow(int row)const;
    std::array<int, N> getCol(int col)const;
    std::array<std::array<int, N>, N> getGrid()const;

    void setCell(int row, int col, int val);
    void setCell(coords cell, int val);
    void setRow(int row, std::array<int, N> arr);
    void setCol(int col, std::array<int, N> arr);
    void setGrid(std::array<std::array<int, N>, N> newGrid);

    void incrementValue(int row, int column);
    void incrementValue(coords cell);

    //Main Methods
    void printGrid();
    void solve();
private:
    //matrix storing the sudoku grid
    std::array<std::array<int, N>, N> grid;
    bool solved = false;

    bool checkBoardValidity();
    bool checkCellValidity(coords cell);
    //recursive function 
    void recursiveSolve(coords cell);
    coords findNextCell(coords currentCell);
    coords getFirstEmpty()const;
};

#endif