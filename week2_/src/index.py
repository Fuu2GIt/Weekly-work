articles = []
id = 1

while True:
    print("\n=== 簡易noteアプリ ===")
    print("1: 記事を投稿する")
    print("2: 記事を見る")
    print("3: 終了する")
    print("4: 全記事を削除する")
    print("5 選んだ番号の記事を削除する")
    
    # ユーザーからの入力を受け取る
    choice = input("番号を選んでください (1/2/3/4/5): ")
    
    if choice == '1':
        # 記事の入力
        title = input("タイトル: ")
        content = input("本文: ")
        
        # 辞書型を使ってタイトルと本文をセットにしてリストに追加
        article = {"title": title, "content": content, "id":id}
        articles.append(article)
        id = id+1
        print("＞記事を投稿しました！")
        
    elif choice == '2':
        print("\n--- 記事一覧 ---")
        # 記事がない場合の処理
        if len(articles) == 0:
            print("＞まだ記事がありません。")
        else:
            # for文でリストの中身を順番に表示
            for art in articles:
                print(f"[{art['id']}] {art['title']}")
                print(f"    {art['content']}\n")
                
    elif choice == '3':
        print("＞アプリを終了します。")
        break  # ループを抜けて終了する

    elif choice == '4':
        articles.clear()
        print("＞記事を削除しました")

    elif choice == '5':
        print("＞選んだ記事番号を削除します")
        for art in articles:
            print(f"[{art['id']}] {art['title']}")
            print(f"    {art['content']}\n")
        remove = int(input("＞記事番号を入力してください: "))

        for art in articles:
            if art['id'] == remove:
                 articles.remove(art)

        else:    
            print("＞正しい番号を入力してください")
        
else:
        print("＞正しい番号を入力してください。")