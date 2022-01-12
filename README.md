# 概要
2の倍数か、3の倍数か、5の倍数か判別するプログラムです。

ロボットシステム学の課題2で作成しました。

count.pyで出力した数字を判別します。

# 用意したもの

・Rasberry Pi 3b

・ノートPC

# 環境

ubuntu 20.04 LTS
Python 3

# 動画

[動画](https://youtu.be/L4v1cUIojZY)
実際に動作させた際の動画です。

# インストールと実行方法
## インストールの際は下記のコマンドを実行

```
cd catkin_ws
cd src
git clone https://github.com/umezawa0315/mypkg.git
cd ..
catkin_make
```

## 実行方法

ここからは、複数の端末での操作が必要です。

### Ａ端末での操作

```
roscore
```

### Ｂ端末での操作

```
rosrun mypkg count.py
```

### Ｃ端末での操作

count.pyが出力した数字を確認するコマンド

```
rostopic echo /count_up
```

### Ｄ端末での操作

Ｄ端末でtwice.pyの実行結果が確認可能

```
rosrun mypkg mypkg twice.py
```

# ライセンス

[BSD 3-Clause License](https://github.com/umezawa0315/mypkg/blob/master/LICENSE)
