# VvTalk
Tool for virtual vocalist talkoid in Mandarin. 汉语普通话语调教辅助工具。

版本号：1.0.1

打包好的版本可以在b站专栏找到度盘链接，同时在vsqx.top上配布。

手动构建环境：

1. 安装MiniConda

2. 创建一个虚拟环境并激活

`conda create -n VvTalk python=3.8

conda activate VvTalk`

3. 确保终端的工作目录在项目的根目录后，运行setup.py

`setup.py'

4. 若安装完成后的使用过程中，在自动对齐时报错并对齐失败，可能是因为Montreal-Forced-Aligner的一个已经修复但尚未更新漏洞。查看其版本，若为2.0.0rc5，则将本项目中 setup_install/Monteral-Forced-Aligner/corpus/acoustic_corpus.py 文件替换掉对应目录下原有的文件，可以解决这个bug。


之前开源的[TyTalk](https://github.com/GalaxieT/TyTalk)算法对应本项目中的reliance.tyTalk


编程太难了555
