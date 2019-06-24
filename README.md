#Simulinkに関するファイル群
## simulinkcode.py
1.実行すると実行ディレクトリ直下でgithubからMatlab属性のファイルでsimulinkと名のつくレポジトリを検索する。
1.そこで得られたレポジトリをcloneする
1.ディレクトリ直下にあるslxファイルをtestディレクトリに移動する。
以上のを駆使してsimukinkファイルを集める。
3.は少々いじる必要あり。
2019/6/22:classに書き換えました。細かいオプションを追加。
2019/6/22:正しい動作をすることを確認。容量に気をつけましょう.
2019/6/24:MDLpursetool.pyを使ってみたが動かない。
具体的なerrorcodeは以下

>~/resesrch/simulink_test_time_estimation/testExample/fourBar.mdl
>read
>Traceback (most recent call last):
>  File "MDLparsetool.py", line 294, in <module>
>    main()
>  File "MDLparsetool.py", line 277, in main
>    result = mdlParser(filePath)
>  File "MDLparsetool.py", line 107, in mdlParser
>    result = mdlparser.parseString(mdldata)
>  File "/Users/ogatatakuya/.pyenv/versions/2.7.11/lib/python2.7/site-packages/pyparsing.py", line 1828, in parseString
>    raise exc
>pyparsing.ParseException: Expected "}" (at char 26802), (line:647, col:3)