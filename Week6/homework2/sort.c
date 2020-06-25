/**
 * @file        q12182666392.c
 * @brief       単方向リストを作成し，昇順ソートする
 * @author      Keitetsu
 * @date        2017/12/01
 * @copyright   Copyright (c) 2017 Keitetsu
 * @par         License
 *              This software is released under the MIT License.
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define LIST_CREATE_EXIT (-1) /*!< リスト作成終了コード */

/**
 * @struct  list_st
 * @brief   リスト構造体
 *
 * @typedef LIST
 * @brief   リスト構造体
 */
typedef struct list_st
{
    int number;           /*!< 数値 */
    struct list_st *next; /*!< 次の要素のポインタ */
} LIST;

/**
 * @brief   リストを作成する
 * @return          リストの先頭ポインタ
 */
static LIST *createList(void);

/**
 * @brief   リストの内容を表示する
 * @param[in]       head        リストの先頭ポインタ
 */
static void printList(LIST *head);

/**
 * @brief   リストを昇順ソートする
 * @param[in]       head        リストの先頭ポインタ
 * @return          リストの先頭ポインタ
 */
static LIST *sortList(LIST *head);

/**
 * @brief   リストを削除する
 * @param[in]       head        リストの先頭ポインタ
 * @retval          NULL        リスト消去成功
 * @retval          Others      リスト消去失敗
 */
static LIST *deleteList(LIST *head);

int main(void)
{
    LIST *head;

    head = NULL;

    head = createList();

    printList(head);

    head = sortList(head);

    printList(head);

    head = deleteList(head);

    return 0;
}

static LIST *createList(void)
{
    LIST *head, *temp, *prev;
    char buf[20];
    int number, count;

    printf("リストの作成を開始します (終了する場合は %d を入力してください)\n", LIST_CREATE_EXIT);

    head = NULL;
    temp = NULL;
    prev = NULL;
    while (1)
    {
        printf("数値を入力してください==> ");
        fgets(buf, sizeof(buf), stdin);
        number = atoi(buf);

        if (number == LIST_CREATE_EXIT)
        {
            break;
        }

        temp = (LIST *)malloc(sizeof(LIST));
        temp->number = number;
        temp->next = NULL;

        if (head == NULL)
        {
            head = temp;
        }
        else
        {
            prev->next = temp;
        }
        prev = temp;
    }

    printf("リストの作成を終了しました\n");

    return head;
}

static void printList(LIST *head)
{
    LIST *temp;
    int count;

    printf("リストの内容を表示します\n");

    temp = head;
    count = 0;
    while (temp != NULL)
    {
        printf("[%d] %d", count, temp->number);
        if (temp->next == NULL)
        {
            printf("\n");
        }
        else
        {
            printf(", ");
        }

        temp = temp->next;
        count++;
    }

    return;
}

static LIST *sortList(LIST *head)
{
    LIST *headUnsorted, *headSorted;
    LIST *max, *prevMax, *prevComp;

    printf("リストを昇順ソートします\n");

    headUnsorted = head; /* 未ソートリスト */
    headSorted = NULL;   /* ソート済リスト */
    while (headUnsorted != NULL)
    {
        max = headUnsorted;      /* 最大値要素を示すポインタ */
        prevMax = NULL;          /* 最大値要素の前の要素を示すポインタ */
        prevComp = headUnsorted; /* 比較対象要素の前の要素を示すポインタ */
        while (prevComp->next != NULL)
        {
            /* 最大値要素と比較対象要素を比較する */
            if ((prevComp->next)->number > max->number)
            {
                /* 最大値要素の更新 */
                max = prevComp->next;
                prevMax = prevComp;
            }
            /* 比較対象要素を更新 */
            prevComp = prevComp->next;
        }

        /* 最大値要素を未ソートリストから削除 */
        if (prevMax == NULL)
        {
            headUnsorted = max->next;
        }
        else
        {
            prevMax->next = max->next;
        }

        /* 最大値要素をソート済リストの先頭に追加 */
        if (headSorted == NULL)
        {
            headSorted = max;
            max->next = NULL;
        }
        else
        {
            max->next = headSorted;
            headSorted = max;
        }
    }

    return headSorted;
}

static LIST *deleteList(LIST *head)
{
    LIST *temp;

    while (head != NULL)
    {
        temp = head;
        head = head->next;
        free(temp);
    }

    return head;
}