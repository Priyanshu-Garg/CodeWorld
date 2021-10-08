#include<stdio.h>
#include<stdlib.h>
typedef struct link
{
    struct link*prev;
    int info;
    struct link*next;
}node;
void display(node*start)
{
    while(start!=NULL)
    {
        printf("%d",start->info);
        start=start->next;
    }
}

int main()
{
    node*start=NULL,*end=NULL;
      node*t=NULL;
    int num;
    do{
    scanf("%d",&num);
    t=(node*)malloc(sizeof(node));
    t->info=num;
    t->next=NULL;
    t->next=end;
    if(start==NULL)
    {
        start=end=t;
    }
    else
    {
        end->next=t;
        end=t;
    }while(num!=0);
    display(start);
    }}
