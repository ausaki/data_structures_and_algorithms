// title: word-ladder
// detail: https://leetcode.com/submissions/detail/192502024/
// datetime: Fri Nov 30 10:26:45 2018
// runtime: 220 ms
// memory: N/A

struct hash_entry {
    char *word;         /* key */
    UT_hash_handle hh; /* makes this structure hashable */
};

struct hash_entry *words = NULL;

void add_word(char *word) {
    struct hash_entry *entry = (struct hash_entry*)malloc(sizeof(struct hash_entry));
    entry->word = word;
    HASH_ADD_KEYPTR(hh, words, entry->word, strlen(entry->word), entry);
}

struct hash_entry *find_word(char *word) {
    struct hash_entry *entry;
    HASH_FIND_STR(words, word, entry);
    return entry;
}

void delete_word(struct hash_entry *entry) {
    HASH_DEL(words, entry);  
}

void print_words(){
    struct hash_entry *entry;
    printf("words: ");
    for(entry = words; entry != NULL; entry = (struct hash_entry*)(entry->hh.next)){
        printf("%s ", entry->word);
    }
    printf("\n");
}

struct Queue {
    int size;
    int head;
    int tail;
    int len;
    void** buffer;
};

struct Node {
    char* word;
    int level;
};

struct Node* node_init(char* word, int level){
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->word = word;
    node->level = level;
    return node;
}

struct Queue* queue_init(){
    struct Queue *queue = (struct Queue*)malloc(sizeof(struct Queue));
    queue->size = 1100;
    queue->buffer = (void**)malloc(sizeof(void *) * queue->size);
    queue->head = 0;
    queue->tail = 0;
    queue->len = 0;
    return queue;
}

void queue_expand(struct Queue *queue){
    int i = 0, old_size = queue->size;
    queue->size = old_size * 2;
    queue->buffer = (void**)realloc(queue->buffer, sizeof(void*) * queue->size);
    if(queue->tail < queue->head){
        for(int i = 0; i < queue->tail; i++){
            queue->buffer[old_size + i] = queue->buffer[i];
        }
        queue->tail += old_size;
    }
}

int queue_size(struct Queue *queue){
    return queue->len;
}

int queue_add(struct Queue *queue, void *node){
    if(queue->len == queue->size){
        queue_expand(queue);
    }
    queue->buffer[queue->tail] = node;
    queue->tail = (queue->tail + 1) % queue->size;
    queue->len ++;
    return 0;
}

void* queue_pop(struct Queue *queue){
    if(queue->len == 0){
        return NULL;
    }
    void* v = queue->buffer[queue->head];
    queue->head = (queue->head + 1) % queue->size;
    queue->len --;
    return v;
}

void print_queue(struct Queue *queue){
    if(queue_size(queue) == 0){
        printf("queue is empty\n");
    }
    int i = 0;
    printf("queue: ");
    for(i = queue->head; i < queue->tail; i = (i + 1) % queue->size){
        printf("%s ", ((struct Node*)queue->buffer[i])->word);
    }
    printf("\n");
}


int ladderLength(char* beginWord, char* endWord, char** wordList, int wordListSize) {
    int word_length = strlen(beginWord);
    int i = 0, e;
    char j = 0, k = 0;
    struct Queue *queue = queue_init();
    struct Node *node;
    struct hash_entry *entry;
    for(i = 0; i < wordListSize; i++){
        add_word(wordList[i]);
    }
    queue_add(queue, node_init(beginWord, 0));
    while(queue_size(queue) && HASH_COUNT(words)){
        node = (struct Node*)queue_pop(queue);
        // printf("%s(%d)(%d),", node->word, node->level, queue_size(queue));
        // print_words();
        for(i = 0; i < word_length; i++){
            k = node->word[i];
            for(j = 'a'; j <= 'z'; j++){
                node->word[i] = j;
                if(entry = find_word(node->word)){
                    e = queue_add(queue, node_init(entry->word, node->level + 1));
                    delete_word(entry);
                    if(strcmp(node->word, endWord) == 0){
                        return node->level + 2;
                    }
                }
            }
            node->word[i] = k;
        }
    }
    return 0;
}