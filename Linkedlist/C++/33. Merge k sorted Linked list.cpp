    Node* mergesort(Node* first,Node* second){
    Node* third=NULL;
    Node* last=NULL;
    if(first->data <second->data){
        third=last=first;
        first=first->next;
        last->next=NULL;
    }
    else{
        third=last=second;
        second=second->next;
        last->next=NULL;
    }
    while(first!=NULL and second!=NULL){
        if(first->data < second->data){
            last->next=first;
            last=first;
            first=first->next;
            last->next=NULL;
        }
        else{
            last->next=second;
            last=second;
            second=second->next;
            last->next=NULL;
        }
    }
    if(first!=NULL) last->next=first;
    else last->next=second;
    return third;
}

//Function to merge K sorted linked list.
Node * mergeKLists(Node *arr[], int k){
    int last=k-1;
    while(last!=0){
        int  i=0;
        int  j=last;
        while(i<j){
            arr[i]=mergesort(arr[i],arr[j]);
            i++;
            j--;
            if(i>=j) last=j;
        }
    }
    return arr[0];
}
