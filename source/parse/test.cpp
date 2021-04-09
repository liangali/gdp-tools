#include <stdio.h>
#include <stdint.h>

struct MyData
{
    uint32_t a : 4;
    uint32_t b : 4;
    uint32_t c : 8;
    uint32_t d : 16;
};


int main()
{
    struct MyData data = {};
    data.a = 7;
    data.b = 5;
    data.c = 30;
    data.d = 0xaa55;

    // size = 4, data = 0xaa551e57
    printf("size = %d, data = 0x%08x\n", sizeof(data), *(uint32_t*)(&data));

    printf("done\n");
    return 0;
}