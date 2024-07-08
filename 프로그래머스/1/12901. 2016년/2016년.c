#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int month, int day) {
    const char* day_name[] = {"THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"};
    const int month_days[] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int total_days = 0;

    for(int m_idx=0; m_idx<month-1; m_idx++)
        total_days += month_days[m_idx];
    total_days += day;

    char* answer = (char*)malloc(sizeof(char) * 3);
    answer = day_name[total_days%7];
    return answer;
}