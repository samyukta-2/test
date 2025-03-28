#include <stdio.h>

int main() {
    int choice;

    printf("select a number: ");
    printf("1.cse");
    printf("2.aiml");
    printf("3.ece");
    printf("4.mec");
    printf("enter a number from (1-4): ");

    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("B.tech Cse\n");
            break;
	case 2:
	    printf("B.tech aiml\n");
	    break;
