import pandas as pd
import tabula

# lattice=Trueでテーブルの軸線でセルを判定
dfs = tabula.read_pdf("https://www.zeneiren.or.jp/cgi-bin/pdfdata/20190925114437.pdf", lattice=True, pages = '40')

# PDFの表をちゃんと取得できているか確認
# for df in dfs:
#     display(df)

# csv/Excelとして保存(今回はdfs[0]のみ)
df = dfs[0].rename(columns={'高ストレ\rス者数': '高ストレス者数', '高ストレス\r者の割合': '高ストレス者の割合'})
df.to_csv("PDFの表.csv", index=None) # csv
df.to_excel("PDFの表.xlsx", index=None) # Excel