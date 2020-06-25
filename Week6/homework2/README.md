# Malloc Challenge

## Best Fit
最も余らないところに保存する．
* free list を heap-listとして保存　
* あとはfirst-fitと一緒

数が少ないと、ソートの分時間食われるものの、使用率はあげられなかった．\
数が減ると平均探索時間が短くなっているためか、時間も使用率も共に上がった．\

```
Challenge 1: simple malloc => my malloc
Time: 37 ms => 1522 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 37 ms => 29 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 357 ms => 1211 ms
Utilization: 8% => 50%
==================================
Challenge 4: simple malloc => my malloc
Time: 66288 ms => 39712 ms
Utilization: 15% => 71%
==================================
Challenge 5: simple malloc => my malloc
Time: 47721 ms => 28976 ms
Utilization: 15% => 74%
==================================
```

## Worst Fit
最も余るところに保存する
* free list を逆向きのheap-listとして保存
* 一番目の要素が保存したい物より小さかったら新しく場所を確保
* それ以外の場合は一番目の場所に保存

見つけるのは早く終わるから実行時間は早くなるかと思ったがそうでもない、、？？

```
Challenge 1: simple malloc => my malloc
Time: 52 ms => 53 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 96 ms => 137 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 724 ms => 139044 ms
Utilization: 8% => 4%
==================================
Challenge 4: simple malloc => my malloc
Time: 56534 ms => 692227 ms
Utilization: 15% => 7%
==================================
Challenge 5: simple malloc => my malloc
Time: 35163 ms => 543346 ms
Utilization: 15% => 7%
==================================
```

