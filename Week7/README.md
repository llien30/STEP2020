# homework1
#### 予想
`ikj <= kij < ijk <= jik < jki <= kji`

#### 結果
`ikj < kij < jik < ijk < jki < kji`

|roop|time[ms] |
|:---|:--------|
|ijk |53908.651|
|ikj |17487.455|
|jki |55805.578|
|jik |31203.471|
|kij |30053.042|
|kji |93590.161|

# homework2
|roop|time[ms] |
|:---|:--------|
|ijk |682624.87|
|ikj |633010.53|
|jki |503420.45|
|jik |533685.53|
|kij |422055.20|
|kji |607516.67|

* Pythonでは、処理にかかるスピードがC++の10倍以上であるため、メモリから読み込んでくるのにかかる時間の差がそれほど大きな差にならない