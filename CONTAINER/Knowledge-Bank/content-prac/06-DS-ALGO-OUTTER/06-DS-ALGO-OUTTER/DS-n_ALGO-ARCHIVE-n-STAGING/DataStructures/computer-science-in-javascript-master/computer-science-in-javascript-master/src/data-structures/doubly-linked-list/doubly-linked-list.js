const head = Symbol("head");
const tail = Symbol("tail");
class DoublyLinkedListNode {
    constructor(data) {
        this.data = data;
        this.next = null;
        this.previous = null;
    }
}
class DoublyLinkedList {
    constructor() {
        this[head] = null;
        this[tail] = null;
    }
    add(data) {
        const newNode = new DoublyLinkedListNode(data);
        if (this[head] === null) {
            this[head] = newNode;
        } else {
            this[tail].next = newNode;
            newNode.previous = this[tail];
        }
        this[tail] = newNode;
    }
    insertBefore(data, index) {
        const newNode = new DoublyLinkedListNode(data);
        if (this[head] === null) {
            throw new RangeError(`Index ${index} does not exist in the list.`);
        }
        if (index === 0) {
            newNode.next = this[head];
            this[head].previous = newNode;
            this[head] = newNode;
        } else {
            let current = this[head];
            let i = 0;
            while ((current.next !== null) && (i < index)) {
                current = current.next;
                i++;
            }
            if (i < index) {
                throw new RangeError(`Index ${index} does not exist in the list.`);
            }
            current.previous.next = newNode;
            newNode.previous = current.previous;
            newNode.next = current;
            current.previous = newNode;
        }
    }
    insertAfter(data, index) {
        const newNode = new DoublyLinkedListNode(data);
        if (this[head] === null) {
            throw new RangeError(`Index ${index} does not exist in the list.`);
        }
        let current = this[head];
        let i = 0;
        while ((current !== null) && (i < index)) {
            current = current.next;
            i++;
        }
        if (i < index) {
            throw new RangeError(`Index ${index} does not exist in the list.`);
        }
        if (this[tail] === current) {
            this[tail] = newNode;
        } else {
            current.next.previous = newNode;
            newNode.next = current.next;
        }
        newNode.previous = current;
        current.next = newNode;
    }
    get(index) {
        if (index > -1) {
            let current = this[head];
            let i = 0;
            while ((current !== null) && (i < index)) {
                current = current.next;
                i++;          
            }
            return current !== null ? current.data : undefined;
        } else {
            return undefined;
        }
    }
    indexOf(data) {
        let current = this[head];
        let index = 0;
        while (current !== null) {
            if (current.data === data) {
                return index;
            }
            current = current.next;
            index++;
        }
        return -1;
    }
    find(matcher) {
        let current = this[head];
        while (current !== null) {
            if (matcher(current.data)) {
                return current.data;
            }
            current = current.next;
        }
        return undefined;
    }
    findIndex(matcher) {
        let current = this[head];
        let index = 0;
        while (current !== null) {
            if (matcher(current.data)) {
                return index;
            }
            current = current.next;
            index++;
        }
        return -1;
    }
    remove(index) {
        if ((this[head] === null) || (index < 0)) {
            throw new RangeError(`Index ${index} does not exist in the list.`);
        }
        if (index === 0) {
            const data = this[head].data;
            this[head] = this[head].next;
            if (this[head] === null) {
                this[tail] = null;
            } else {
                this[head].previous = null;
            }
            return data;
        }
        let current = this[head];
        let i = 0;
        while ((current !== null) && (i < index)) {
            current = current.next;
            i++;
        }
        if (current !== null) {
            current.previous.next = current.next;
            if (this[tail] === current) {
                this[tail] = current.previous;
            } else {
                current.next.previous = current.previous;
            }
            return current.data;
        }
        throw new RangeError(`Index ${index} does not exist in the list.`);
    }
    clear() {
        this[head] = null;
        this[tail] = null;
    }
    get size() {
        if (this[head] === null) {
            return 0;
        }
        let current = this[head];
        let count = 0;
        while (current !== null) {
            count++;
            current = current.next;
        }
        return count;
    }
    [Symbol.iterator]() {
        return this.values();
    }
    *values(){
        let current = this[head];
        while (current !== null) {
            yield current.data;
            current = current.next;
        }
    }
    *reverse(){
        let current = this[tail];
        while (current !== null) {
            yield current.data;
            current = current.previous;
        }
    }
    toString(){
        return [...this].toString();
    }
}
exports.DoublyLinkedList = DoublyLinkedList;
