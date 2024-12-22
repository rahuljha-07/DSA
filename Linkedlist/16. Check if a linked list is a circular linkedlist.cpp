bool isCircular(Node *head)
{
   // If the list is empty, it's not circular
   if(head == NULL) return false;  // Return false for empty list, as it's not circular

   // Initialize a temporary pointer to traverse the list
   Node *temp = head;

   // Traverse the list and check if any node's next points to the head
   while (temp) {
      if (temp->next == head) {  // If current node's next pointer is the head, it's circular
         return true;
      }
      temp = temp->next;  // Move to the next node
   }

   // If we reach the end of the list without finding a cycle, it's not circular
   return false;
}
