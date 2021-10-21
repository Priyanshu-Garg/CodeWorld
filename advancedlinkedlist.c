#include<stdio.h>
#include<stdlib.h>
struct node{
int data;
struct node*next;};
void display(struct node*ptr)
{
    while(ptr!=NULL)
    {
        printf("%d ",ptr->data);
        ptr=ptr->next;
    }
}
void reverse_display(struct node*ptr)
{
    int n=0,i;
    int a[100];
    while(ptr!=NULL)
    {
        a[n]=ptr->data;
        n++;
        ptr=ptr->next;
    }
    while(n>0)
    {
        printf("%d ",a[n-1]);
        n--;
    }
}
void deletion(struct node*ptr)
{
    int num;
    printf("which node do you want to remove enter the number\n");
    scanf("%d",&num);
    struct node*temp,*t;
    if(ptr->data==num)
    {
        t=ptr;
        ptr=ptr->next;
        free(t);
    }
    else
    {
        temp=ptr;
        while(temp->next!=NULL)
        {
            if(temp->next->data==num)
        {
            t=temp->next;
            temp->next=temp->next->next;
            free(t);
        }
        else
        {
            temp=temp->next;
        }}
    }
}
void count_node(struct node*ptr)
{int f=0;
    while(ptr!=NULL)
    {
        f++;
        ptr=ptr->next;
    }
    printf("No.of Nodes are :%d\n",f);
}
void reverse(struct node*start)
{
    struct node*c=NULL,*pre=NULL,*n=NULL;
    c=start;
    while(c!=NULL)
    {
        n=c->next;
        c->next=pre;
        pre=c;
        c=n;
    }
    start=pre;
    display(start);

}
int main()
{
    struct node*start=NULL,*temp=NULL,*temp2=NULL;
    int n,f=0;
    do{
        scanf("%d",&n);
        temp2=temp;
        temp=(struct node*)malloc(sizeof(struct node));
        temp->next=NULL;
        temp->data=n;
        if(start==NULL)
            start=temp;
        else
            temp2->next=temp;
    }while(n!=0);
    count_node(start);
    reverse(start);


}
