import streamlit as st
from query_agent import query_llama3, run_sql

st.set_page_config(page_title="E-Commerce AI Agent", layout="wide")
st.title("🛍️ E-Commerce Data Assistant")

question = st.text_input("Ask a question about your sales data:")

if question:
    with st.spinner("Thinking..."):
        sql, answer = query_llama3(question)

        if sql:
            st.subheader("💡 Answer")
            st.write(answer)

            st.subheader("🧠 Generated SQL")
            st.code(sql, language="sql")

            columns, rows = run_sql(sql)
            if columns and rows:
                st.subheader("📊 Query Result")
                st.dataframe(pd.DataFrame(rows, columns=columns))
        else:
            st.error(answer)
