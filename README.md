# emojicpp
Emoji :smile: for c++ developers :+1:

This will convert emoji codes in strings to unicode emojis. 


```c++
emojicpp::emojize("Emoji :smile: for c++ :+1:") 
```

**Output**


> Emoji 😄 for c++ 👍


**Sample program**

```c++
#include <iostream>
#include "emoji.h"

int main() {
    std::cout << emojicpp::emojize("Emoji :smile: for c++ :+1:") << std::endl;
    return 0;
}
```

See supported emoji [list](https://github.com/shalithasuranga/emojicpp/blob/master/emoji.h)
