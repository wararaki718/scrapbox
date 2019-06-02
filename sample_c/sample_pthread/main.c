#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

static void *thread_func(void *vptr_args)
{
    int i;

    for(i = 0; i < 20; i++) {
        fputs("  b\n", stderr);
        sleep(1);
    }

    return NULL;
}

int main()
{
    int i;
    pthread_t thread;

    if (pthread_create(&thread, NULL, thread_func, NULL) != 0) {
        return EXIT_FAILURE;
    }

    for(i = 0; i < 20; i++) {
        puts("a");
        sleep(1);
    }

    if (pthread_join(thread, NULL) != 0) {
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
