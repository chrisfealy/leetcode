var mergeTwoLists = function(list1, list2) {
    let head = node = new ListNode()
    while(list1 && list2) {
        if(list1.val < list2.val) {
            node.next = list1
            list1 = list1.next
        }
        else {
            node.next = list2
            list2 = list2.next
        }
        node = node.next
    }
    node.next = list1 || list2
    return head.next
};
