import streamlit as st
import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")

st.sidebar.image(r"C:\Users\DELL\OneDrive\Desktop\Chat'sUp\C'sU_logo.png", use_column_width=True)

st.sidebar.markdown("<h1 style='color: green;'>WhatsApp Chat Analyzer</h1>", unsafe_allow_html=True)

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df=preprocessor.preprocess(data)

    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user = st.sidebar.selectbox("Show analysis w.r.t :",user_list)

    if st.sidebar.button("Show Analysis"):
        num_messages, num_emojis, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

        st.markdown("<h1 style='color: orangered;'>Top Statistics</h1>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Emojis")
            st.title(num_emojis)

        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)

        with col4:
            st.header("Links Shared")
            st.title(num_links)

        st.markdown("<h1 style='color: orangered;'>Activity Map</h1>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most Busy Day")

            busy_day = helper.week_activity_map(selected_user, df)

            fig, ax = plt.subplots()
            fig.patch.set_facecolor('#262730')
            ax.set_facecolor('#262730')

            ax.bar(busy_day.index, busy_day.values, color='purple')

            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')

            plt.xticks(rotation='vertical', color='white')

            ax.set_xlabel('Day', color='white')
            ax.set_ylabel('Messages', color='white')
            ax.set_title('Most Busy Day', color='white')

            st.pyplot(fig)

        with col2:
            st.header("Most Busy Month")

            busy_month = helper.month_activity_map(selected_user, df)

            fig, ax = plt.subplots()
            fig.patch.set_facecolor('#262730')
            ax.set_facecolor('#262730')

            ax.bar(busy_month.index, busy_month.values, color='orange')

            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')

            plt.xticks(rotation='vertical', color='white')

            ax.set_xlabel('Month', color='white')
            ax.set_ylabel('Messages', color='white')
            ax.set_title('Most Busy Month', color='white')

            st.pyplot(fig)

        st.markdown("<h1 style='color: orangered;'>Weekly Activity Map</h1>", unsafe_allow_html=True)
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

        if selected_user == 'Overall':
            st.markdown("<h1 style='color: orangered;'>Most Busy Users</h1>", unsafe_allow_html=True)
            x,df_new = helper.fetch_busy_users(df)
            fig, ax = plt.subplots()
            fig.patch.set_facecolor('#262730')
            ax.set_facecolor('#262730')
            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color= 'g')
                plt.xticks(rotation='vertical', color='white')
                ax.tick_params(axis='y', colors='white')
                for i, value in enumerate(x.values):
                    ax.text(i, value, str(value), ha='center', va='bottom', color='white')

                st.pyplot(fig)

            with col2:
                st.dataframe(df_new)
        st.markdown("<h1 style='color: orangered;'>Word Cloud</h1>", unsafe_allow_html=True)
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        most_common_df = helper.most_common_words(selected_user, df)

        fig, ax = plt.subplots()

        fig.patch.set_facecolor('#262730')
        ax.set_facecolor('#262730')
        ax.barh(most_common_df[0], most_common_df[1], color='steelblue')

        plt.xticks(rotation='vertical', color='white')

        st.markdown("<h1 style='color: orangered;'>Most Common Words</h1>", unsafe_allow_html=True)

        for i, value in enumerate(most_common_df[1]):
            ax.text(value, i, str(value), ha='left', va='center', color='white')

        ax.tick_params(axis='y', colors='white')

        st.pyplot(fig)

        emoji_df = helper.emoji_analysis(selected_user, df)
        st.markdown("<h1 style='color: orangered;'>Emoji Analysis</h1>", unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots()
            fig.patch.set_facecolor('black')
            ax.set_facecolor('black')

            explode = [0.15] * len(emoji_df['count'])
            ax.pie(emoji_df['count'], labels=emoji_df['emoji'], autopct='%1.1f%%', explode=explode, shadow=True)

            st.pyplot(fig)

        st.markdown("<h1 style='color: orangered;'>Timeline</h1>", unsafe_allow_html=True)
        timeline = helper.monthly_timeline(selected_user, df)

        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#262730')
        ax.set_facecolor('#262730')

        ax.plot(timeline['time'], timeline['message'], color='darkgreen')

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        plt.xticks(rotation='vertical', color='white')

        ax.set_xlabel('Time', color='white')
        ax.set_ylabel('Messages', color='white')
        ax.set_title('Monthly Timeline', color='white')

        st.pyplot(fig)

        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)

        fig, ax = plt.subplots()
        fig.patch.set_facecolor('#262730')
        ax.set_facecolor('#262730')

        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='darkgreen')

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        plt.xticks(rotation='vertical', color='white')
        ax.set_xlabel('Date', color='white')
        ax.set_ylabel('Messages', color='white')
        ax.set_title('Daily Timeline', color='white')

        st.pyplot(fig)

