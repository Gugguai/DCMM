import plotly.graph_objects as go

# 数据
years = [2018,2020, 2021, 2022, 2023, 2024]
values = [1,2, 4, 6, 10, 11]
custom_texts = ['海尔中央空调互联工厂入选全球首批"灯塔工厂"', '沈阳海尔冰箱互联工厂', 
    '青岛啤酒互联工厂、天津海尔洗衣机互联工厂', '郑州海尔热水器互联工厂、青岛海尔冰箱互联工厂', '天津海尔洗衣机互联工厂、卡奥斯合肥智控互联工厂、海尔青岛洗衣机互联工厂、海尔合肥空调互联工厂',
    '海尔胶州空调互联工厂']

# 创建折线图
fig = go.Figure(data=[
    go.Scatter(
        x=years,
        y=values,
        mode='lines+markers',
        hovertemplate='<b>年份</b>: %{x}<br><b>数值</b>: %{y}<br><b>说明</b>: %{text}<extra></extra>',
        text=custom_texts,
        line=dict(color='#1f77b4', width=3, shape='spline'),
        marker=dict(
            size=12,
            color='#1f77b4',
            line=dict(color='white', width=2),
            symbol='circle'
        )
    )
])

# 设置布局
fig.update_layout(
    title=dict(
        text='海尔互联工厂发展历程',
        font=dict(size=28, family='Arial', color='#2c3e50'),
        x=0.5,
        y=0.95
    ),
    xaxis=dict(
        title=dict(text='年份', font=dict(size=16, family='Arial', color='#2c3e50')),
        tickformat='d',
        tickmode='linear',
        dtick=1,
        showgrid=True,
        gridcolor='rgba(189, 195, 199, 0.2)',
        tickfont=dict(size=14, family='Arial')
    ),
    yaxis=dict(
        title=dict(text='互联工厂数量', font=dict(size=16, family='Arial', color='#2c3e50')),
        showgrid=True,
        gridcolor='rgba(189, 195, 199, 0.2)',
        tickfont=dict(size=14, family='Arial')
    ),
    showlegend=False,
    plot_bgcolor='white',
    paper_bgcolor='white',
    margin=dict(l=80, r=40, t=100, b=80),
    hoverlabel=dict(bgcolor='white', font_size=14, font_family='Arial')
)

# 显示图表
fig.show()