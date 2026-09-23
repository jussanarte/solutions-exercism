#include "two_fer.h"
#include <stdio.h> 

void two_fer(char *buffer, const char *name) {
    const char *display_name = (name == NULL) ? "you" : name;

    // sprintf monta a string final e guarda-a no buffer (é diferente do printf).
    sprintf(buffer, "One for %s, one for me.", display_name);
}