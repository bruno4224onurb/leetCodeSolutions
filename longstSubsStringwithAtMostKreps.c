//programa para encontrar a maior substring com k repetições no máximo
#include <stdio.h>
#include <string.h>

//mapa ASCII
int mapIndex[128];
int lengthOfLongestSubstring(char* s, int k) {
//seta todos no mapa para 0
    memset(mapIndex,0,sizeof(mapIndex));
    int bigstSub = 0;
    int beg = 0;
//percorre a string
    for(int end = 0; s[end] != '\0'; end++){
        char current = s[end];
        //testa se teve k reps
        if(mapIndex[current] > k) beg += 1;
        //conta a incidencia 
        mapIndex[current] += 1;
        //testa tamanho
        int length = end - beg + 1;
        if(length > bigstSub) bigstSub = length;
    }
    return bigstSub;
    
}
