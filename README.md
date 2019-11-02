# ptt2txt
transfer ptt backup articles to a single txt file

功能：把ptt的備份文章整合到一個txt檔，因而可以快速流覽、查詢備份的所有文章內容

step1. 在自己個版(有版主權限)內按 u 進行備份, 可以把看板文章&精華區文章備份到指定信箱

step2. 收到備份的tgz檔後解壓縮, 裡面每一個檔案為一篇文章, 可以用txt或word打開來直接看內容

step3. 把解壓縮後的文章檔放到 "ptt_articles" 的資料夾底下

step4. 執行 "ptt2txt.py", 就會看到有一個 "ptt2txt.txt" 檔案生成, 裡面就是整合的結果

備註: 因為編碼問題, 有些文章沒辦法順利整合, 那些文章的檔案名稱會紀錄在另一生成檔 "unsolved_articles.txt" 中, 那些文章目前只能自行手動用記事本orWORD開啟.
