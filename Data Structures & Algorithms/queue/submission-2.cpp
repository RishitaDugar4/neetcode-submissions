struct Node {
    Node* next;
    Node* prev;
    int val;

    Node(int val) : val(val), next(nullptr), prev(nullptr) {}
};

class Deque {
private:
    Node* head;
    Node* tail;
public:
    Deque() {
        head = new Node(-1);
        tail = new Node(-1);

        head->next = tail;
        tail->prev = head;
    }

    bool isEmpty() {
        return head->next == tail;
    }

    void append(int value) {
        Node* newNode = new Node(value);
        Node* lastNode = tail->prev;
        
        lastNode->next = newNode;
        newNode->prev = lastNode;
        newNode->next = tail;
        tail->prev = newNode;

    }

    void appendleft(int value) {
        Node* newNode = new Node(value);
        Node* firstNode = head->next;

        firstNode->prev = newNode;
        newNode->next = firstNode;
        newNode->prev = head;
        head->next = newNode;

    }

    int pop() {
        if (isEmpty()) { return -1; }
        
        Node* deleted = tail->prev;
        int val = deleted->val;

        tail->prev = deleted->prev;
        deleted->prev->next = tail;

        delete deleted;
        return val;
    }

    int popleft() {
        if (isEmpty()) { return -1; }

        Node* deleted = head->next;
        int val = deleted->val;
        
        head->next = deleted->next;
        deleted->next->prev = head;

        delete deleted;
        return val;
    }
};
