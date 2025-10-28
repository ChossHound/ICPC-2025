#include <cassert>
#include <iostream>
#include <iterator>
#include <utility>

int strInversionSum(std::string);

int main(int argc, char* argv[]){
    //simple bitstring assertions
    assert(strInversionSum("001") == 0);
    assert(strInversionSum("010") == 1);
    assert(strInversionSum("101") == 1);
    assert(strInversionSum("11010") == 5);
    std::cout << "simple bitstring assertions passed\n";
    // sequence with ambiguous char assertions:
    
    assert(strInversionSum("?0?") == 3);
    
    
    return 0;
}

int strInversionSum(std::string sequence){
    int i= 0 ,j=sequence.size() -1;
    int result = 0;

    while(i < j){
        while(sequence[i] == '0'){
            i++;
        }
        // std::cout << "i: " << i << '\n';  
        while(sequence[j] == '1'){
            j--;
        }
        // std::cout << "j: " << j << '\n';
        if(i >= j){
            break;
        }else if(sequence[i] == '?'){
            // recurse twice on substrings from i to j
            //str[i] = 0
            std::string a = sequence.substr(i, j-i);
            a[0] = '0';
            
            //str[i] = 1
            std::string b = sequence.substr(i,j-i);
            b[0] = '1';
            // result += both recursions
            result += strInversionSum(a) + strInversionSum(b);
        }else if(sequence[j] == '?'){
            // recurse twice on substrings from i to j
            //str[j] = 0
            std::string c = sequence.substr(i ,j-i);
            c[j-i] = '0';
            //str[j] = 1
            std::string d = sequence.substr(i, j - i);
            d[j - i] = '1';
            //result += both recursions
            result += strInversionSum(c) + strInversionSum(d);
        }else{
            result += (j - i);
            // swap values
            std::swap(sequence[i], sequence[j]);
        }
    }
    return result;
}

