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
            printf("B.tech Cse amity university\n");
            break;
	case 2:
	    printf("B.tech aiml amity university\n");
	    break;
	case 3:
	    printf("B.tech ece\n");
	    break;
	case 4:
	    printf("b.tech mec amity university\n");
	    break;
	default:
	    printf("invalid");
    }
}

