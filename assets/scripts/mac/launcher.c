#include <unistd.h>

int main(int argc, char* argv[]) {
    return execv("/Applications/Cayenue.app/Contents/MacOS/Python/Library/Frameworks/Python.framework/Versions/Current/cayenue-env/bin/cayenue", NULL);
}