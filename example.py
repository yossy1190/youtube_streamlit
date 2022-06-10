import streamlit as st
import time

# タイトルを出力
st.title('streamlit サンプルタイトル')
# 文字情報を出力
st.write('Interactiove widgets')

left_column,right_column=st.columns(2)

button=left_column.button('右カラムに文字を表示する')
if button:
    right_column.write('ここは右カラムです')
    print('ok')

st.empty()

st.write('Start!!')

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'表示中{i+1}%')
    bar.progress(i+1)
    time.sleep(0.05)

'Done!!'

# if st.checkbox('Show Image'):
#     img=Image.open('icon.jpg')
#     st.image(img,caption='my image',use_column_width=True)

text_input=st.text_input(
    "あなたが好きな趣味を教えてください。",
    )

expander=st.expander('問い合わせ1')
expander.write('回答1')
expander=st.expander('問い合わせ2')
expander.write('回答2')
expander=st.expander('問い合わせ3')
expander.write('回答3')
expander=st.expander('問い合わせ4')
expander.write('回答4')

'あんたの好きな趣味は、',text_input,'です'

condition=st.slider('あなたのコンディションは？',0,100,50)
'コンディション',condition

# df=pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=["lat","lon"]
# )

# st.bar_chart(df)
# st.map(df)

# st.write(df.style.highlight_max())
# st.dataframe(df.style.highlight_max())
# st.table(df.style.highlight_max())

