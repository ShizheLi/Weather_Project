> 文件的4种状态

- `Untracked`：此文件在文件夹中，但并未加入到git库，通过`git add`命令转变为`staged`状态

- `Unmodified`：文件已经入库，但并未修改。如果文件修改，则状态变为`Modified`，如果使用`git rm`命令移出版本库，则变为`Untracked`文件；

- `Modified`：文件已修改。使用`git add`命令转为`staged`暂存状态，或使用`git checkout`命令丢弃修改，重新返回`Unmodified`状态；

- `Staged`：使用`git commit`命令将修改同步到库中，文件变为`Unmodified`状态，使用`git reset HEAD filename` 命令取消暂存，文件变为`Modified`状态。



> 忽略文件

在主目录下建立`.gitignore`文件

```md
*.txt      # 忽略所有以`.txt`结尾的文件
!lib.txt   # 忽略除`lib.txt`以外的文件
/tmp       # 
tmp/       #
doc/*.txt  #
```




