import os

p2t = 'ptt2txt.txt'
unsolved = 'unsolved_articles.txt'
err_count = 0

for dirName, sub_dirNames, fileNames in os.walk('ptt_articles'):
    for i in range(len(fileNames)):
        fn = 'ptt_articles/' + fileNames[i]
        file_Obj = open(fn, encoding = 'Big5-HKSCS')
        try:    
            data = file_Obj.read()
        except UnicodeDecodeError:
            with open(unsolved, 'a') as error_log:
                error_log.write('需手動開啟檔案:' + fileNames[i] + '\n')
                err_count += 1
        
        with open(p2t, 'a') as ptt_out:
            try:
                ptt_out.write(data)
            except UnicodeEncodeError:
                with open(unsolved, 'a') as error_log:
                    error_log.write('需手動開啟檔案:' + fileNames[i] + '\n')
                    err_count += 1
        file_Obj.close()
    with open(unsolved, 'a') as error_log:
        error_log.write('總文章數:%d 順利合併數:%d 需手動開啟數:%d \n\n' % (len(fileNames), len(fileNames) - err_count, err_count))
