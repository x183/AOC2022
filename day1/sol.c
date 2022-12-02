#include <stdio.h>
#include <stdlib.h>

int readLine(FILE *fptr, char *line)
{
	int i = 0;
	char c;
	while ((c = fgetc(fptr)) != EOF)
	{
		printf("Reads file, char no. %d", i);
		if (c == '\n')
		{
			line[i] = '\0';
			return 1;
		}
		line[i] = c;
		i++;
	}
	return 0;
}

int main(int argc, char *argv[])
{
	// printf("reached main =)");
	FILE *fptr;
	fptr = fopen("./quest.txt", "r");
	char *line = NULL;
	if (readLine(fptr, line))
		printf("%s", line);
	int sum = 0;
	int num;
	return 0;
}