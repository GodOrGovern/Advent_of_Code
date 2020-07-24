// https://adventofcode.com/2018/day/9

#include <stdio.h>
#include <stdlib.h>

#define PLAYER_NUM 426 // Number of players
#define MAX_VAL 72058 // Number of turns (maximum marble value)

// Implements a node for a doubly-linked list
typedef struct Marble
{
    struct Marble* left;
    struct Marble* right;
    int value;
} Marble;

/* Build a circle of 'Marbles', keeping track of player scores and stopping when
 * there have been 'number' turns. Returns the highest player score */
long long buildCircle(Marble* current, int number);

/* Add the value of the marble 7 spots clockwise of 'current' to the current
 * player's score ('index' of 'players') and remove it from the circle */
Marble* addScore(Marble* current, int index, long long players[]);

// Add a 'Marble' to the right of 'current'
Marble* addMarble(Marble* current, int value);

// Find the max value in 'array' with length 'count'
long long maxArr(long long array[], int count);

// Free the circular doubly linked list of 'Marble' nodes
void freeMarbles(Marble* marble);

// Driver function
int main(void)
{
    Marble* first = (Marble*) malloc(sizeof(Marble));
    first->value = 0;
    first->left = first;
    first->right = first;

    long long maxOne = buildCircle(first, MAX_VAL);
    printf("Part One: %lli\n", maxOne);

    freeMarbles(first);
    first->left = first;
    first->right = first;

    long long maxTwo = buildCircle(first, MAX_VAL * 100);
    printf("Part Two: %lli\n", maxTwo);

    freeMarbles(first);
    free(first);
}

long long buildCircle(Marble* current, int number)
{
    long long players[PLAYER_NUM] = { 0 };
    int curPlayer = 0;
    for (int i = 1; i < number; i++)
    {
        if (i % 23 == 0 && current->value > 0)
        {
            players[curPlayer] += i;
            current = addScore(current, curPlayer, players);
        }
        else
            current = addMarble(current, i);
        curPlayer = (curPlayer + 1) % PLAYER_NUM;
    }

    return maxArr(players, PLAYER_NUM);
}

Marble* addScore(Marble* current, int index, long long players[])
{
    for (int i = 0; i < 7; i++)
        current = current->left;
    players[index] += current->value;

    Marble* next = current->right;
    current->left->right = next;
    next->left = current->left;
    free(current);
    return next;
}

Marble* addMarble(Marble* current, int value)
{
    Marble* next = (Marble*) malloc(sizeof(Marble));
    next->value = value;
    next->left = current->right;
    next->right = current->right->right;
    next->right->left = next;
    next->left->right = next;
    return next;
}

long long maxArr(long long array[], int count)
{
    long long max = array[0];

    for (int i = 1; i < count; i++)
        if (array[i] > max)
            max = array[i];

    return max;
}

void freeMarbles(Marble* marble)
{
    marble->left = NULL;
    marble = marble->right->right;
    while (marble->left)
    {
        free(marble->left);
        marble->left = NULL;
        marble = marble->right;
    }
}
