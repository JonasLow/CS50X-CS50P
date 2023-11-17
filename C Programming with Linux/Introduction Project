#include <stdio.h>

/*
You are rolling a red, a yellow and a green standard dice (whose sides each have
the numbers 1-6 on them) and combine them to a 3-digit number by using the red 
value as the ones place, the yellow value as the tens place and the green value 
as the hundreds place. For example, if you rolled a 3 with red, a 5 with yellow 
and 2 with green then the combined 3-digit number would be 253.

You repeat this process and your job is to continuously find the average of all 
of those 3-digit numbers.

More precisely, you need to first read an integer that tells you how many 
3-digit numbers you'll be averaging. Next, you need to read the red value, then 
the yellow value, then the green value of the first throw and print out the 
corresponding 3-digit number as well as the current average with one decimal 
place. Then you repeat this process for the given number of rounds.
*/

int main(void){
    int ones = 0;
    int tens = 0;
    int hundreds = 0;
    int trials = 0;
    
    scanf("%d", &trials);
    
    int i = 0;
    int number = 0;
    float sum = 0.0;
    float average = 0.0;
    
    for (i = 1; i < trials + 1; i++){
        scanf("%d %d %d", &ones, &tens, &hundreds);
        
        number = ones + tens * 10 + hundreds * 100;
        sum = sum + number;
        average = sum / i;
        
        printf("%d. you rolled: %d, current average: %.1f\n", i, number, average);
    }
    
    return 0;
}