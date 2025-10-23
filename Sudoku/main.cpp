# include "solver.hpp"

void test();

int main(int argc, char* argv[]){
    std::string fileInput;
    if(argc >= 2 && std::string(argv[1]) == "test"){
        test();
    }
    else if(argc >= 2){
        fileInput = argv[1];
    }
    std::ifstream fin;
    SudokuSolver game(fin, fileInput);
    game.printGrid();
    game.solve();
    std::cout << ", " << '\n';
    game.printGrid();

    return 0;
}


void test(){
    // testing suite for program...
    std::ifstream fin;
    SudokuSolver testGame(fin, "testGame.txt");
    testGame.printGrid();
    testGame.solve();
    std::cout << '\n';
    testGame.printGrid();
}